# activeParentalControls

**Framework**: Declared Age Range  
**Kind**: property

The parental controls that are active on the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var activeParentalControls: AgeRangeService.ParentalControls
```

#### Discussion

It’s important to note that the minimum age of legal adulthood varies depending on the region associated with someone’s Apple account.  If [`activeParentalControls`](agerangeservice/agerange/activeparentalcontrols.md) is empty, either the device doesn’t have parental controls enabled as part of the response or a person’s age doesn’t fall into the reporting range for the specific region.

## See Also

- [var lowerBound: Int?](agerangeservice/agerange/lowerbound.md)
  The minimum age in the person’s declared age range.
- [var upperBound: Int?](agerangeservice/agerange/upperbound.md)
  The maximum age in the person’s declared age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](agerangeservice/agerange/agerangedeclaration.md)
  Information about how the person set their age range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/activeparentalcontrols)*