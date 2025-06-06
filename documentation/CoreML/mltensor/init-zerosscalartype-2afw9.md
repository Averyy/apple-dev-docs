# init(zeros:scalarType:)

**Framework**: Core ML  
**Kind**: init

Creates a tensor with all scalars set to zero.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init<Scalar>(zeros shape: [Int], scalarType: Scalar.Type = Scalar.self) where Scalar : MLTensorScalar, Scalar : BinaryFloatingPoint, Scalar.RawSignificand : FixedWidthInteger
```

## Parameters

- `shape`: The shape of the tensor.
- `scalarType`: The scalar type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(zeros:scalartype:)-2afw9)*