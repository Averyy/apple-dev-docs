# axis

**Framework**: Accelerate  
**Kind**: property

The index of the axis on which the function applies scale and bias.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- tvOS 15.0+

## Declaration

```swift
var axis: Int?
```

#### Discussion

Set to `nil` to dequantize the entire tensor using scale and bias.

## See Also

- [var scale: BNNSNDArrayDescriptor?](bnns/fuseddequantizationparameters/scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor?](bnns/fuseddequantizationparameters/bias.md)
  The descriptor of the bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fuseddequantizationparameters/axis)*