# integerLinearSaturate(scale:offset:shift:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns an activation function that computes an arithmetic shift, preserving sign.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS
- watchOS 4.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
static func integerLinearSaturate(scale: Int32 = 1, offset: Int32 = 0, shift: Int32 = 0) -> BNNSActivation
```

## Parameters

- `scale`: The scale for the activation function.
- `offset`: The offset for the activation function.
- `shift`: The arithmetic shift for the activation function.

## See Also

### Related Documentation
- [BNNSActivationFunctionIntegerLinearSaturate](../bnnsactivationfunction/bnnsactivationfunctionintegerlinearsaturate.md)
  An activation function that returns an arithmetic shift, preserving sign.
### Type Methods
- [static func integerLinearSaturatePerChannel(scale: UnsafePointer<Int32>, offset: UnsafePointer<Int32>, shift: UnsafePointer<Int32>) -> BNNSActivation](./integerlinearsaturateperchannel%28scale,offset,shift%29.md)
  Returns an activation function that computes an arithmetic shift, preserving sign for each channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivation/integerlinearsaturate(scale:offset:shift:))*