# AgeRangeService.AgeRange

**Framework**: Declared Age Range  
**Kind**: struct

Information about a person’s age range based on their response to your age range request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct AgeRange
```

#### Overview

This provides the minimum information necessary for you to make content decisions while protecting the person’s privacy. Rather than receiving an exact age, you receive age range bounds that correspond to your specified age gates.

For more information about requesting age ranges, refer to `requestAgeRange(ageGates:_:_:in:)`.

## Topics

### Fetching the age range
- [var lowerBound: Int?](agerangeservice/agerange/lowerbound.md)
  The minimum age in the person’s declared age range.
- [var upperBound: Int?](agerangeservice/agerange/upperbound.md)
  The maximum age in the person’s declared age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](agerangeservice/agerange/agerangedeclaration.md)
  Information about how the person set their age range.
- [var activeParentalControls: AgeRangeService.ParentalControls](agerangeservice/agerange/activeparentalcontrols.md)
  The parental controls that are active on the device.

## See Also

- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  Constants that describe how an adult, parent, or guardian set the age range.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Requests an age range for the person signed in to iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Requests an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating whether a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange)*