# ageRangeDeclaration

**Framework**: Declared Age Range  
**Kind**: property  
**Role**: Instance Property

Information about how the person set their age range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?
```

#### Discussion

This property provides context about the reliability and source of the age information. Use this information to determine the appropriate level of content restriction required for your app’s features.

For more information about declaration types, refer to [`AgeRangeService.AgeRangeDeclaration`](../agerangedeclaration.md).

## See Also

### Fetching the age range
- [var lowerBound: Int?](./lowerbound.md)
  The minimum age in the person’s declared age range.
- [var upperBound: Int?](./upperbound.md)
  The maximum age in the person’s declared age range.
- [var activeParentalControls: AgeRangeService.ParentalControls](./activeparentalcontrols.md)
  The parental controls that are active on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/agerangedeclaration)*