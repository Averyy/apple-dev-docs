# activeParentalControls

**Framework**: Declared Age Range  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

It’s important to note that the minimum age of legal adulthood varies depending on the region associated with someone’s Apple account.  If [`activeParentalControls`](./activeparentalcontrols.md) is empty, either the device doesn’t have parental controls enabled as part of the response or a person’s age doesn’t fall into the reporting range for the specific region.

## See Also

### Fetching the age range
- [var lowerBound: Int?](./lowerbound.md)
  The minimum age in the person’s declared age range.
- [var upperBound: Int?](./upperbound.md)
  The maximum age in the person’s declared age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](./agerangedeclaration.md)
  Information about how the person set their age range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/activeparentalcontrols)*