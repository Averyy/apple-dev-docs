# init(randomUniform:in:seed:scalarType:)

**Framework**: Coreml  
**Kind**: init

Creates a tensor with the specified shape, randomly sampling scalar values from a uniform distribution in `bounds`.

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
init<Scalar>(randomUniform shape: [Int], in bounds: ClosedRange<Scalar> = 0...1, seed: UInt64? = nil, scalarType: Scalar.Type = Scalar.self) where Scalar : MLTensorScalar, Scalar : BinaryInteger
```

#### Discussion

> **Note**: Using the same seed produces the same result only when dispatched to the same compute device.

## Parameters

- `shape`: The shape of the tensor.
- `bounds`: The bounds of the distribution. The default value is  .
- `seed`: The random seed.
- `scalarType`: The scalar type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(randomuniform:in:seed:scalartype:)-4ktle)*