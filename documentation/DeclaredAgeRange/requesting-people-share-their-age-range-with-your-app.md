# Requesting people’s age range information in your app

**Framework**: Declared Age Range

Ask people to share their age range with your app, and tailor features for adults, teens, and children while preserving privacy.

#### Overview

Use the Declared Age Range API to request age information from people using your app without requiring them to share their exact birthdate. You specify age gates (age thresholds like 13, 16, or 18), and the system returns an age range — a span of ages with a minimum and maximum — the person falls into. When you request an age range, the system presents a sheet that describes the data you’re requesting and asks people to grant permission to share their age range with your app. For teens and children in a family sharing group, parents or guardians control whether to always share age range information, never share it, or decide on an app-by-app basis.

Based on the person’s response, the system returns their shared age range with a [`lowerBound`](agerangeservice/agerange/lowerbound.md) and [`upperBound`](agerangeservice/agerange/upperbound.md), or if they’re in a nonregulated region, the system can return [`AgeRangeService.Response.declinedSharing`](agerangeservice/response/declinedsharing.md). You also receive information about whether parental controls are turned on. The system also provides the age range declaration source when available.

To use Declared Age Range, add the [`com.apple.developer.declared-age-range`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.declared-age-range) entitlement to your app by enabling the Declared Age Range capability on your target in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

The system protects privacy by caching age range responses. When a person’s age crosses into a new range (for example, when they turn 13), the API continues returning the previous range until the anniversary of their original declaration. People can manually update this in settings if they want immediate access to new features with the following steps:

1. Open Settings on iPhone or iPad, or System Settings on Mac.
2. Choose [your name].
3. Choose Personal Information > Age Range for Apps.

> ❗ **Important**: Data from the Declared Age Range API is based on information declared by an end user, or their parent or guardian. You are solely responsible for ensuring compliance with associated laws or regulations that may apply to your app.

#### Check Eligibility for Age Related Features

Before implementing age features in your app, check whether the person using your app is in a region that requires age assurance. Use [`isEligibleForAgeFeatures`](agerangeservice/iseligibleforagefeatures.md) to determine whether associated laws or regulations may apply to your app based on the person’s location and account settings. This property returns `true` when your app needs to support age assurance for the current user. In macOS, [`isEligibleForAgeFeatures`](agerangeservice/iseligibleforagefeatures.md) returns `false` because the system doesn’t require age assurance for the person or device. However, you can still call `requestAgeRange` in macOS to get the declared age range.

When `isEligibleForAgeFeatures` returns `true`, the person is in a regulated region that requires age assurance. In some regulated regions, the system automatically provides the person’s age range — they can’t decline sharing. These regions determine the age gates that the system uses to return age ranges, and it may differ from the age gates you specify in your request. In nonregulated regions, people grant permission to share age range information that they or their parent or guardian have already registered with the system. When they share, the system returns age ranges based on the age gates you specify (such as 13, 16, and 18). If the person declines, you receive a `declinedSharing` response.

```swift
do {
    let isEligible = try await AgeRangeService.shared.isEligibleForAgeFeatures
    if isEligible {
        // Person is eligible; enable age features.
    } else {
        // Handle case where person isn't eligible.
    }
} catch {
    // Handle error during eligibility check.
}
```

> ❗ **Important**: Don’t use [`significantAppChangeApprovalRequired`](agerangeservice/parentalcontrols/significantappchangeapprovalrequired.md). Instead, use both [`isEligibleForAgeFeatures`](agerangeservice/iseligibleforagefeatures.md) and [`requestAgeRange(ageGates:_:_:in:)`](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md) to detect when you need to communicate significant changes to parents and guardians.

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange

@Environment(\.requestAgeRange) var requestAgeRange

