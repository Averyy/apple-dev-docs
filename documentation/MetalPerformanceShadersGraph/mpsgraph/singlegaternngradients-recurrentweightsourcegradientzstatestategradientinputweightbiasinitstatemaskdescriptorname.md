# singleGateRNNGradients(_:recurrentWeight:sourceGradient:zState:stateGradient:inputWeight:bias:initState:mask:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a single-gate RNN gradient operation and returns the gradient tensor values.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func singleGateRNNGradients(_ source: MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, stateGradient: MPSGraphTensor?, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]
```

#### Return Value

A valid `MPSGraphTensor` array containing gradients for each input tensor, except for `sourceGradient` and `mask`. In case an input is `nil`, no gradient will be returned for it. The order of the gradients will be: for `source`, for `recurrentWeight`, for `inputWeight`, for `bias` and finally for `initState`.

#### Discussion

For details of this operation and parameters, refer to documentation of [`singleGateRNN(_:recurrentWeight:inputWeight:bias:initState:mask:descriptor:name:)`](mpsgraph/singlegaternn(_:recurrentweight:inputweight:bias:initstate:mask:descriptor:name:).md).

## Parameters

- `source`: A tensor that contains the source data   with the data layout [T,N,I].   In case   and   then the layout is [T,N,H] and   for   and   the layout is [T,N,2H].
- `recurrentWeight`: A tensor containing the recurrent weights  . For   the layout is [2,H,H] and otherwise it is [H,H].   Note: For   this tensor must have a static shape.
- `sourceGradient`: The input gradient, that is the gradient of a tensor with respect to the first output of the forward pass.
- `zState`: The second output of     with  .
- `stateGradient`: The input gradient coming from the future timestep - optional, if missing the operation assumes zeroes.
- `inputWeight`: A tensor containing the input weights matrix   - optional, if missing the operation assumes a diagonal unit-matrix.   For   the layout is [2H,I] and otherwise it is [H,I].
- `bias`: A tensor containing the bias   - optional, if missing the operation assumes zeroes. For   the layout is [2H] and otherwise it is [H].
- `initState`: The initial internal state of the RNN   - optional, if missing the operation assumes zeroes. For   the layout is [N,2H] and otherwise it is [N,H].
- `mask`: A tensor containing the mask   - optional, if missing the operation assumes ones. This is useful for dropout support.
- `descriptor`: A descriptor that defines the parameters for the RNN operation.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:stategradient:inputweight:bias:initstate:mask:descriptor:name:))*