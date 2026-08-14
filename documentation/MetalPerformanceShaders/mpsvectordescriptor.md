# MPSVectorDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [convenience init(length: Int, dataType: MPSDataType)](mpsvectordescriptor/init(length:datatype:).md)
- [convenience init(length: Int, vectors: Int, vectorBytes: Int, dataType: MPSDataType)](mpsvectordescriptor/init(length:vectors:vectorbytes:datatype:).md)
### Instance Properties
- [var dataType: MPSDataType](mpsvectordescriptor/datatype.md)
- [var length: Int](mpsvectordescriptor/length.md)
- [var vectorBytes: Int](mpsvectordescriptor/vectorbytes.md)
- [var vectors: Int](mpsvectordescriptor/vectors.md)
### Type Methods
- [class func vectorBytes(forLength: Int, dataType: MPSDataType) -> Int](mpsvectordescriptor/vectorbytes(forlength:datatype:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MPSVector](mpsvector.md)
  A 1D array of data that stores the data’s values.
- [class MPSTemporaryVector](mpstemporaryvector.md)
  A vector allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsvectordescriptor)*