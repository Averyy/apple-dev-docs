# GRUGradients(_:recurrentWeight:sourceGradient:zState:outputFwd:stateGradient:inputWeight:bias:initState:mask:secondaryBias:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a GRU gradient operation and returns the gradient tensor values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func GRUGradients(_ source: MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, outputFwd: MPSGraphTensor, stateGradient: MPSGraphTensor?, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, secondaryBias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]
```

#### Return Value

A valid `MPSGraphTensor` array containing gradients for each input tensor, except for `sourceGradient` and `mask`. In case an input is nil, no gradient will be returned for it. The order of the gradients will be: for `source`, for `recurrentWeight`, for `inputWeight`, for `bias`, for `initState` and for `secondaryBias`.

#### Discussion

For details of this operation and parameters, refer to documentation of [`GRU(_:recurrentWeight:inputWeight:bias:initState:mask:secondaryBias:descriptor:name:)`](mpsgraph/gru(_:recurrentweight:inputweight:bias:initstate:mask:secondarybias:descriptor:name:).md).

## Parameters

- `source`: A tensor containing the source data   with the data layout [T,N,I]. In case   and   then the layout is [T,N,3H] and for   and   the layout is [T,N,6H].
- `recurrentWeight`: A tensor containing the recurrent weights  . For   the layout is [2,3H,H] and otherwise it is [3H,H].
- `sourceGradient`: The input gradient, that is the gradient of a tensor with respect to the first output of the forward pass.
- `zState`: The second output of     with   .
- `outputFwd`: The first output of     with  .
- `stateGradient`: The input gradient for state coming from the future timestep - optional, if missing the operation assumes zeroes.
- `inputWeight`: A tensor containing the input weights matrix   - optional, if missing the operation assumes a diagonal unit-matrix.   For   the layout is [6H,I] and otherwise it is [3H,I].
- `bias`: A tensor containing the bias   - optional, if missing the operation assumes zeroes. For   the layout is [6H] and otherwise it is [3H].
- `initState`: The initial internal state of the LSTM   - optional, if missing the operation assumes zeroes. For   the layout is [N,2H] and otherwise it is [N,H].
- `mask`: A tensor containing the mask   - optional, if missing the operation assumes ones. Useful for dropout.
- `secondaryBias`: A tensor containing the secondary bias vector   - optional, if missing the operation assumes zeroes. Only used with  . Shape is [H], ie. a vector for each gate, or [2H] for bidirectional.
- `descriptor`: A descriptor that defines the parameters for the GRU operation.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/grugradients(_:recurrentweight:sourcegradient:zstate:outputfwd:stategradient:inputweight:bias:initstate:mask:secondarybias:descriptor:name:))*