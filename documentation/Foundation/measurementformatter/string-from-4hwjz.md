# string(from:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a localized string representation of the provided unit of measure.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func string(from unit: Unit) -> String
```

#### Return Value

A user-readable string that represents the unit of measure. If the unit cannot be localized, the unit’s [`symbol`](unit/symbol.md) value is used.

## Parameters

- `unit`: The unit of measure to be represented.

## See Also

- [func string(from: Measurement<Unit>) -> String](measurementformatter/string(from:)-wt9y.md)
  Creates and returns a localized string representation of the provided measurement.
- [func string<UnitType>(from: Measurement<UnitType>) -> String](measurementformatter/string(from:)-6rcb1.md)
  Creates and returns a localized string representation of the provided measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurementformatter/string(from:)-4hwjz)*