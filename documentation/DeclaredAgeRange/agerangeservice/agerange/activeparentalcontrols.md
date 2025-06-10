# activeParentalControls

**Framework**: DeclaredAgeRange  
**Kind**: property

The parental controls turned on as a part of the response.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
var activeParentalControls: AgeRangeService.ParentalControls
```

#### Discussion

If empty, upper bound of age range is not below 18 or the person is under 18 with no parental controls enabled.

## See Also

- [var lowerBound: Int?](agerangeservice/agerange/lowerbound.md)
  The lower limit of the person’s age range.
- [var upperBound: Int?](agerangeservice/agerange/upperbound.md)
  The upper limit of the person’s age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](agerangeservice/agerange/agerangedeclaration.md)
  The sharer of the age range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/activeparentalcontrols)*