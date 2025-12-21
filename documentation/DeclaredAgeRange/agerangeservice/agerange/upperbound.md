# upperBound

**Framework**: Declared Age Range  
**Kind**: property

The maximum age in the person’s declared age range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var upperBound: Int?
```

#### Discussion

When this value is `nil`, there’s no upper bound to the person’s age range, indicating they meet or exceed your highest `ageGate`. When present, this value represents the highest `ageGate` the person is confirmed to be under.

Use with `lowerBound` to provide age range boundaries for content decision making.

## See Also

- [var lowerBound: Int?](agerangeservice/agerange/lowerbound.md)
  The minimum age in the person’s declared age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](agerangeservice/agerange/agerangedeclaration.md)
  Information about how the person set their age range.
- [var activeParentalControls: AgeRangeService.ParentalControls](agerangeservice/agerange/activeparentalcontrols.md)
  The parental controls that are active on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/upperbound)*