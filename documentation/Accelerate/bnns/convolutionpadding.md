# BNNS.ConvolutionPadding

**Framework**: Accelerate  
**Kind**: enum

Constants that describe convolution padding modes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
enum ConvolutionPadding
```

## Topics

### Convolution Padding Modes
- [case asymmetric(left: Int, right: Int, up: Int, down: Int)](bnns/convolutionpadding/asymmetric(left:right:up:down:).md)
  A padding mode that supports individual padding values for each side.
- [BNNS.ConvolutionPadding.symmetric(x:y:)](bnns/convolutionpadding/symmetric(x:y:).md)
  A padding mode that provides symmetric padding.
### Special Values
- [static var zero: BNNS.ConvolutionPadding](bnns/convolutionpadding/zero.md)
  A padding mode with zero padding on all sides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/convolutionpadding)*