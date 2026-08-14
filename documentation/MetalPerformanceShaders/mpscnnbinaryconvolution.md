# MPSCNNBinaryConvolution

**Framework**: Metal Performance Shaders  
**Kind**: class

A convolution kernel with binary weights and an input image using binary approximations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBinaryConvolution
```

#### Overview

The [`MPSCNNBinaryConvolution`](mpscnnbinaryconvolution.md) optionally first binarizes the input image and then convolves the result with a set of binary-valued filters, each producing one feature map in the output image (which is a normal image).

The output is computed as follows:

![out[i, x, y, c] = ( sum_{dx,dy,f} in[i,x+dx, y+dy, f] x B[c,dx,dy,f] ) * scale[c] * beta[i,x,y] + bias[c]](/images/com.apple.metalperformanceshaders/media-2903520@2x.png)

where the *sum over* *dx,dy* is over the spatial filter kernel window defined by [`kernelWidth`](mpscnnconvolutiondescriptor/kernelwidth.md) and [`kernelHeight`](mpscnnconvolutiondescriptor/kernelheight.md), *sum over* *f* is over the input feature channel indices within group, *B* contains the binary weights, interpreted as `{-1, 1}` or `{0, 1}` and *scale[c]* is the `outputScaleTerms` array and bias is the `outputBiasTerms` array. Above *i* is the image index in batch the sum over input channels *f* runs through the group indices. The convolution operator ⊗ is defined by [`MPSCNNBinaryConvolutionType`](mpscnnbinaryconvolutiontype.md) passed in at initialization time of the filter:

- **[`MPSCNNBinaryConvolutionType.binaryWeights`](mpscnnbinaryconvolutiontype/binaryweights.md)**: The input image is not binarized at all and the convolution is computed interpreting the weights as `[0, 1] -> {-1, 1}` with the given scaling terms.
- **[`MPSCNNBinaryConvolutionType.XNOR`](mpscnnbinaryconvolutiontype/xnor.md)**: The convolution is computed by first binarizing the input image using the sign function `bin(x) = x < 0 ? -1 : 1` and the convolution multiplication is done with the XNOR-operator:

`!(x ^ y) = delta_xy = { (x == y) ? 1 : 0 }`

and scaled according to the optional scaling operations.

Note that we output the values of the bitwise convolutions to interval `{-1, 1}`, which means that the output of the XNOR-operator is scaled implicitly as follows:

`r = 2 * ( !(x ^ y) ) - 1 = { -1, 1 }`

This means that for a dot-product of two 32-bit words the result is:

`r = 2 * popcount(!(x ^ y) ) - 32 = 32 - 2 * popcount( x ^ y ) = { -32, -30, ..., 30, 32 }`

- **[`MPSCNNBinaryConvolutionType.AND`](mpscnnbinaryconvolutiontype/and.md)**: The convolution is computed by first binarizing the input image using the sign function `bin(x) = x < 0 ? -1 : 1` and the convolution multiplication is done with the AND-operator:

`(x & y) = delta_xy * delta_x1 = { (x == y == 1) ? 1 : 0 }`

and scaled according to the optional scaling operations.

Note that we output the values of the AND-operation is assumed to lie in `{0, 1}` interval and hence no more implicit scaling takes place.

This means that for a dot-product of two 32-bit words the result is:

`r = popcount(x & y) = { 0, ..., 31, 32 }`

The input data can be pre-offset and scaled by providing the `inputBiasTerms` and `inputScaleTerms` parameters for the initialization functions and this can be used for example to accomplish batch normalization of the data. The scaling of input values happens before possible beta-image computation.

The parameter `beta` above is an optional image which is used to compute scaling factors for each spatial position and image index. For the XNOR-Net based networks this is computed as follows:

![beta[i,x,y] = sum_{dx,dy} A[i, x+dx, y+dy] / (kx * ky)](/images/com.apple.metalperformanceshaders/media-2903518@2x.png)

where *(dx,dy)* are summed over the convolution filter window.

![[ -kx/2, (kx-1)/2], [ -ky/2, (ky-1)/2 ] and A[i,x,y] = sum_{c} abs( in[i,x,y,c] ) / Nc](/images/com.apple.metalperformanceshaders/media-2903519@2x.png)

where *in* is the original input image (in full precision) and *Nc* is the number of input channels in the input image. Parameter `beta` is not passed as input and to enable beta-scaling the user can provide [`MPSCNNBinaryConvolutionFlags.useBetaScaling`](mpscnnbinaryconvolutionflags/usebetascaling.md) in the flags parameter in the initialization functions.

Finally the normal activation neuron is applied and the result is written to the output image.

> **Note**:  [`MPSCNNBinaryConvolution`](mpscnnbinaryconvolution.md) does not currently support [`groups`](mpscnnconvolutiondescriptor/groups.md) greater than 1.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnbinaryconvolution/init(coder:device:).md)
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/init(device:convolutiondata:outputbiasterms:outputscaleterms:inputbiasterms:inputscaleterms:type:flags:).md)
  Initializes a binary convolution kernel.
- [convenience init(device: any MTLDevice, convolutionData: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](mpscnnbinaryconvolution/init(device:convolutiondata:scalevalue:type:flags:).md)
  Initializes a binary convolution kernel.
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [enum MPSCNNBinaryConvolutionType](mpscnnbinaryconvolutiontype.md)
  Options that defines what operations are used to perform binary convolution.
- [enum MPSCNNBinaryConvolutionFlags](mpscnnbinaryconvolutionflags.md)
  Options used to control binary convolution kernels.
### Instance Properties
- [var inputFeatureChannels: Int](mpscnnbinaryconvolution/inputfeaturechannels.md)
- [var outputFeatureChannels: Int](mpscnnbinaryconvolution/outputfeaturechannels.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Inherited By
- [MPSCNNBinaryFullyConnected](mpscnnbinaryfullyconnected.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MPSCNNConvolution](mpscnnconvolution.md)
  A convolution kernel that convolves the input image with a set of filters, with each producing one feature map in the output image.
- [class MPSCNNDepthWiseConvolutionDescriptor](mpscnndepthwiseconvolutiondescriptor.md)
  A description of a convolution object that does depthwise convolution.
- [class MPSCNNSubPixelConvolutionDescriptor](mpscnnsubpixelconvolutiondescriptor.md)
  A description of a convolution object that does subpixel upsampling and reshaping.
- [class MPSCNNConvolutionTranspose](mpscnnconvolutiontranspose.md)
  A transposed convolution kernel.
- [class MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
  A gradient convolution kernel.
- [class MPSCNNConvolutionGradientState](mpscnnconvolutiongradientstate.md)
  An object that exposes a gradient convolution kernel’s gradient with respect to weights and biases.
- [protocol MPSImageSizeEncodingState](mpsimagesizeencodingstate.md)
  A protocol for objects that contain information about an image size elsewhere in the graph.
- [class MPSCNNConvolutionWeightsAndBiasesState](mpscnnconvolutionweightsandbiasesstate.md)
  A class that stores weights and biases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryconvolution)*