# cleaner

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

A category for electricity usage during the cleanest grid periods.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst

## Declaration

```swift
var cleaner: Measure?
```

## Discussion

This category represents electricity usage when the electrical grid uses its cleanest available energy sources, which might include renewable energy such as solar, wind, or hydroelectric, or cleaner fossil fuel sources such as natural gas instead of coal.

## See Also

### Getting grid cleanliness information
- [var lessClean: Measure?](./lessclean.md)
  A category for electricity usage during less-clean grid periods.
- [var avoid: Measure?](./avoid.md)
  A category for electricity usage during periods that the framework suggests a person avoid.
- [var unknown: Measure?](./unknown.md)
  A category of electricity usage when grid cleanliness information is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/gridcleanliness/cleaner)*