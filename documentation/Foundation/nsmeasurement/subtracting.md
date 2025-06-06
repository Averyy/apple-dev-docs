# subtracting(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new measurement by subtracting the specified measurement from the receiver.

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
func subtracting(_ measurement: Measurement<Unit>) -> Measurement<Unit>
```

#### Return Value

A new measurement with a value equal to the receiver’s value minus the value of the specified measurement converted into the unit of the receiver.

#### Discussion

This method raises an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) if the receiver cannot be converted to unit.

You can use the [`canBeConverted(to:)`](nsmeasurement/canbeconverted(to:).md) method, passing the unit of the specified measurement, to determine whether a measurement can be converted to a particular unit before calling this method.

## Parameters

- `measurement`: The measurement to be subtracted.

## See Also

- [func adding(Measurement<Unit>) -> Measurement<Unit>](nsmeasurement/adding(_:).md)
  Returns a new measurement by adding the receiver to the specified measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmeasurement/subtracting(_:))*