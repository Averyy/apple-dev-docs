# convert(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Converts the measurement to the specified unit.

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
mutating func convert(to otherUnit: UnitType)
```

Available when `UnitType` inherits `Dimension`.

## Parameters

- `otherUnit`: A unit of the same `Dimension`.

## See Also

### Converting to Other Units
- [func converted(to: UnitType) -> Measurement<UnitType>](./converted%28to%29.md)
  Returns a new measurement created by converting to the specified unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/convert(to:))*