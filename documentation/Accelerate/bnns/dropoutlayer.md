# BNNS.DropoutLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a dropout filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- tvOS 14.0+

## Declaration

```swift
class DropoutLayer
```

## Topics

### Creating a Dropout Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, rate: Float, seed: UInt32, control: UInt8, filterParameters: BNNSFilterParameters?)](bnns/dropoutlayer/init(input:output:rate:seed:control:filterparameters:).md)
  Returns a new dropout layer.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](bnns/unarylayer.md)

## See Also

- [struct BNNSLayerParametersDropout](bnnslayerparametersdropout.md)
  A structure that contains the parameters of a dropout layer.
- [func BNNSFilterCreateLayerDropout(UnsafePointer<BNNSLayerParametersDropout>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerdropout(_:_:).md)
  Returns a new dropout layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/dropoutlayer)*