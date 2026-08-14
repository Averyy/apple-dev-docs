# Implementing age assurance and permissions

**Framework**: Declared Age Range

Create a significant change flow to inform people about important updates in your app and request age-related permissions.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+
- Xcode 27.0+ (Beta)

#### Overview

When you introduce significant changes that affect how people interact with your app, you may be required to inform people about those changes. In certain regions, you’re also required to obtain parental approval before minors can continue using your app. For more information on complying with age assurance laws and related requirements, refer to [`Design safe and age‑appropriate experiences for your apps and games`](https://developer.apple.comhttps://developer.apple.com/kids/).

This sample app demonstrates how to implement a significant change flow using [`Declared Age Range`](DeclaredAgeRange.md), [`PermissionKit`](https://developer.apple.com/documentation/permissionkit), and [`iCloud key-value storage`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesigningForKey-ValueDataIniCloud.html).

#### Configure the Sample Code Project

To configure the sample code project, do the following in Xcode:

1. Select the sample target, then click the Signing & Capabilities tab.
2. In the Bundle Identifier text field, change the bundle ID to your own app’s bundle ID.
3. Add the Declared Age Range capability. Xcode adds the [`com.apple.developer.declared-age-range`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.declared-age-range) entitlement to the sample target.
4. Add the iCloud capability, then enable the “Key-value storage” service. Xcode adds the [`iCloud Key-Value Store Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.ubiquity-kvstore-identifier) to the sample target. For more information, refer to [`Configuring iCloud services`](https://developer.apple.com/documentation/xcode/configuring-icloud-services).
5. Configure the sample target to use your team for signing. For more information, refer to [`Preparing your app for distribution`](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution).

After configuring the project, sign in to iCloud on a device with iOS 26.4 or later, then build and run the sample in Xcode.

> **Note**: To test this sample in the sandbox environment, create a [`Sandbox Apple Account`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-a-sandbox-apple-account/), then follow the steps in [`Testing age assurance in sandbox`](https://developer.apple.com/documentation/storekit/testing-age-assurance-in-sandbox).

#### Detect Regulatory Requirements

Before showing the significant change flow, the sample app checks whether the person is in a region that requires age assurance. `ComplianceManager` calls `AgeRangeService.shared.requiredRegulatoryFeatures` and inspects the returned set to determine which requirements apply:

```swift
regulatoryFeatures = try await AgeRangeService.shared.requiredRegulatoryFeatures
isComplianceRequired = !regulatoryFeatures.isEmpty
```

If the set contains [`AgeRangeService.RegulatoryFeature.significantAppChangeRequiresParentalConsent`](agerangeservice/regulatoryfeature/significantappchangerequiresparentalconsent.md), the app requests parental approval for minors. If it contains [`AgeRangeService.RegulatoryFeature.significantAppChangeRequiresAdultNotification`](agerangeservice/regulatoryfeature/significantappchangerequiresadultnotification.md), the app prompts verified adults to acknowledge the changes. When neither feature is present, the app skips the flow entirely.

#### Request the Persons Age Range

When the sample app requires compliance, `SignificantChangeView` calls the `requestAgeRange()` environment action to present a system dialog asking the person to share their age range. The app passes an age gate of 18 to distinguish minors from adults:

```swift
let response = try await requestAgeRange(ageGates: ageOfMajority)
let result = AgeRangeResult.from(response)
```

`AgeRangeResult.from(_:)` parses the response into one of four categories:

- **`.minor`**: The person’s upper age bound is below 18.
- **`.verifiedAdult`**: The person is an adult with a confirmed payment method.
- **`.unverifiedAdult`**: The person is an adult without account verification.
- **`.declinedSharing`**: The person declined to share their age range.

#### Handle the Significant Change Flow

The sample app routes each age-range result through a different path.

**Minor:** When the person is a minor, the app creates a [`PermissionQuestion`](https://developer.apple.com/documentation/permissionkit/permissionquestion) describing the changes and presents `RequestParentalApprovalView`.

```swift
case .minor(let ageRange):
    formattedAgeRange = ageRange
    guard complianceManager.requiresParentalConsent else {
        versionManager.handlePendingChanges()
        dismiss()
        return
    }
    let topic = SignificantAppUpdateTopic(description: versionManager.changesDescription)
    parentalQuestion = PermissionQuestion(significantAppUpdateTopic: topic)
```

**Verified adult:** When the person is a verified adult in a jurisdiction requiring adult notification, the app calls `presentSignificantChanges()`, which uses the `showSignificantUpdateAcknowledgment()` environment action to present the system acknowledgment dialog. After the person acknowledges the changes, the app marks all pending changes as handled.

```swift
case .verifiedAdult(let ageRange):
    formattedAgeRange = ageRange
    guard complianceManager.requiresAdultNotification else {
        versionManager.handlePendingChanges()
        dismiss()
        return
    }
    presentSignificantChanges()
```

**Unverified adult:** When the person is an adult without a verified account, the app sets the phase to `.blocked` and prevents access until the person verifies their account in Settings.

```swift
case .unverifiedAdult:
    phase = .blocked
```

#### Request Parental Approval and Track Acknowledged Changes

`RequestParentalApprovalView` uses a [`PermissionButton`](https://developer.apple.com/documentation/permissionkit/permissionbutton) to send the `PermissionQuestion` to the parent or guardian’s device. The sample app entry point listens for the parent’s response using `AskCenter.shared.responses(for:)`. When the parent approves the request, the app marks all significant changes as handled. When the parent denies the request, the app prevents the minor from using it:

```swift
for await response in AskCenter.shared.responses(for: SignificantAppUpdateTopic.self) {
    guard response.choice.answer == .approval else {
        return
    }
    versionManager.handleAllChanges()
}
```

`SignificantChangeVersion` tracks which changes each person has acknowledged using [`NSUbiquitousKeyValueStore`](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore). When the person acknowledges a change, the app writes it to iCloud so other devices don’t present the same flow again:

```swift
for change in changes {
    handledChanges.insert(change)
    if !ubiquitousStore.bool(forKey: change.id) {
        ubiquitousStore.set(true, forKey: change.id)
    }
}
ubiquitousStore.synchronize()
```

The app also listens for changes arriving from other devices by observing [`didChangeExternallyNotification`](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/didchangeexternallynotification) and syncing the local set of handled changes.

People who install the app when a significant change is already present don’t need to acknowledge it. `SignificantChangeVersion` uses the [`originalAppVersion`](https://developer.apple.com/documentation/storekit/apptransaction/originalappversion) property of [`AppTransaction`](https://developer.apple.com/documentation/storekit/apptransaction) to retrieve the version the person originally installed, then automatically marks any changes the app introduced at or before that version as handled:

```swift
if change.introducedInVersion.compare(originalAppVersion, options: .numeric) != .orderedDescending {
    pendingChanges.insert(change)
}
```

## See Also

- [com.apple.developer.declared-age-range](../bundleresources/entitlements/com.apple.developer.declared-age-range.md)
  A Boolean value indicating whether your app may request a person’s age range.
- [Requesting people’s age range information in your app](requesting-people-share-their-age-range-with-your-app.md)
  Ask people to share their age range with your app, and tailor features for adults, teens, and children while preserving privacy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/implementing-age-assurance-and-permissions)*