# BNNSFilterCreateFullyConnectedLayer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a fully connected filter, initialized with input, output, layer, and filter parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func BNNSFilterCreateFullyConnectedLayer(_ in_desc: UnsafePointer<BNNSVectorDescriptor>, _ out_desc: UnsafePointer<BNNSVectorDescriptor>, _ layer_params: UnsafePointer<BNNSFullyConnectedLayerParameters>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Return Value

A BNNSFilter object representing a fully connected filter configured with the specified  parameters

## Parameters

- `in_desc`: Pointer to a   struct describing the input
- `out_desc`: Pointer to a   struct describing the output
- `layer_params`: Pointer to a   struct describing the layer parameters
- `filter_params`: Pointer to a   struct describing the filter parameters

## See Also

- [struct BNNSFullyConnectedLayerParameters](bnnsfullyconnectedlayerparameters.md)
  A structure containing fully connected layer parameters.
- [class FullyConnectedLayer](bnns/fullyconnectedlayer.md)
  A layer object that wraps a fully connected filter and manages its deinitialization.
- [struct BNNSLayerParametersFullyConnected](bnnslayerparametersfullyconnected.md)
  A structure that contains the parameters of a fully connected layer.
- [func BNNSFilterCreateLayerFullyConnected(UnsafePointer<BNNSLayerParametersFullyConnected>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerfullyconnected(_:_:).md)
  Returns a new fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatefullyconnectedlayer(_:_:_:_:))*