# BNNSLayerParametersActivation

**Framework**: Accelerate  
**Kind**: struct

A set of parameters that define an activation layer.

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
struct BNNSLayerParametersActivation
```

#### Overview

Use an activation layer to perform type conversion. The following code shows how to convert 16-bit integer values to single-precision values:

```swift
let input: [Int16] = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var output = [Float](repeating: 0, count: input.count)

input.withUnsafeBufferPointer { inputPtr in
    output.withUnsafeMutableBufferPointer { outputPtr in
        
        let inputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                    layout: BNNSDataLayoutVector,
                                                    size: (input.count, 0, 0, 0, 0, 0, 0, 0),
                                                    stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                    data: UnsafeMutableRawPointer(mutating: inputPtr.baseAddress),
                                                    data_type: .int16,
                                                    table_data: nil,
                                                    table_data_type: .int16,
                                                    data_scale: 1,
                                                    data_bias: 0)
        
        let ouputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                    layout: BNNSDataLayoutVector,
                                                    size: (input.count, 0, 0, 0, 0, 0, 0, 0),
                                                    stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                    data: outputPtr.baseAddress,
                                                    data_type: .float,
                                                    table_data: nil,
                                                    table_data_type: .float,
                                                    data_scale: 1,
                                                    data_bias: 0)
        
        var layerParameters = BNNSLayerParametersActivation(i_desc: inputDescriptor,
                                                                 o_desc: ouputDescriptor,
                                                                 activation: .identity,
                                                                 axis_flags: 0)
        
        BNNSDirectApplyActivationBatch(&layerParameters,
                                       nil,
                                       1,
                                       input.count,
                                       input.count)
    }
}

// Prints "[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]"
print(output)
```

## Topics

### Initializers
- [init()](bnnslayerparametersactivation/init.md)
  Returns a new activation layer parameters structure.
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, activation: BNNSActivation, axis_flags: UInt32)](bnnslayerparametersactivation/init(i_desc:o_desc:activation:axis_flags:).md)
  Returns a new activation layer parameters structure from the supplied descriptors, activation function, and axis flags.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersactivation/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersactivation/o_desc.md)
  The descriptor of the output.
- [var activation: BNNSActivation](bnnslayerparametersactivation/activation.md)
  The activation function that the layer applies to the output.
- [var axis_flags: UInt32](bnnslayerparametersactivation/axis_flags.md)
  Flags that indicate axes on which to apply certain activation functions.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSFilterCreateVectorActivationLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatevectoractivationlayer(_:_:_:_:).md)
- [class ActivationLayer](bnns/activationlayer.md)
  A layer object that wraps an activation filter and manages its deinitialization.
- [struct BNNSActivationFunction](bnnsactivationfunction.md)
  Constants that describe activation functions.
- [struct BNNSActivation](bnnsactivation.md)
  A set of parameters that describe common activation functions.
- [func BNNSFilterCreateLayerActivation(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayeractivation(_:_:).md)
  Returns a new activation layer.
- [func BNNSDirectApplyActivationBatch(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](bnnsdirectapplyactivationbatch(_:_:_:_:_:).md)
  Applies an activation filter to a set of input objects, writing out the result to a set of output objects.
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:axes:input:output:batchsize:filterparameters:).md)
  Applies an activation function on the specified axes.
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:input:output:batchsize:filterparameters:).md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersactivation)*