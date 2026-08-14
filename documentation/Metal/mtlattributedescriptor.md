# MTLAttributeDescriptor

**Framework**: Metal  
**Kind**: class

A descriptor of an argument’s format and where its data is in memory.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAttributeDescriptor
```

#### Overview

Attribute descriptors are part of an [`MTLVertexDescriptor`](mtlvertexdescriptor.md) or [`MTLStageInputOutputDescriptor`](mtlstageinputoutputdescriptor.md) instance to provide layout information about a function’s arguments. Each descriptor is for a single argument, containing information about the attached data, offset and stride, and data type.

## Topics

### Defining attribute location
- [var bufferIndex: Int](mtlattributedescriptor/bufferindex.md)
  The index in the buffer argument table for the buffer that contains the data for this attribute.
- [var offset: Int](mtlattributedescriptor/offset.md)
  The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.
- [var format: MTLAttributeFormat](mtlattributedescriptor/format.md)
  The format of the attribute’s data.
- [enum MTLAttributeFormat](mtlattributeformat.md)
  The data format options for acceleration structures.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var stageInputDescriptor: MTLStageInputOutputDescriptor?](mtlcomputepipelinedescriptor/stageinputdescriptor.md)
  The organization of input and output data for the next kernel call.
- [class MTLAttributeDescriptorArray](mtlattributedescriptorarray.md)
  An array of attribute descriptor objects.
- [class MTLBufferLayoutDescriptor](mtlbufferlayoutdescriptor.md)
  A description of how a compute function fetches input data for an attribute.
- [class MTLBufferLayoutDescriptorArray](mtlbufferlayoutdescriptorarray.md)
  An array of buffer layout descriptor objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributedescriptor)*