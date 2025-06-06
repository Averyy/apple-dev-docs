# BNNSActivation

**Framework**: Accelerate  
**Kind**: struct

A set of parameters that describe common activation functions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSActivation
```

## Topics

### Initializers
- [init()](bnnsactivation/init.md)
  Returns a new common activation function parameters structure.
- [init(function: BNNSActivationFunction, alpha: Float, beta: Float)](bnnsactivation/init(function:alpha:beta:).md)
  Returns a new common activation function parameters structure that uses the specified function, alpha, and beta.
- [init(function: BNNSActivationFunction, alpha: Float, beta: Float, iscale: Int32, ioffset: Int32, ishift: Int32, iscale_per_channel: UnsafePointer<Int32>?, ioffset_per_channel: UnsafePointer<Int32>?, ishift_per_channel: UnsafePointer<Int32>?)](bnnsactivation/init(function:alpha:beta:iscale:ioffset:ishift:iscale_per_channel:ioffset_per_channel:ishift_per_channel:).md)
  Returns a new common activation function parameters structure that uses the specified function, alpha, beta, integer scale, offset, and shift.
### Instance Properties
- [var function: BNNSActivationFunction](bnnsactivation/function.md)
  The activation function that the layer applies to its output.
- [var alpha: Float](bnnsactivation/alpha.md)
  The parameter for the alpha of the activation function.
- [var beta: Float](bnnsactivation/beta.md)
  The parameter for the beta of the activation function.
- [var iscale: Int32](bnnsactivation/iscale.md)
  Scale for integer functions.
- [var ioffset: Int32](bnnsactivation/ioffset.md)
  Offset for integer functions.
- [var ishift: Int32](bnnsactivation/ishift.md)
  Shift for integer functions.
- [var iscale_per_channel: UnsafePointer<Int32>?](bnnsactivation/iscale_per_channel.md)
  Scale per channel for integer functions.
- [var ioffset_per_channel: UnsafePointer<Int32>?](bnnsactivation/ioffset_per_channel.md)
  Offset per channel for integer functions.
- [var ishift_per_channel: UnsafePointer<Int32>?](bnnsactivation/ishift_per_channel.md)
  Shift per channel for integer functions.
### Type Methods
- [static func integerLinearSaturate(scale: Int32, offset: Int32, shift: Int32) -> BNNSActivation](bnnsactivation/integerlinearsaturate(scale:offset:shift:).md)
  Returns an activation function that computes an arithmetic shift, preserving sign.
- [static func integerLinearSaturatePerChannel(scale: UnsafePointer<Int32>, offset: UnsafePointer<Int32>, shift: UnsafePointer<Int32>) -> BNNSActivation](bnnsactivation/integerlinearsaturateperchannel(scale:offset:shift:).md)
  Returns an activation function that computes an arithmetic shift, preserving sign for each channel.
### Type Properties
- [static var identity: BNNSActivation](bnnsactivation/identity.md)
  Identity activation function.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSFilterCreateVectorActivationLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatevectoractivationlayer(_:_:_:_:).md)
- [class ActivationLayer](bnns/activationlayer.md)
  A layer object that wraps an activation filter and manages its deinitialization.
- [struct BNNSActivationFunction](bnnsactivationfunction.md)
  Constants that describe activation functions.
- [struct BNNSLayerParametersActivation](bnnslayerparametersactivation.md)
  A set of parameters that define an activation layer.
- [func BNNSFilterCreateLayerActivation(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayeractivation(_:_:).md)
  Returns a new activation layer.
- [func BNNSDirectApplyActivationBatch(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](bnnsdirectapplyactivationbatch(_:_:_:_:_:).md)
  Applies an activation filter to a set of input objects, writing out the result to a set of output objects.
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:axes:input:output:batchsize:filterparameters:).md)
  Applies an activation function on the specified axes.
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:input:output:batchsize:filterparameters:).md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivation)*