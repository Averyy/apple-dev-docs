# MTLBufferLayoutDescriptorArray

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An array of buffer layout descriptor objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLBufferLayoutDescriptorArray
```

```objc
@interface MTLBufferLayoutDescriptorArray : NSObject
```

## Overview

An [`MTLBufferLayoutDescriptorArray`](./mtlbufferlayoutdescriptorarray.md) defines the data layout and loading for compute data, using [`MTLBufferLayoutDescriptor`](./mtlbufferlayoutdescriptor.md) instances.

## Topics

### Array accessors
- [subscript(Int) -> MTLBufferLayoutDescriptor!](./mtlbufferlayoutdescriptorarray/subscript%28_%29.md)
  Returns the state of the specified buffer layout.
- [- setObject:atIndexedSubscript:](./mtlbufferlayoutdescriptorarray/setobject_atindexedsubscript_.md)
  Sets the state of the specified buffer layout.

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

### Configuring compute pass inputs
- [var stageInputDescriptor: MTLStageInputOutputDescriptor?](./mtlcomputepipelinedescriptor/stageinputdescriptor.md)
  The organization of input and output data for the next kernel call.
- [class MTLAttributeDescriptor](./mtlattributedescriptor.md)
  A descriptor of an argument’s format and where its data is in memory.
- [class MTLAttributeDescriptorArray](./mtlattributedescriptorarray.md)
  An array of attribute descriptor objects.
- [class MTLBufferLayoutDescriptor](./mtlbufferlayoutdescriptor.md)
  A description of how a compute function fetches input data for an attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray)*