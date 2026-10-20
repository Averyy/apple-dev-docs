# function

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The activation function that the layer applies to its output.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var function: BNNSActivationFunction
```

```c
BNNSActivationFunction function;
```

## See Also

### Instance Properties
- [var alpha: Float](./alpha.md)
  The parameter for the alpha of the activation function.
- [var beta: Float](./beta.md)
  The parameter for the beta of the activation function.
- [var iscale: Int32](./iscale.md)
  Scale for integer functions.
- [var ioffset: Int32](./ioffset.md)
  Offset for integer functions.
- [var ishift: Int32](./ishift.md)
  Shift for integer functions.
- [var iscale_per_channel: UnsafePointer<Int32>?](./iscale_per_channel.md)
  Scale per channel for integer functions.
- [var ioffset_per_channel: UnsafePointer<Int32>?](./ioffset_per_channel.md)
  Offset per channel for integer functions.
- [var ishift_per_channel: UnsafePointer<Int32>?](./ishift_per_channel.md)
  Shift per channel for integer functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivation/function)*