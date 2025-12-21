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

Use `AgeRangeService` to request a person’s age range and manage their access to content on your app.

This service enables you to create age-range restricted experiences while respecting people’s privacy and meeting regulatory requirements. The system presents a standardized interface that people can use to share their age information with your app, and you receive the information necessary to make content decisions.

The following code demonstrates how to request a person’s age range and determine what content to display on your app’s landing page based on their age group:

```swift
do {
   let response = try await AgeRangeService.shared.requestAgeRange(ageGates: 13, 15, 18)
   guard let lowerBound = response.lowerBound else {
       // Allow access to under 13 features.
       return
   }
   if lowerBound >= 18 {
      // Allow access to 18+ features.
   } else if lowerBound >= 15 {
       // Allow access to 15+ features.
   } else if lowerBound >= 13 {
       // Allow access to 13+ features.
   }
} catch AgeRangeService.Error.notAvailable {
   // No age range provided.
   return
}
```

The system may override your age-range restrictions based on regulations and the person’s geographic location. Age ranges are designed to provide the minimum information necessary for content decisions while protecting privacy. Parental controls and family sharing settings may affect the availability and accuracy of age information.

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
### Handling errors
- [AgeRangeService.Error](agerangeservice/error.md)
  An error that occurs when an age range request fails.
### Instance Properties
- [var isEligibleForAgeFeatures: Bool](agerangeservice/iseligibleforagefeatures.md)
  A boolean value that indicates whether an adult, teen, or child is eligible for age gated features.

## See Also

- [struct DeclaredAgeRangeAction](declaredagerangeaction.md)
  An action that requests a person’s declared age range with automatic UI context management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice)*