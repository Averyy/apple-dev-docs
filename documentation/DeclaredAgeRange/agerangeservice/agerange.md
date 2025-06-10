# AgeRangeService.AgeRange

**Framework**: DeclaredAgeRange  
**Kind**: struct

A person’s age range is based on the information they provided in response to the age range request.

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

For more information, refer to `requestAgeRange(ageGates:_:_:in:)`

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
- [AgeRangeService.Response](agerangeservice/response.md)
  A response indicating either a person shared their age range or declined to share it.
- [AgeRangeService.ParentalControls](agerangeservice/parentalcontrols.md)
  An option set to define parental controls enabled and shared as a part of age range declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange)*