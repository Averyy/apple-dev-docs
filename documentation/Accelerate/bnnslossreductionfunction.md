# BNNSLossReductionFunction

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe reduction functions used by a loss layer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSLossReductionFunction
```

```c
typedef enum { ... } BNNSLossReductionFunction;
```

## Topics

### Reduction Functions
- [var rawValue: UInt32](./bnnslossreductionfunction/rawvalue.md)
- [init(UInt32)](./bnnslossreductionfunction/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnslossreductionfunction/init%28rawvalue%29.md)
- [var BNNSLossReductionMean: BNNSLossReductionFunction](./bnnslossreductionmean.md)
  Sums the loss of all samples in the batch and divides by the number of samples.
- [var BNNSLossReductionNonZeroWeightMean: BNNSLossReductionFunction](./bnnslossreductionnonzeroweightmean.md)
  Sums the loss of all samples in the batch and divides by the number of non-zero weights.
- [var BNNSLossReductionSum: BNNSLossReductionFunction](./bnnslossreductionsum.md)
  Sums the loss of all samples in the batch.
- [var BNNSLossReductionWeightedMean: BNNSLossReductionFunction](./bnnslossreductionweightedmean.md)
  Sums the loss of all samples in the batch and divides by the sum of all weights.
- [var BNNSLossReductionNone: BNNSLossReductionFunction](./bnnslossreductionnone.md)
  Returns the loss without any reduction.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Loss layers
- [class LossLayer](./bnns/losslayer.md)
  A layer object that wraps a loss filter and manages its deinitialization.
- [struct BNNSLossFunction](./bnnslossfunction.md)
  Constants that describe loss functions.
- [struct BNNSLayerParametersLossBase](./bnnslayerparameterslossbase.md)
  A structure that contains the parameters of a loss layer.
- [struct BNNSLayerParametersLossHuber](./bnnslayerparameterslosshuber.md)
  A structure that contains the parameters of a Huber loss layer.
- [struct BNNSLayerParametersLossSigmoidCrossEntropy](./bnnslayerparameterslosssigmoidcrossentropy.md)
  A structure that contains the parameters of a sigmoid cross entropy loss layer.
- [struct BNNSLayerParametersLossSoftmaxCrossEntropy](./bnnslayerparameterslosssoftmaxcrossentropy.md)
  A structure that contains the parameters of a softmax cross entropy loss layer.
- [struct BNNSLayerParametersLossYolo](./bnnslayerparameterslossyolo.md)
  A structure that contains the parameters of a You Only Look Once (YOLO) loss layer.
- [func BNNSFilterCreateLayerLoss(UnsafeRawPointer, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerloss%28_,_%29.md)
  Returns a new loss layer.
- [func BNNSLossFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafeMutableRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int) -> Int32](./bnnslossfilterapplybatch%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a loss filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSLossFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](./bnnslossfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a loss filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslossreductionfunction)*