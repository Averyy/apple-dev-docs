# MLCLayer

**Framework**: ML Compute  
**Kind**: class

The base class for all framework layers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCLayer
```

#### Overview

This class defines a polymorphic interface for `MLCLayer` subclasses. There are subclasses for each supported neural network layer type. Use the appropriate subclass initializer to create a layer object.

## Topics

### Inspecting a Layer
- [var layerID: Int](mlclayer/layerid.md)
  A unique number that identifies each layer.
- [var label: String](mlclayer/label.md)
  A string that helps identify this layer.
- [var isDebuggingEnabled: Bool](mlclayer/isdebuggingenabled.md)
  A Boolean that indicates whether you choose to debug the layer when executing a graph that includes it.
- [var deviceType: MLCDeviceType](mlclayer/devicetype.md)
  A device type that indicates where the system executes the layer.
- [class func supportsDataType(MLCDataType, on: MLCDevice) -> Bool](mlclayer/supportsdatatype(_:on:).md)
  Returns a Boolean that indicates whether instances of this layer accept source tensors for the data type and device that you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MLCActivationLayer](mlcactivationlayer.md)
- [MLCArithmeticLayer](mlcarithmeticlayer.md)
- [MLCBatchNormalizationLayer](mlcbatchnormalizationlayer.md)
- [MLCComparisonLayer](mlccomparisonlayer.md)
- [MLCConcatenationLayer](mlcconcatenationlayer.md)
- [MLCConvolutionLayer](mlcconvolutionlayer.md)
- [MLCDropoutLayer](mlcdropoutlayer.md)
- [MLCEmbeddingLayer](mlcembeddinglayer.md)
- [MLCFullyConnectedLayer](mlcfullyconnectedlayer.md)
- [MLCGatherLayer](mlcgatherlayer.md)
- [MLCGramMatrixLayer](mlcgrammatrixlayer.md)
- [MLCGroupNormalizationLayer](mlcgroupnormalizationlayer.md)
- [MLCInstanceNormalizationLayer](mlcinstancenormalizationlayer.md)
- [MLCLSTMLayer](mlclstmlayer.md)
- [MLCLayerNormalizationLayer](mlclayernormalizationlayer.md)
- [MLCLossLayer](mlclosslayer.md)
- [MLCMatMulLayer](mlcmatmullayer.md)
- [MLCMultiheadAttentionLayer](mlcmultiheadattentionlayer.md)
- [MLCPaddingLayer](mlcpaddinglayer.md)
- [MLCPoolingLayer](mlcpoolinglayer.md)
- [MLCReductionLayer](mlcreductionlayer.md)
- [MLCReshapeLayer](mlcreshapelayer.md)
- [MLCScatterLayer](mlcscatterlayer.md)
- [MLCSelectionLayer](mlcselectionlayer.md)
- [MLCSliceLayer](mlcslicelayer.md)
- [MLCSoftmaxLayer](mlcsoftmaxlayer.md)
- [MLCSplitLayer](mlcsplitlayer.md)
- [MLCTransposeLayer](mlctransposelayer.md)
- [MLCUpsampleLayer](mlcupsamplelayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayer)*