# axis

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The index of the axis on which the function applies scale and bias.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
var axis: Int?
```

#### Discussion

Set to `nil` to dequantize the entire tensor using scale and bias.

## See Also

### Inspecting the Properties of a Fused Dequantization Parameters Structure
- [var scale: BNNSNDArrayDescriptor?](./scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor?](./bias.md)
  The descriptor of the bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fuseddequantizationparameters/axis)*