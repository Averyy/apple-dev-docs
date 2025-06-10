# ElectricityInsightRecord.GridCleanliness

**Framework**: EnergyKit  
**Kind**: struct

A struct that describes the cleanliness of the grid’s energy or duration data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
struct GridCleanliness
```

## Topics

### Initializing the grid data
- [init(clean: Measure?, reduce: Measure?, avoid: Measure?, unknown: Measure?)](electricityinsightrecord/gridcleanliness/init(clean:reduce:avoid:unknown:).md)
  Creates an instance of the grid cleanliness data.
### Getting the grid cleanliness information
- [var avoid: Measure?](electricityinsightrecord/gridcleanliness/avoid.md)
  The duration of energy or runtime data that can’t be reduced.
- [var clean: Measure?](electricityinsightrecord/gridcleanliness/clean.md)
  The duration of energy or runtime data that’s cleaner.
- [var reduce: Measure?](electricityinsightrecord/gridcleanliness/reduce.md)
  The duration of energy or runtime data that can be reduced.
- [var unknown: Measure?](electricityinsightrecord/gridcleanliness/unknown.md)
  The unknown duration of energy or runtime data.

## See Also

- [var dataByGridCleanliness: ElectricityInsightRecord<Measure>.GridCleanliness?](electricityinsightrecord/databygridcleanliness.md)
  The electrical energy consumed or generated, or the runtime duration broken down by levels of cleanliness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/gridcleanliness)*