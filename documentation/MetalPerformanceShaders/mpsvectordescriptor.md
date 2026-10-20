# MPSVectorDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A description of the length and data type of a vector.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSVectorDescriptor
```

```objc
@interface MPSVectorDescriptor : NSObject
```

## Topics

### Initializers
- [convenience init(length: Int, dataType: MPSDataType)](./mpsvectordescriptor/init%28length,datatype%29.md)
- [convenience init(length: Int, vectors: Int, vectorBytes: Int, dataType: MPSDataType)](./mpsvectordescriptor/init%28length,vectors,vectorbytes,datatype%29.md)
### Instance Properties
- [var dataType: MPSDataType](./mpsvectordescriptor/datatype.md)
- [var length: Int](./mpsvectordescriptor/length.md)
- [var vectorBytes: Int](./mpsvectordescriptor/vectorbytes.md)
- [var vectors: Int](./mpsvectordescriptor/vectors.md)
### Type Methods
- [class func vectorBytes(forLength: Int, dataType: MPSDataType) -> Int](./mpsvectordescriptor/vectorbytes%28forlength,datatype%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Vectors
- [class MPSVector](./mpsvector.md)
  A 1D array of data that stores the data’s values.
- [class MPSTemporaryVector](./mpstemporaryvector.md)
  A vector allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsvectordescriptor)*