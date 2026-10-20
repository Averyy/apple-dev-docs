# init()

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new common activation function parameters structure.

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
init()
```

## See Also

### Initializers
- [init(function: BNNSActivationFunction, alpha: Float, beta: Float)](./init%28function,alpha,beta%29.md)
  Returns a new common activation function parameters structure that uses the specified function, alpha, and beta.
- [init(function: BNNSActivationFunction, alpha: Float, beta: Float, iscale: Int32, ioffset: Int32, ishift: Int32, iscale_per_channel: UnsafePointer<Int32>?, ioffset_per_channel: UnsafePointer<Int32>?, ishift_per_channel: UnsafePointer<Int32>?)](./init%28function,alpha,beta,iscale,ioffset,ishift,iscale_per_channel,ioffset_per_channel,ishift_per_channel%29.md)
  Returns a new common activation function parameters structure that uses the specified function, alpha, beta, integer scale, offset, and shift.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivation/init())*