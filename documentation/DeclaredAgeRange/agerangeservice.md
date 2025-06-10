# AgeRangeService

**Framework**: DeclaredAgeRange  
**Kind**: struct

A request for the age range of a person logged onto the current device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
struct AgeRangeService
```

#### Overview

Use `AgeRangeService` to request a person’s age range and manage their access to content on your app. The code snippet below describes how to request a person’s age range and determine what content to display on your app’s landing page.

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

## Topics

### Retrieving the shared instance
- [static let shared: AgeRangeService](agerangeservice/shared.md)
  The singleton app instance.
### Getting the age range
- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  An enumeration that describes the declared age range.
- [AgeRangeService.AgeRange](agerangeservice/agerange.md)
  A person’s age range is based on the information they provided in response to the age range request.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating either a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.
### Handling errors
- [AgeRangeService.Error](agerangeservice/error.md)
  An error that occurs when an age range request fails.
### Instance Methods
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Determines an age range for the person logged onto the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Determines an age range for the person using the device.

## See Also

- [struct DeclaredAgeRangeAction](declaredagerangeaction.md)
  Provides an action to request a person’s declared age range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice)*