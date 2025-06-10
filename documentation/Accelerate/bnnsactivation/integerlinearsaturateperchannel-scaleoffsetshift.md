# integerLinearSaturatePerChannel(scale:offset:shift:)

**Framework**: Accelerate  
**Kind**: method

Returns an activation function that computes an arithmetic shift, preserving sign for each channel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+
- watchOS 4.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
static func integerLinearSaturatePerChannel(scale: UnsafePointer<Int32>, offset: UnsafePointer<Int32>, shift: UnsafePointer<Int32>) -> BNNSActivation
```

## Parameters

- `scale`: The scale for the activation function.
- `offset`: The offset for the activation function.
- `shift`: The arithmetic shift for the activation function.

## See Also

- [BNNSActivationFunctionIntegerLinearSaturatePerChannel](bnnsactivationfunction/bnnsactivationfunctionintegerlinearsaturateperchannel.md)
  An activation function that returns an arithmetic shift, preserving sign for each channel.
- [static func integerLinearSaturate(scale: Int32, offset: Int32, shift: Int32) -> BNNSActivation](bnnsactivation/integerlinearsaturate(scale:offset:shift:).md)
  Returns an activation function that computes an arithmetic shift, preserving sign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivation/integerlinearsaturateperchannel(scale:offset:shift:))*