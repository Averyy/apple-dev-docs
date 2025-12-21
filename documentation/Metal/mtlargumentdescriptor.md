# MTLArgumentDescriptor

**Framework**: Metal  
**Kind**: class

A representation of an argument within an argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MTLArgumentDescriptor
```

#### Overview

This descriptor can represent arguments within flat structures only. It can represent arrays of allowed argument buffer data types, but it cannot represent arguments within nested structures. Argument buffers with simple, flat structures can be represented by an array of [`MTLArgumentDescriptor`](mtlargumentdescriptor.md) instances. You can then use this array to create an [`MTLArgumentEncoder`](mtlargumentencoder.md) instance by calling the [`makeArgumentEncoder(arguments:)`](mtldevice/makeargumentencoder(arguments:).md) method. Argument buffers with complex, nested structures need to define their structure in Metal shading language code, which can then be directly assigned to a specific buffer index of a function. You can then use this buffer index to call the [`makeArgumentEncoder(bufferIndex:)`](mtlfunction/makeargumentencoder(bufferindex:).md) method and create an [`MTLArgumentEncoder`](mtlargumentencoder.md) instance.

## Topics

### Setting the descriptor’s properties
- [var dataType: MTLDataType](mtlargumentdescriptor/datatype.md)
  The data type of the argument.
- [var index: Int](mtlargumentdescriptor/index.md)
  The index ID of the argument.
- [var access: MTLBindingAccess](mtlargumentdescriptor/access.md)
  The access permissions of the argument.
- [var arrayLength: Int](mtlargumentdescriptor/arraylength.md)
  The length of an array argument.
- [var constantBlockAlignment: Int](mtlargumentdescriptor/constantblockalignment.md)
  The alignment of the constant block.
- [var textureType: MTLTextureType](mtlargumentdescriptor/texturetype.md)
  The texture type of a texture argument.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
  Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)
  Optimize resource performance within an argument buffer.
- [Indexing argument buffers](indexing-argument-buffers.md)
  Assign resource indices within an argument buffer.
- [Rendering terrain dynamically with argument buffers](rendering-terrain-dynamically-with-argument-buffers.md)
  Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding argument buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [protocol MTLArgumentEncoder](mtlargumentencoder.md)
  An interface you can use to encode argument data into an argument buffer.
- [let MTLAttributeStrideStatic: Int](mtlattributestridestatic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentdescriptor)*