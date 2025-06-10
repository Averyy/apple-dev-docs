# BNNS.FullyConnectedLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a fully connected filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
class FullyConnectedLayer
```

## Topics

### Creating a Fully Connected Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?, activation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters?)](bnns/fullyconnectedlayer/init(input:output:weights:bias:activation:filterparameters:).md)
  Returns a new fully connected layer.
### Type Methods
- [static func sparsify(batchSize: Int, inputLayout: BNNS.SparseLayout, inputDenseShape: BNNSNDArrayDescriptor, inputValues: BNNSNDArrayDescriptor, output: inout BNNSNDArrayDescriptor, sparseParameters: BNNS.SparseParameters?, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](bnns/fullyconnectedlayer/sparsify(batchsize:inputlayout:inputdenseshape:inputvalues:output:sparseparameters:workspace:filterparameters:).md)
  Converts a sparse tensor from a standardized sparse layout to a device-specific sparse layout that Fully Connected uses.

## Relationships

### Inherits From
- [BNNS.ConvolutionLayer](bnns/convolutionlayer.md)

## See Also

- [struct BNNSFullyConnectedLayerParameters](bnnsfullyconnectedlayerparameters.md)
  A structure containing fully connected layer parameters.
- [func BNNSFilterCreateFullyConnectedLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSFullyConnectedLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatefullyconnectedlayer(_:_:_:_:).md)
  Returns a fully connected filter, initialized with input, output, layer, and filter parameters.
- [struct BNNSLayerParametersFullyConnected](bnnslayerparametersfullyconnected.md)
  A structure that contains the parameters of a fully connected layer.
- [func BNNSFilterCreateLayerFullyConnected(UnsafePointer<BNNSLayerParametersFullyConnected>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerfullyconnected(_:_:).md)
  Returns a new fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fullyconnectedlayer)*