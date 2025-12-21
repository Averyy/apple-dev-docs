# lessClean

**Framework**: EnergyKit  
**Kind**: property

A category for electricity usage during less-clean grid periods.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst ?+
- macOS 26.1+

## Declaration

```swift
var lessClean: Measure?
```

#### Discussion

This category represents electricity usage during periods when the electrical grid uses more fossil fuel energy sources, making it less environmentally friendly than the cleanest periods.

## See Also

- [var cleaner: Measure?](electricityinsightrecord/gridcleanliness/cleaner.md)
  A category for electricity usage during the cleanest grid periods.
- [var avoid: Measure?](electricityinsightrecord/gridcleanliness/avoid.md)
  A category for electricity usage during periods that the framework suggests a person avoid.
- [var unknown: Measure?](electricityinsightrecord/gridcleanliness/unknown.md)
  A category of electricity usage when grid cleanliness information is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/gridcleanliness/lessclean)*