# BNNSFilterCreateLayerLoss(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new loss layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSFilterCreateLayerLoss(_ layer_params: UnsafeRawPointer, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

You use a loss layer to compute forward and backward loss.

Forward loss can optionally also compute an optional loss gradient. For example, given the following predicted values in `input`, and ground truth values in `labels`:

```swift
let input: [Float]  = [9, 1, 6, 3, 4, 5, 6, 7, 8, 9]
let labels: [Float] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The following code computes the loss using [`BNNSLossFunctionMeanSquareError`](bnnslossfunctionmeansquareerror.md), reduced to a single value using [`BNNSLossReductionSum`](bnnslossreductionsum.md):

```swift
let n = input.count

var inDelta = [Float](repeating: .nan, count: n)
var output: [Float] = [ .nan ] // expected loss = (9 - 0)² + (6 - 2)² = 97

let flags = BNNSNDArrayFlags(0)

let inputDescriptor = BNNSNDArrayDescriptor(flags: flags,
                                            layout: BNNSDataLayoutVector,
                                            size: (n, 0, 0, 0, 0, 0, 0, 0),
                                            stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                            data: nil,
                                            data_type: .float,
                                            table_data: nil,
                                            table_data_type: .float,
                                            data_scale: 1,
                                            data_bias: 0)

let outputDescriptor = BNNSNDArrayDescriptor(flags: flags,
                                             layout: BNNSDataLayoutVector,
                                             size: (1, 0, 0, 0, 0, 0, 0, 0),
                                             stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                             data: nil,
                                             data_type: .float,
                                             table_data: nil,
                                             table_data_type: .float,
                                             data_scale: 1,
                                             data_bias: 0)

var lossParams = BNNSLayerParametersLossBase(function: BNNSLossFunctionMeanSquareError,
                                             i_desc: inputDescriptor,
                                             o_desc: outputDescriptor,
                                             reduction: BNNSLossReductionSum)

let lossLayer = BNNSFilterCreateLayerLoss(&lossParams, nil)

defer {
    BNNSFilterDestroy(lossLayer)
}

inDelta.withUnsafeMutableBufferPointer { inDeltaPtr in
    
    var inDeltaDescriptor = BNNSNDArrayDescriptor(flags: flags,
                                                  layout: BNNSDataLayoutVector,
                                                  size: (n, 0, 0, 0, 0, 0, 0, 0),
                                                  stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                  data: inDeltaPtr.baseAddress,
                                                  data_type: .float,
                                                  table_data: nil,
                                                  table_data_type: .float,
                                                  data_scale: 1,
                                                  data_bias: 0)

    BNNSLossFilterApplyBatch(lossLayer, 1,
                             input, n,
                             labels, n,
                             nil, 0,
                             &output,
                             &inDeltaDescriptor, n)
}
```

On return, `output` contains `(9 - 0)² + (6 - 2)² = 97`, and `inDelta` contains `[18.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`.

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

- [class LossLayer](bnns/losslayer.md)
  A layer object that wraps a loss filter and manages its deinitialization.
- [struct BNNSLossFunction](bnnslossfunction.md)
  Constants that describe loss functions.
- [struct BNNSLossReductionFunction](bnnslossreductionfunction.md)
  Constants that describe reduction functions used by a loss layer.
- [struct BNNSLayerParametersLossBase](bnnslayerparameterslossbase.md)
  A structure that contains the parameters of a loss layer.
- [struct BNNSLayerParametersLossHuber](bnnslayerparameterslosshuber.md)
  A structure that contains the parameters of a Huber loss layer.
- [struct BNNSLayerParametersLossSigmoidCrossEntropy](bnnslayerparameterslosssigmoidcrossentropy.md)
  A structure that contains the parameters of a sigmoid cross entropy loss layer.
- [struct BNNSLayerParametersLossSoftmaxCrossEntropy](bnnslayerparameterslosssoftmaxcrossentropy.md)
  A structure that contains the parameters of a softmax cross entropy loss layer.
- [struct BNNSLayerParametersLossYolo](bnnslayerparameterslossyolo.md)
  A structure that contains the parameters of a You Only Look Once (YOLO) loss layer.
- [func BNNSLossFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafeMutableRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int) -> Int32](bnnslossfilterapplybatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a loss filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSLossFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnslossfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a loss filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayerloss(_:_:))*