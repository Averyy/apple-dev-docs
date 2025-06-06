# fastFourierTransform(_:axes:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a fast Fourier transform operation and returns the result tensor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func fastFourierTransform(_ tensor: MPSGraphTensor, axes: [NSNumber], descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid complex-valued MPSGraphTensor of the same shape as `tensor`.

#### Discussion

This operation computes the fast Fourier transform of the input tensor according to the following formulae.

```md
    output[mu] = scale * sum_nu exp( +/- i * 2Pi * mu * nu / n ) input[nu], where
```

`scale = 1` for `scaling_mode = none`, `scale = 1/V_f` for `scaling_mode = size`, `scale = 1/sqrt(V_f)` for `scaling_mode = unitary`, where `V_f` is the volume of the transformation defined by the dimensions included in `axes` (`V_f = prod_{i \in axes} shape(input)[i]`) (see [`scalingMode`](mpsgraphfftdescriptor/scalingmode.md)), `+` is selected in `+/-` when `inverse` is specified, otherwise `-` is used and the sum is done separately over each dimension in `axes` and `n` is the dimension length of that axis.

> 💡 **Tip**: Currently MPSGraph supports the transformation only within the last four dimensions of the input tensor. In case you need to transform higher dimensions than the last four, you can tranpose the higher dimensions of the input with [`transpose(_:permutation:name:)`](mpsgraph/transpose(_:permutation:name:).md)  to be within that last four and then transpose the result tensor back with the inverse of the input transpose.

Currently MPSGraph supports the transformation only within the last four dimensions of the input tensor. In case you need to transform higher dimensions than the last four, you can tranpose the higher dimensions of the input with [`transpose(_:permutation:name:)`](mpsgraph/transpose(_:permutation:name:).md)  to be within that last four and then transpose the result tensor back with the inverse of the input transpose.

## Parameters

- `tensor`: A complex or real-valued input tensor.
- `axes`: An array of numbers that specifies over which axes MPSGraph performs the Fourier transform - all axes must be contained within last four dimensions of the input tensor.
- `descriptor`: A descriptor that defines the parameters of the Fourier transform operation - see  .
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/fastfouriertransform(_:axes:descriptor:name:))*