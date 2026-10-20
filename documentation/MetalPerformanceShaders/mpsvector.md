# MPSVector

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A 1D array of data that stores the data’s values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSVector
```

```objc
@interface MPSVector : NSObject
```

## Topics

### Initializers
- [init(buffer: any MTLBuffer, descriptor: MPSVectorDescriptor)](./mpsvector/init%28buffer,descriptor%29.md)
- [init(buffer: any MTLBuffer, offset: Int, descriptor: MPSVectorDescriptor)](./mpsvector/init%28buffer,offset,descriptor%29.md)
- [init(device: any MTLDevice, descriptor: MPSVectorDescriptor)](./mpsvector/init%28device,descriptor%29.md)
### Instance Properties
- [var data: any MTLBuffer](./mpsvector/data.md)
- [var dataType: MPSDataType](./mpsvector/datatype.md)
- [var device: any MTLDevice](./mpsvector/device.md)
- [var length: Int](./mpsvector/length.md)
- [var vectorBytes: Int](./mpsvector/vectorbytes.md)
- [var vectors: Int](./mpsvector/vectors.md)
- [var offset: Int](./mpsvector/offset.md)
### Instance Methods
- [func resourceSize() -> Int](./mpsvector/resourcesize%28%29.md)
- [func synchronize(on: any MTLCommandBuffer)](./mpsvector/synchronize%28on%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPSTemporaryVector](./mpstemporaryvector.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Vectors
- [class MPSVectorDescriptor](./mpsvectordescriptor.md)
  A description of the length and data type of a vector.
- [class MPSTemporaryVector](./mpstemporaryvector.md)
  A vector allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsvector)*