# upperBound

**Framework**: Declared Age Range  
**Kind**: property  
**Role**: Instance Property

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

When this value is `nil`, there’s no upper bound to the person’s age range, indicating they meet or exceed the highest age gate specified by the `requestAgeRange(ageGates:_:_:in:)` methods (for example, [`requestAgeRange(ageGates:_:_:in:)`](../requestagerange%28agegates,_,_,in%29-2go8c.md)).

When present, the value of this property equals the highest age gate that exceeds the person’s declared age, out of the age gates you supply to the method.

Consider this property together with [`lowerBound`](./lowerbound.md) to gate your app’s content based on the person’s declared age range.

## See Also

### Fetching the age range
- [var lowerBound: Int?](./lowerbound.md)
  The minimum age in the person’s declared age range.
- [var ageRangeDeclaration: AgeRangeService.AgeRangeDeclaration?](./agerangedeclaration.md)
  Information about how the person set their age range.
- [var activeParentalControls: AgeRangeService.ParentalControls](./activeparentalcontrols.md)
  The parental controls that are active on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerange/upperbound)*