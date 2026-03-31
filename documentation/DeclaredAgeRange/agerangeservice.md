# AgeRangeService

**Framework**: Declared Age Range  
**Kind**: struct

A request for the age range of a person logged onto the current device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct AgeRangeService
```

#### Overview

Use `AgeRangeService` to request a person’s age range and manage their access to content on your app. This service enables you to create age-appropriate experiences while respecting people’s privacy and meeting regulatory requirements. The system presents an interface that describes the data you’re requesting and asks people to grant permission to share their age range with your app.

The following code demonstrates how to request a person’s age range and determine what content to display on your app’s landing page based on their age group:

**SwiftUI**:

```swift
import SwiftUI
import DeclaredAgeRange

@Environment(\.requestAgeRange) var requestAgeRange

func checkAgeRange() async {
    guard let response = try? await requestAgeRange(ageGates: 13, 15, 18),
    case let .sharing(ageRange) = response else {
        return // Person declined sharing, or other error.
    }

    guard let lowerBound = ageRange.lowerBound else {
        // Person is under 13; enable age-appropriate experience.
        return
    }

    if lowerBound >= 18 {
        // Enable features for age 18 and older.
    } else if lowerBound >= 15 {
        // Enable features for ages 15-17.
    } else {
        // Enable features for ages 13-14.
    }
}
```

**UIKit and AppKit**:

```swift
// import UIKit for iOS and iPadOS.
// import AppKit for macOS.
import DeclaredAgeRange

func checkAgeRange() async {
    guard let response = try? await requestAgeRange(
        ageGates: 13, 15, 18,
        in: viewControllerOrWindow // Use UIViewController in UIKit or NSWindow in AppKit.
    ),
    case let .sharing(ageRange) = response else {
        return // Person declined sharing, or other error.
    }

    guard let lowerBound = ageRange.lowerBound else {
        // Person is under 13; enable age-appropriate experience.
        return
    }

    if lowerBound >= 18 {
        // Enable features for age 18 and older.
    } else if lowerBound >= 15 {
        // Enable features for ages 15-17.
    } else {
        // Enable features for ages 13-14.
    }
}
```

The system may override your age gates based on the local regulations of the person’s geographic location. Age ranges provide the minimum information necessary for content decisions while protecting privacy. Parental controls and family sharing settings may affect the availability and accuracy of age information.

## Topics

### Retrieving the shared instance
- [static let shared: AgeRangeService](agerangeservice/shared.md)
  The singleton app instance for accessing age range services.
### Getting the age range
- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  Constants that describe how an adult, parent, or guardian set the age range.
- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  Information about a person’s age range based on their response to your age range request.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Requests an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating whether a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.
### Accessing regulatory features
- [var isEligibleForAgeFeatures: Bool](agerangeservice/iseligibleforagefeatures.md)
  A Boolean value that indicates whether an adult, teen, or child is eligible for age-gated features.
### Defining regulatory features
- [AgeRangeService.RegulatoryFeature](agerangeservice/regulatoryfeature.md)
  Defines the regulatory features that your app may need to support.
- [var requiredRegulatoryFeatures: Set<AgeRangeService.RegulatoryFeature>](agerangeservice/requiredregulatoryfeatures.md)
  A set of regulatory features that are required for the person.
### Displaying update acknowledgments
- [func showSignificantUpdateAcknowledgment(in: UIWindowScene, updateDescription: String) async throws](agerangeservice/showsignificantupdateacknowledgment(in:updatedescription:).md)
  Displays a system-provided interface for people to acknowledge a significant app update.
### Handling errors
- [AgeRangeService.Error](agerangeservice/error.md)
  An error that occurs when an age range request fails.

## See Also

- [struct DeclaredAgeRangeAction](declaredagerangeaction.md)
  An action that requests a person’s age range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice)*