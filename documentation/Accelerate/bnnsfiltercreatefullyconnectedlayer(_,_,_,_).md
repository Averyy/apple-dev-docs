# BNNSFilterCreateFullyConnectedLayer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a fully connected filter, initialized with input, output, layer, and filter parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerFullyConnected(_:_:))
- iPadOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerFullyConnected(_:_:))
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerFullyConnected(_:_:))
- macOS 10.12+ - Deprecated in 11.0 (renamed: BNNSFilterCreateLayerFullyConnected(_:_:))
- tvOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerFullyConnected(_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSFilterCreateLayerFullyConnected(_:_:))
- watchOS 3.0+ - Deprecated in 7.0 (renamed: BNNSFilterCreateLayerFullyConnected(_:_:))

> **Deprecated**: Use [`BNNSFilterCreateFullyConnectedLayer(_:_:_:_:)`](./bnnsfiltercreatefullyconnectedlayer%28_,_,_,_%29.md) instead.

## Declaration

```swift
func BNNSFilterCreateFullyConnectedLayer(_ in_desc: UnsafePointer<BNNSVectorDescriptor>, _ out_desc: UnsafePointer<BNNSVectorDescriptor>, _ layer_params: UnsafePointer<BNNSFullyConnectedLayerParameters>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

```c
BNNSFilterBNNSFilterCreateFullyConnectedLayer(const BNNSVectorDescriptor *in_desc, const BNNSVectorDescriptor *out_desc, const BNNSFullyConnectedLayerParameters *layer_params, const BNNSFilterParameters *filter_params);
```

## Return Value

A BNNSFilter object representing a fully connected filter configured with the specified  parameters

## Parameters

- `in_desc`: Pointer to a `BNNSVectorDescriptor` struct describing the input
- `out_desc`: Pointer to a `BNNSVectorDescriptor` struct describing the output
- `layer_params`: Pointer to a `BNNSFullyConnectedLayerParameters` struct describing the layer parameters
- `filter_params`: Pointer to a `BNNSFilterParameters` struct describing the filter parameters

## See Also

### Fully connected layers
- [struct BNNSFullyConnectedLayerParameters](./bnnsfullyconnectedlayerparameters.md)
  A structure containing fully connected layer parameters.
- [class FullyConnectedLayer](./bnns/fullyconnectedlayer.md)
  A layer object that wraps a fully connected filter and manages its deinitialization.
- [struct BNNSLayerParametersFullyConnected](./bnnslayerparametersfullyconnected.md)
  A structure that contains the parameters of a fully connected layer.
- [func BNNSFilterCreateLayerFullyConnected(UnsafePointer<BNNSLayerParametersFullyConnected>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerfullyconnected%28_,_%29.md)
  Returns a new fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatefullyconnectedlayer(_:_:_:_:))*