func checkParentalNotification() async {
    do {
        let isEligible = try await AgeRangeService.shared.isEligibleForAgeFeatures
        guard isEligible else { return }
        
        let response = try await requestAgeRange(ageGates: 18)
        
        if case let .sharing(ageRange) = response,
            let upperBound = ageRange.upperBound,
            upperBound < 18 {
            // Person is under 18; notify parent or guardian of significant changes.
        }
    } catch {
        // Handle error.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange

func checkParentalNotification() async {
    do {
        let isEligible = try await AgeRangeService.shared.isEligibleForAgeFeatures
        guard isEligible else {
            // Age features not required in this region.
            return
        }

        let response = try await AgeRangeService.shared.requestAgeRange(
            ageGates: 18,
            in: viewControllerOrWindow // Use UIViewController in UIKit or NSWindow in AppKit.
        )

        switch response {
        case let .sharing(ageRange):
            if let upperBound = ageRange.upperBound, upperBound < 18 {
                // Person is under 18; notify parent or guardian of significant changes.
            }
        case .declinedSharing:
            // In some regulated regions, the system automatically provides the person's age range — the person can't decline sharing.
            break
        }
    } catch {
        // Handle error.
    }
}
```

#### Check Required Regulatory Features

After determining that age features are required for a person, use [`requiredRegulatoryFeatures`](agerangeservice/requiredregulatoryfeatures.md) to understand which regulatory requirements apply. This property returns a set of [`AgeRangeService.RegulatoryFeature`](agerangeservice/regulatoryfeature.md) values that tell you which actions you need to take for compliance.

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange

func checkRegulatoryRequirements() async {
    do {
        let requiredFeatures = try await AgeRangeService.shared.requiredRegulatoryFeatures

        if requiredFeatures.contains(.declaredAgeRangeRequired) {
            // You must request the person's age range.
            // Implement age range request flow.
        }

        if requiredFeatures.contains(.significantAppChangeRequiresParentalConsent) {
            // Significant app changes require parental or guardian consent.
            // Use PermissionKit to request consent from parents or guardians.
        }

        if requiredFeatures.contains(.significantAppChangeRequiresAdultNotification) {
            // You must notify the adult user of your app of significant app changes.
            // Present appropriate notification UI.
        }
    } catch {
        // Handle error.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange

func checkRegulatoryRequirements() async {
    do {
        let requiredFeatures = try await AgeRangeService.shared.requiredRegulatoryFeatures

        if requiredFeatures.contains(.declaredAgeRangeRequired) {
            // You must request the person's age range.
            // Implement age range request flow.
        }

        if requiredFeatures.contains(.significantAppChangeRequiresParentalConsent) {
            // Significant app changes require parental or guardian consent.
            // Use PermissionKit to request consent from parents or guardians.
        }

        if requiredFeatures.contains(.significantAppChangeRequiresAdultNotification) {
            // You must notify the adult user of your app of significant app changes.
            // Present appropriate notification UI.
        }
    } catch {
        // Handle error.
    }
}
```

#### Request an Age Range

To ask the system for an age range, call [`requestAgeRange(ageGates:_:_:in:)`](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md) in UIKit, [`requestAgeRange(ageGates:_:_:in:)`](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md) in AppKit, or use the [`callAsFunction(ageGates:_:_:)`](declaredagerangeaction/callasfunction(agegates:_:_:).md) environment value in SwiftUI.

Define the age gates, which are the minimum ages important to your app, as parameters. You can specify up to three age gates, which create up to four possible age ranges. Each range must be at least two years in duration. Handle the response to determine which age-appropriate features are accessible based on the person’s age range. Check if the response indicates the person is sharing their age range, then use the minimum age you specify to grant access to age-appropriate features:

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange

@Environment(\.requestAgeRange) var requestAgeRange

func checkAgeRange() async {
    do {
        let response = try await requestAgeRange(ageGates: 13, 15, 18)

        guard case let .sharing(ageRange) = response else {
            // Person declined sharing.
            return
        }

        guard let lowerBound = ageRange.lowerBound else {
            // Person is under 13; enable age-appropriate experience.
            return
        }

        if lowerBound >= 18 {
            // Enable features for age 18 and over.
        } else if lowerBound >= 15 {
            // Enable features for ages 15-17.
        } else {
            // Enable features for ages 13-14.
        }
    } catch {
        // Handle error.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange

func checkAgeRange() async {
    do {
        let response = try await AgeRangeService.shared.requestAgeRange(
            ageGates: 13, 15, 18,
            in: viewControllerOrWindow // Use UIViewController in UIKit or NSWindow in AppKit.
        )

        switch response {
        case let .sharing(ageRange):
            guard let lowerBound = ageRange.lowerBound else {
                // Person is under 13; enable age-appropriate experience.
                return
            }

            if lowerBound >= 18 {
                // Enable features for age 18 and over.
            } else if lowerBound >= 15 {
                // Enable features for ages 15-17.
            } else {
                // Enable features for ages 13-14.
            }

        case .declinedSharing:
            // In some regulated regions, the system automatically provides the person's age range — the person can't decline sharing.
            break
        }
    } catch {
        // Handle error.
    }
}
```

To identify if a person is under a specific age range, check the `upperBound` value:

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange

@Environment(\.requestAgeRange) var requestAgeRange

func checkAgeRange() async {
    do {
        let response = try await requestAgeRange(ageGates: 18)

        guard case let .sharing(ageRange) = response else {
            // Person declined sharing.
            return
        }

        if let upperBound = ageRange.upperBound, upperBound < 18 {
            // Person is under 18; enable age-appropriate experience.
            // Notify parents or guardians of significant changes.
        } else {
            // Person is over 18; grant full access.
        }
    } catch {
        // Handle error.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange

func checkAgeRange() async {
    do {
        let response = try await AgeRangeService.shared.requestAgeRange(
            ageGates: 18,
            in: viewControllerOrWindow // Use UIViewController in UIKit or NSWindow in AppKit.
        )

        switch response {
        case let .sharing(ageRange):
            if let upperBound = ageRange.upperBound, upperBound < 18 {
                // Person is under 18; enable age-appropriate experience.
                // Notify parents or guardians of significant changes.
            } else {
                // Person is over 18; grant full access.
            }
        case .declinedSharing:
            // In some regulated regions, the system automatically provides the person's age range — the person can't decline sharing.
            break
        }
    } catch {
        // Handle error.
    }
}
```

#### Handle Errors

The API throws errors when requests fail or the service is unavailable. Handle these errors to provide appropriate fallback experiences:

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange

@Environment(\.requestAgeRange) var requestAgeRange

func checkAgeRange() async {
    do {
        let response = try await requestAgeRange(ageGates: 13, 16)
        // Handle age range request response.
    } catch AgeRangeService.Error.invalidRequest {
        // Handle invalid request error.
    } catch AgeRangeService.Error.notAvailable {
        // Handle age range not available error.
    } catch {
        // Handle other errors.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange

func checkAgeRange() async {
    do {
        let response = try await AgeRangeService.shared.requestAgeRange(
            ageGates: 13, 16, 
            in: viewControllerOrWindow // Use UIViewController in UIKit or NSWindow in AppKit.
        )
        // Handle age range request response.
    } catch AgeRangeService.Error.invalidRequest {
        // Handle invalid request error.
    } catch AgeRangeService.Error.notAvailable {
        // Handle age range not available error.
    } catch {
        // Handle other errors.
    }
}
```

#### Interpret the Response

After a person grants your app access to their age range, the system returns a response:

- A [`lowerBound`](agerangeservice/agerange/lowerbound.md) and [`upperBound`](agerangeservice/agerange/upperbound.md) that define the age range based on your age gates
- An age range declaration that describes how the person set the age
- Active parental controls when applicable

Use the `lowerBound` value to enforce minimum ages in your app. When the `lowerBound` value is `nil`, the person is below your lowest age gate. When the `upperBound` is `nil`, the person meets or exceeds your highest age gate. Treat the response as an age range rather than inferring an exact age.

Check the [`ageRangeDeclaration`](agerangeservice/agerange/agerangedeclaration.md) to understand how the person or their parent or guardian set their age range. The declaration method indicates whether the age was self-declared, guardian-declared, or verified using a payment method, government ID, or another method. Apply appropriate controls based on the declaration method.

> **Note**: The declaration methods (`checkedByOtherMethod`, `guardianCheckedByOtherMethod`, `governmentIDChecked`, `guardianGovernmentIDChecked`, `paymentChecked`, and `guardianPaymentChecked`) are only available in some regions. For more information, refer to [`Next steps for apps distributed in Texas`](https://developer.apple.comhttps://developer.apple.com/news/?id=2ezb6jhj).

```swift
if #available(iOS 26.2, macOS 26.2, *) {
    // Handle all age range declarations supported in iOS 26.2 and later and macOS 26.2 and later.
    switch declaration {
        case .selfDeclared:
        case .guardianDeclared:
        case .checkedByOtherMethod:
        case .guardianCheckedByOtherMethod:
        case .governmentIDChecked:
        case .guardianGovernmentIDChecked:
        case .paymentChecked:
        case .guardianPaymentChecked:
    }
} else if #available(iOS 26, macOS 26, *) {
    // Handle all age range declarations supported in iOS 26 and 26.1 and macOS 26 and 26.1.
    switch declaration {
        case .selfDeclared:
        case .guardianDeclared:
    }
}
```

#### Request Permission From Parents or Guardians

When the person’s age range has an `upperBound` value that indicates they’re not yet an adult in their region, check [`activeParentalControls`](agerangeservice/agerange/activeparentalcontrols.md) to determine if Screen Time or Family Controls restrictions are active. Use PermissionKit to facilitate approval requests from their parent or guardian for specific capabilities, such as messaging. Design your features so that parental controls always take precedence over your own in-app settings:

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange

@Environment(\.requestAgeRange) var requestAgeRange

func checkCommunicationLimits() async {
    do {
        let response = try await requestAgeRange(ageGates: 13)

        guard case let .sharing(ageRange) = response else {
            // Person declined sharing.
            return
        }

        if ageRange.activeParentalControls.contains(.communicationLimits) {
            // Child has communication limits turned on.
            // Use PermissionKit to request messaging permissions.
        }
    } catch {
        // Handle error.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange

func checkCommunicationLimits() async {
    do {
        let response = try await AgeRangeService.shared.requestAgeRange(
            ageGates: 13,
            in: viewControllerOrWindow // Use UIViewController in UIKit or NSWindow in AppKit.
        )

        switch response {
        case let .sharing(ageRange):
            if ageRange.activeParentalControls.contains(.communicationLimits) {
                // Child has communication limits turned on.
                // Use PermissionKit to request messaging permissions.
            }
        case .declinedSharing:
            // In some regulated regions, the system automatically provides the person's age range — the person can't decline sharing.
            break
        }
    } catch {
        // Handle error.
    }
}
```

#### Handle Significant App Updates

When your app undergoes significant changes — such as changes to its age rating, features, or data practices — you may need to notify people or obtain consent before they continue using your app. Use [`requiredRegulatoryFeatures`](agerangeservice/requiredregulatoryfeatures.md) to determine if notification or consent is required for the person. For more information, see [`Age assurance frameworks Q&A`](https://developer.apple.comhttps://developer.apple.com/support/age-assurance/).

If [`AgeRangeService.RegulatoryFeature.significantAppChangeRequiresAdultNotification`](agerangeservice/regulatoryfeature/significantappchangerequiresadultnotification.md) is present in the required features set, you must notify the adult user about your app’s significant changes before they continue using your app. Use [`showSignificantUpdateAcknowledgment(in:updateDescription:)`](agerangeservice/showsignificantupdateacknowledgment(in:updatedescription:).md) to display a system-provided interface where they can acknowledge the update:

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange

func handleSignificantUpdate(windowScene: UIWindowScene) async {
    do {
        let requiredFeatures = try await AgeRangeService.shared.requiredRegulatoryFeatures

        if requiredFeatures.contains(.significantAppChangeRequiresAdultNotification) {
            // You must notify the adult user about your app's significant changes.
            try await AgeRangeService.shared.showSignificantUpdateAcknowledgment(
                in: windowScene,
                updateDescription: "We've updated our app with new social features that allow direct messaging between people."
            )
        }
    } catch {
        // Handle error.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange

func handleSignificantUpdate() async {
    do {
        let requiredFeatures = try await AgeRangeService.shared.requiredRegulatoryFeatures

        if requiredFeatures.contains(.significantAppChangeRequiresAdultNotification) {
            // You must notify the adult user about your app's significant changes.
            try await AgeRangeService.shared.showSignificantUpdateAcknowledgment(
                in: windowScene, // Use UIWindowScene in UIKit or NSWindow in AppKit.
                updateDescription: "We've updated our app with new social features that allow direct messaging between people."
            )
        }
    } catch {
        // Handle error.
    }
}
```

If [`AgeRangeService.RegulatoryFeature.significantAppChangeRequiresParentalConsent`](agerangeservice/regulatoryfeature/significantappchangerequiresparentalconsent.md) is present in the required features set, parents or guardians must consent before children can continue using your app after a significant change. Create a [`SignificantAppUpdateTopic`](https://developer.apple.com/documentation/permissionkit/significantappupdatetopic) with a clear description of what changed, then use [`PermissionKit`](https://developer.apple.com/documentation/permissionkit) to request consent:

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange
import PermissionKit

func handleSignificantUpdate() async {
    do {
        let requiredFeatures = try await AgeRangeService.shared.requiredRegulatoryFeatures

        if requiredFeatures.contains(.significantAppChangeRequiresParentalConsent) {
            // A parent or guardian must consent on behalf of their child.
            let topic = SignificantAppUpdateTopic(
                description: "This update adds video calling and location sharing features."
            )
            // Use PermissionKit to request consent with the topic.
        }
    } catch {
        // Handle error.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange
import PermissionKit

func handleSignificantUpdate() async {
    do {
        let requiredFeatures = try await AgeRangeService.shared.requiredRegulatoryFeatures

        if requiredFeatures.contains(.significantAppChangeRequiresParentalConsent) {
            // A parent or guardian must consent on behalf of their child.
            let topic = SignificantAppUpdateTopic(
                description: "This update adds video calling and location sharing features."
            )
            // Use PermissionKit to request consent with the topic.
        }
    } catch {
        // Handle error.
    }
}
```

Use concise, understandable language that clearly explains what changed in your app. Parents and guardians see this description when deciding whether to grant permission. You determine what constitutes a significant update based on applicable regulations. For more information, see [`Age assurance frameworks Q&A`](https://developer.apple.comhttps://developer.apple.com/support/age-assurance/).

You can also use [`ageRatingCode`](https://developer.apple.com/documentation/storekit/appstore/ageratingcode) within StoreKit to determine if your app’s age rating changes on a person’s device. If it’s changed, use [`SignificantAppUpdateTopic`](https://developer.apple.com/documentation/permissionkit/significantappupdatetopic) to request consent from a parent or guardian for the child to continue using your app.

##### Monitor for Consent Withdrawal

Monitor for consent withdrawal by implementing [`App Store Server Notifications V2`](https://developer.apple.comhttps://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) to receive `RESCIND_CONSENT` [`notificationType`](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype) notifications. This notification type indicates that a parent or guardian has withdrawn consent for a child’s app usage. When you receive this notification, immediately restrict the child’s access to capabilities that require parental or guardian consent and update your app’s state accordingly.

Verify your implementation in the sandbox environment before deploying to production. The sandbox allows you to test various age range scenarios, including children under 13, ages 13-15, ages 16-17, and 18 and older, with different approval states and age declaration types. You can also simulate consent revocation by entering your app’s bundle ID to trigger a `RESCIND_CONSENT` notification to your server.

Access sandbox testing through Developer Mode settings on your device, or configure test scenarios in App Store Connect. For detailed setup instructions and a complete list of test cases with their corresponding API return values, see [`Testing age assurance in sandbox`](https://developer.apple.com/documentation/storekit/testing-age-assurance-in-sandbox).

## See Also

- [com.apple.developer.declared-age-range](../bundleresources/entitlements/com.apple.developer.declared-age-range.md)
  A Boolean value indicating whether your app may request a person’s age range.
- [Implementing age assurance and permissions](implementing-age-assurance-and-permissions.md)
  Create a significant change flow to inform people about important updates in your app and request age-related permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/requesting-people-share-their-age-range-with-your-app)*