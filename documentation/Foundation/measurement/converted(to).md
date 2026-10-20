# converted(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new measurement created by converting to the specified unit.

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
func converted(to otherUnit: UnitType) -> Measurement<UnitType>
```

Available when `UnitType` inherits `Dimension`.

#### Return Value

A converted measurement.

## Parameters

- `otherUnit`: A unit of the same `Dimension`.

## See Also

### Converting to Other Units
- [func convert(to: UnitType)](./convert%28to%29.md)
  Converts the measurement to the specified unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/converted(to:))*