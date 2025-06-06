# BNNS.PaddingLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a padding filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
class PaddingLayer
```

## Topics

### Creating a Padding Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, mode: BNNS.PaddingMode, size: [(x: Int, y: Int)], filterParameters: BNNSFilterParameters?)](bnns/paddinglayer/init(input:output:mode:size:filterparameters:).md)
  Returns a new padding layer.
### Specifying the Padding Mode
- [BNNS.PaddingMode](bnns/paddingmode.md)
  Constants that define padding modes.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](bnns/unarylayer.md)

## See Also

- [struct BNNSPaddingMode](bnnspaddingmode.md)
  Constants that define padding modes.
- [struct BNNSLayerParametersPadding](bnnslayerparameterspadding.md)
  A structure that contains the parameters of a padding layer.
- [func BNNSFilterCreateLayerPadding(UnsafePointer<BNNSLayerParametersPadding>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerpadding(_:_:).md)
  Returns a new loss layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/paddinglayer)*