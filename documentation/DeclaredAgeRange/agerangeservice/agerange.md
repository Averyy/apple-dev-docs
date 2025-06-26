# AgeRangeService.AgeRange

**Framework**: Declared Age Range  
**Kind**: struct

A person’s age range is based on the age they provided in response to the age range request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
struct AgeRange
```

#### Overview

For more information, refer to [`requestAgeRange(ageGates:_:_:in:)`](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)

## Topics

### Fetching the age range
- [var lowerBound: Int?](agerangeservice/agerange/lowerbound.md)
  The lower limit of the person’s age range.
- [var upperBound: Int?](agerangeservice/agerange/upperbound.md)
  The upper limit of the person’s age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](agerangeservice/agerange/agerangedeclaration.md)
  The sharer of the age range.
- [var activeParentalControls: AgeRangeService.ParentalControls](agerangeservice/agerange/activeparentalcontrols.md)
  The parental controls turned on as a part of the response.

## See Also

- [AgeRangeService.AgeRangeDeclaration](agerangeservice/agerangedeclaration.md)
  An enumeration that describes the declared age range.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: UIViewController) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)
  Determines an age range for the person logged onto iCloud on the device.
- [func requestAgeRange(ageGates: Int, Int?, Int?, in: NSWindow) async throws -> AgeRangeService.Response](agerangeservice/requestagerange(agegates:_:_:in:)-4yo3r.md)
  Determines an age range for the person logged onto iCloud on the device.
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating either a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange)*