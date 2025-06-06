# converting(to:)

**Framework**: Foundation  
**Kind**: method

Returns a measurement created by converting the receiver to the specified unit.

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
func converting(to unit: Unit) -> Measurement<Unit>
```

#### Return Value

A new measurement with a value calculated by converting into the new unit.

#### Discussion

This method raises an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) if the receiver cannot be converted to unit.

## Parameters

- `unit`: The unit to convert the measurement into.

## See Also

- [func canBeConverted(to: Unit) -> Bool](nsmeasurement/canbeconverted(to:).md)
  Indicates whether the measurement can be converted to the given unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmeasurement/converting(to:))*