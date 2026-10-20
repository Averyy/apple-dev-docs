# BNNS.FullyConnectedLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps a fully connected filter and manages its deinitialization.

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
class FullyConnectedLayer
```

## Topics

### Creating a Fully Connected Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?, activation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters?)](./fullyconnectedlayer/init%28input,output,weights,bias,activation,filterparameters%29.md)
  Returns a new fully connected layer.
### Type Methods
- [static func sparsify(batchSize: Int, inputLayout: BNNS.SparseLayout, inputDenseShape: BNNSNDArrayDescriptor, inputValues: BNNSNDArrayDescriptor, output: inout BNNSNDArrayDescriptor, sparseParameters: BNNS.SparseParameters?, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](./fullyconnectedlayer/sparsify%28batchsize,inputlayout,inputdenseshape,inputvalues,output,sparseparameters,workspace,filterparameters%29.md)
  Converts a sparse tensor from a standardized sparse layout to a device-specific sparse layout that Fully Connected uses.

## Relationships

### Inherits From
- [BNNS.ConvolutionLayer](./convolutionlayer.md)

## See Also

### Fully connected layers
- [struct BNNSFullyConnectedLayerParameters](../bnnsfullyconnectedlayerparameters.md)
  A structure containing fully connected layer parameters.
- [func BNNSFilterCreateFullyConnectedLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSFullyConnectedLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatefullyconnectedlayer%28_,_,_,_%29.md)
  Returns a fully connected filter, initialized with input, output, layer, and filter parameters.
- [struct BNNSLayerParametersFullyConnected](../bnnslayerparametersfullyconnected.md)
  A structure that contains the parameters of a fully connected layer.
- [func BNNSFilterCreateLayerFullyConnected(UnsafePointer<BNNSLayerParametersFullyConnected>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatelayerfullyconnected%28_,_%29.md)
  Returns a new fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fullyconnectedlayer)*