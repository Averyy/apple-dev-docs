# BNNS.DropoutLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps a dropout filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
class DropoutLayer
```

## Topics

### Creating a Dropout Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, rate: Float, seed: UInt32, control: UInt8, filterParameters: BNNSFilterParameters?)](./dropoutlayer/init%28input,output,rate,seed,control,filterparameters%29.md)
  Returns a new dropout layer.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](./unarylayer.md)

## See Also

### Dropout layers
- [struct BNNSLayerParametersDropout](../bnnslayerparametersdropout.md)
  A structure that contains the parameters of a dropout layer.
- [func BNNSFilterCreateLayerDropout(UnsafePointer<BNNSLayerParametersDropout>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatelayerdropout%28_,_%29.md)
  Returns a new dropout layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/dropoutlayer)*