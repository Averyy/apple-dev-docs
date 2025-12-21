# string(from:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a localized string representation of the provided measurement.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func string<UnitType>(from measurement: Measurement<UnitType>) -> String where UnitType : Unit
```

#### Return Value

A user-readable string that represents the measurement.

## Parameters

- `measurement`: The measurement to be represented.

## See Also

- [func string(from: Measurement<Unit>) -> String](measurementformatter/string(from:)-wt9y.md)
  Creates and returns a localized string representation of the provided measurement.
- [func string(from: Unit) -> String](measurementformatter/string(from:)-4hwjz.md)
  Creates and returns a localized string representation of the provided unit of measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter/string(from:)-6rcb1)*