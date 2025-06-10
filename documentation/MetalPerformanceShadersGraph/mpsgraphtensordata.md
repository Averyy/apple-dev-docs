# MPSGraphTensorData

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The representation of a compute data type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphTensorData
```

#### Overview

Pass data to a graph using a tensor data, a reference will be taken to your data and used just in time when the graph is run.

## Topics

### Initializers
- [init(MPSMatrix)](mpsgraphtensordata/init(_:)-2go2.md)
  Initializes a tensor data with an MPS matrix.
- [init(MPSNDArray)](mpsgraphtensordata/init(_:)-4bnfb.md)
  Initializes an MPSGraphTensorData with an MPS ndarray.
- [init([MPSImage])](mpsgraphtensordata/init(_:)-511a.md)
  Initializes a tensor data with an MPS image batch.
- [init(any MTLTensor)](mpsgraphtensordata/init(_:)-60j6x.md)
  Initializes an MPSGraphTensorData with an MTLTensor.
- [init(MPSVector)](mpsgraphtensordata/init(_:)-9kgoe.md)
  Initializes a tensor data with an MPS vector.
- [init(MPSVector, rank: Int)](mpsgraphtensordata/init(_:rank:)-1e4ks.md)
  Initializes a tensor data with an MPS vector enforcing rank of the result.
- [init(MPSMatrix, rank: Int)](mpsgraphtensordata/init(_:rank:)-1lnxg.md)
  Initializes a tensor data with an MPS matrix enforcing rank of the result.
- [init(any MTLBuffer, shape: [NSNumber], dataType: MPSDataType)](mpsgraphtensordata/init(_:shape:datatype:).md)
  Initializes an tensor data with a metal buffer.
- [init(any MTLBuffer, shape: [NSNumber], dataType: MPSDataType, rowBytes: Int)](mpsgraphtensordata/init(_:shape:datatype:rowbytes:).md)
  Initializes an tensor data with a metal buffer.
- [init(device: MPSGraphDevice, data: Data, shape: [NSNumber], dataType: MPSDataType)](mpsgraphtensordata/init(device:data:shape:datatype:).md)
  Initializes the tensor data with an `NSData` on a device.
### Instance Properties
- [var dataType: MPSDataType](mpsgraphtensordata/datatype.md)
  The data type of the tensor data.
- [var device: MPSGraphDevice](mpsgraphtensordata/device.md)
  The device of the tensor data.
- [var shape: [NSNumber]](mpsgraphtensordata/shape.md)
  The shape of the tensor data.
### Instance Methods
- [func mpsndarray() -> MPSNDArray](mpsgraphtensordata/mpsndarray.md)
  Return an mpsndarray object will copy contents if the contents are not stored in an MPS ndarray.

## Relationships

### Inherits From
- [MPSGraphObject](mpsgraphobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata)*