# lowerBound

**Framework**: Declared Age Range  
**Kind**: property

The minimum age in the person’s declared age range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var lowerBound: Int?
```

#### Discussion

When this value is `nil`, the person’s age range is below the lowest age gate specified by the `requestAgeRange(ageGates:_:_:in:)` methods (for example, [`requestAgeRange(ageGates:_:_:in:)`](agerangeservice/requestagerange(agegates:_:_:in:)-2go8c.md)), indicating the person is under your minimum age requirement.

When present, the value of this property equals the highest age gate that the person’s declared age meets or exceeds, out of the age gates you supply to the method.

For example, if you specify age gates of `13`, `16`, and `18` and this property’s value is `16`, the person is at least 16 years old, but may or may not be 18 or older.

Consider this property together with [`upperBound`](agerangeservice/agerange/upperbound.md) to gate your app’s content based on the person’s declared age range.

## See Also

- [var upperBound: Int?](agerangeservice/agerange/upperbound.md)
  The maximum age in the person’s declared age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](agerangeservice/agerange/agerangedeclaration.md)
  Information about how the person set their age range.
- [var activeParentalControls: AgeRangeService.ParentalControls](agerangeservice/agerange/activeparentalcontrols.md)
  The parental controls that are active on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/lowerbound)*