# avoid

**Framework**: EnergyKit  
**Kind**: property

A category for electricity usage during periods that the framework suggests a person avoid.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst ?+
- macOS 26.1+

## Declaration

```swift
var avoid: Measure?
```

#### Discussion

The framework might put electricity usage in this category when:

- Grid operators ask electricity consumers to temporarily reduce their power usage during periods of high demand or grid stress, also known as a  event.
- Fossil fuel plants predominantly power the grid, composing the least desirable times for energy consumption from an environmental perspective.

> ❗ **Important**: The framework reserves this property for future use.

## See Also

- [var cleaner: Measure?](electricityinsightrecord/gridcleanliness/cleaner.md)
  A category for electricity usage during the cleanest grid periods.
- [var lessClean: Measure?](electricityinsightrecord/gridcleanliness/lessclean.md)
  A category for electricity usage during less-clean grid periods.
- [var unknown: Measure?](electricityinsightrecord/gridcleanliness/unknown.md)
  A category of electricity usage when grid cleanliness information is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/gridcleanliness/avoid)*