# ioffset_per_channel

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

Offset per channel for integer functions.

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
var ioffset_per_channel: UnsafePointer<Int32>?
```

```c
const int32_t * ioffset_per_channel;
```

## See Also

### Instance Properties
- [var function: BNNSActivationFunction](./function.md)
  The activation function that the layer applies to its output.
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
- [var ishift_per_channel: UnsafePointer<Int32>?](./ishift_per_channel.md)
  Shift per channel for integer functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivation/ioffset_per_channel)*