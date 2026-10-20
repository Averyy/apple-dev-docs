# MPSTemporaryVector

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A vector allocated on GPU private memory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSTemporaryVector
```

```objc
@interface MPSTemporaryVector : MPSVector
```

## Topics

### Initializers
- [convenience init(commandBuffer: any MTLCommandBuffer, descriptor: MPSVectorDescriptor)](./mpstemporaryvector/init%28commandbuffer,descriptor%29.md)
### Instance Properties
- [var readCount: Int](./mpstemporaryvector/readcount.md)
### Type Methods
- [class func prefetchStorage(with: any MTLCommandBuffer, descriptorList: [MPSVectorDescriptor])](./mpstemporaryvector/prefetchstorage%28with,descriptorlist%29.md)

## Relationships

### Inherits From
- [MPSVector](./mpsvector.md)
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
- [class MPSVectorDescriptor](./mpsvectordescriptor.md)
  A description of the length and data type of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryvector)*