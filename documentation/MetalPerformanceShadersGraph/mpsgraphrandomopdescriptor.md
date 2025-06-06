# MPSGraphRandomOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

A class that describes the random operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphRandomOpDescriptor
```

## Topics

### Initializers
- [convenience init?(distribution: MPSGraphRandomDistribution, dataType: MPSDataType)](mpsgraphrandomopdescriptor/init(distribution:datatype:).md)
  Class method to initialize a distribution descriptor.
### Instance Properties
- [var dataType: MPSDataType](mpsgraphrandomopdescriptor/datatype.md)
  The data type of the generated result values.
- [var distribution: MPSGraphRandomDistribution](mpsgraphrandomopdescriptor/distribution.md)
  The type of distribution to draw samples from. See MPSGraphRandomDistribution.
- [var max: Float](mpsgraphrandomopdescriptor/max.md)
  The upper range of the distribution.
- [var maxInteger: Int](mpsgraphrandomopdescriptor/maxinteger.md)
  The upper range of the distribution.
- [var mean: Float](mpsgraphrandomopdescriptor/mean.md)
  The mean of the distribution.
- [var min: Float](mpsgraphrandomopdescriptor/min.md)
  The lower range of the distribution.
- [var minInteger: Int](mpsgraphrandomopdescriptor/mininteger.md)
  The lower range of the distribution.
- [var samplingMethod: MPSGraphRandomNormalSamplingMethod](mpsgraphrandomopdescriptor/samplingmethod.md)
  The sampling method of the distribution.
- [var standardDeviation: Float](mpsgraphrandomopdescriptor/standarddeviation.md)
  The standard deviation of the distribution.

## Relationships

### Inherits From
- [MPSGraphObject](mpsgraphobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSGraph](mpsgraph.md)
  The optimized representation of a compute graph of operations and tensors.
- [class MPSGraphCompilationDescriptor](mpsgraphcompilationdescriptor.md)
  A class that consists of all the levers for compiling graphs.
- [class MPSGraphConvolution2DOpDescriptor](mpsgraphconvolution2dopdescriptor.md)
  A class that describes the properties of a 2D-convolution operator.
- [class MPSGraphConvolution3DOpDescriptor](mpsgraphconvolution3dopdescriptor.md)
  A class that describes the properties of a 3D-convolution operator.
- [class MPSGraphCreateSparseOpDescriptor](mpsgraphcreatesparseopdescriptor.md)
  A class that describes the properties of a create sparse operation.
- [class MPSGraphDepthwiseConvolution2DOpDescriptor](mpsgraphdepthwiseconvolution2dopdescriptor.md)
  A class that defines the parameters for  a 2D-depthwise convolution operation.
- [class MPSGraphDepthwiseConvolution3DOpDescriptor](mpsgraphdepthwiseconvolution3dopdescriptor.md)
  The class that defines the parameters for a 3D-depthwise convolution operation.
- [class MPSGraphDevice](mpsgraphdevice.md)
  A class that describes the compute device.
- [class MPSGraphExecutable](mpsgraphexecutable.md)
  The compiled representation of a compute graph executable.
- [class MPSGraphExecutableExecutionDescriptor](mpsgraphexecutableexecutiondescriptor.md)
  A class that consists of all the levers  to synchronize and schedule executable execution.
- [class MPSGraphExecutableSerializationDescriptor](mpsgraphexecutableserializationdescriptor.md)
  A class that consists of all the levers  to serialize an executable.
- [class MPSGraphExecutionDescriptor](mpsgraphexecutiondescriptor.md)
  A class that consists of all the levers  to synchronize and schedule graph execution.
- [class MPSGraphFFTDescriptor](mpsgraphfftdescriptor.md)
  The class that defines the parameters for a fast Fourier transform (FFT) operation.
- [class MPSGraphGRUDescriptor](mpsgraphgrudescriptor.md)
  The class that defines the parameters for a gated recurrent unit (GRU) operation.
- [class MPSGraphImToColOpDescriptor](mpsgraphimtocolopdescriptor.md)
  The class that defines the parameters for an image to column or column to image operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomopdescriptor)*