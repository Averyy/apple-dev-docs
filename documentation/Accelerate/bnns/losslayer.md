# BNNS.LossLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps a loss filter and manages its deinitialization.

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
class LossLayer
```

## Topics

### Creating a Loss Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, lossFunction: BNNS.LossFunction, lossReduction: BNNS.LossReduction, filterParameters: BNNSFilterParameters?)](./losslayer/init%28input,output,lossfunction,lossreduction,filterparameters%29.md)
  Returns a new loss layer.
### Specifying a Loss Function
- [BNNS.LossFunction](./lossfunction.md)
  Constants that describe loss functions.
### Specifying a Loss Reduction Function
- [BNNS.LossReduction](./lossreduction.md)
  An enumeration that describes loss reduction functions.
### Applying a Loss Layer
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, labels: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](./losslayer/apply%28batchsize,input,labels,output,generatinginputgradient%29.md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
### Instance Methods
- [func apply(batchSize: Int, input: BNNSNDArrayDescriptor, labels: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, broadcastsWeights: Bool, generatingInputGradient: BNNSNDArrayDescriptor) throws](./losslayer/apply%28batchsize,input,labels,output,weights,broadcastsweights,generatinginputgradient%29.md)

## Relationships

### Inherits From
- [BNNS.Layer](./layer.md)

## See Also

### Loss layers
- [struct BNNSLossFunction](../bnnslossfunction.md)
  Constants that describe loss functions.
- [struct BNNSLossReductionFunction](../bnnslossreductionfunction.md)
  Constants that describe reduction functions used by a loss layer.
- [struct BNNSLayerParametersLossBase](../bnnslayerparameterslossbase.md)
  A structure that contains the parameters of a loss layer.
- [struct BNNSLayerParametersLossHuber](../bnnslayerparameterslosshuber.md)
  A structure that contains the parameters of a Huber loss layer.
- [struct BNNSLayerParametersLossSigmoidCrossEntropy](../bnnslayerparameterslosssigmoidcrossentropy.md)
  A structure that contains the parameters of a sigmoid cross entropy loss layer.
- [struct BNNSLayerParametersLossSoftmaxCrossEntropy](../bnnslayerparameterslosssoftmaxcrossentropy.md)
  A structure that contains the parameters of a softmax cross entropy loss layer.
- [struct BNNSLayerParametersLossYolo](../bnnslayerparameterslossyolo.md)
  A structure that contains the parameters of a You Only Look Once (YOLO) loss layer.
- [func BNNSFilterCreateLayerLoss(UnsafeRawPointer, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatelayerloss%28_,_%29.md)
  Returns a new loss layer.
- [func BNNSLossFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafeMutableRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int) -> Int32](../bnnslossfilterapplybatch%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a loss filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSLossFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](../bnnslossfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a loss filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/losslayer)*