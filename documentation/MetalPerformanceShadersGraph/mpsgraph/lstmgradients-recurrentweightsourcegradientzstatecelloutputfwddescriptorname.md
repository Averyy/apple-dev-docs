# LSTMGradients(_:recurrentWeight:sourceGradient:zState:cellOutputFwd:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates an LSTM gradient operation and returns the gradient tensor values.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func LSTMGradients(_ source: MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]
```

#### Return Value

A valid `MPSGraphTensor` array containing gradients for each input tensor, except for `sourceGradient` and `mask`. In case an input is nil, no gradient will be returned for it. The order of the gradients will be: for `source`, for `recurrentWeight`, for `inputWeight`, for `bias`, for `initState` and for `initCell`.

#### Discussion

For details of this operation and parameters, refer to documentation of [`LSTM(_:recurrentWeight:inputWeight:bias:initState:initCell:mask:peephole:descriptor:name:)`](mpsgraph/lstm(_:recurrentweight:inputweight:bias:initstate:initcell:mask:peephole:descriptor:name:).md).

## Parameters

- `source`: A tensor containing the source data    with the data layout [T,N,I]. In case   and   then the layout is [T,N,4H] and for   and   the layout is [T,N,8H].
- `recurrentWeight`: A tensor containing the recurrent weights  . For   the layout is [2,4H,H] and otherwise it is [4H,H].
- `sourceGradient`: The input gradient, that is the gradient of a tensor with respect to the first output of the forward pass.
- `zState`: The third output of     with  .
- `cellOutputFwd`: The second output of     with   or  .
- `descriptor`: A descriptor that defines the parameters for the LSTM operation.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:descriptor:name:))*