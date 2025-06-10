# init(function:alpha:beta:)

**Framework**: Accelerate  
**Kind**: init

Returns a new common activation function parameters structure that uses the specified function, alpha, and beta.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- visionOS ?+
- watchOS 3.0+
- Unknown ?+ - Deprecated
- tvOS 10.0+

## Declaration

```swift
init(function: BNNSActivationFunction, alpha: Float = .nan, beta: Float = .nan)
```

#### Return Value

A new common activation function parameters structure.

## Parameters

- `function`: The activation function to use.
- `alpha`: The parameter for the alpha of the activation function.
- `beta`: The parameter for the beta of the activation function.

## See Also

- [init()](bnnsactivation/init.md)
  Returns a new common activation function parameters structure.
- [init(function: BNNSActivationFunction, alpha: Float, beta: Float, iscale: Int32, ioffset: Int32, ishift: Int32, iscale_per_channel: UnsafePointer<Int32>?, ioffset_per_channel: UnsafePointer<Int32>?, ishift_per_channel: UnsafePointer<Int32>?)](bnnsactivation/init(function:alpha:beta:iscale:ioffset:ishift:iscale_per_channel:ioffset_per_channel:ishift_per_channel:).md)
  Returns a new common activation function parameters structure that uses the specified function, alpha, beta, integer scale, offset, and shift.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivation/init(function:alpha:beta:))*