# MPSTemporaryVector

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [convenience init(commandBuffer: any MTLCommandBuffer, descriptor: MPSVectorDescriptor)](mpstemporaryvector/init(commandbuffer:descriptor:).md)
### Instance Properties
- [var readCount: Int](mpstemporaryvector/readcount.md)
### Type Methods
- [class func prefetchStorage(with: any MTLCommandBuffer, descriptorList: [MPSVectorDescriptor])](mpstemporaryvector/prefetchstorage(with:descriptorlist:).md)

## Relationships

### Inherits From
- [MPSVector](mpsvector.md)
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
- [class MPSVectorDescriptor](mpsvectordescriptor.md)
  A description of the length and data type of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryvector)*