# MTLAttributeDescriptorArray

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An array of attribute descriptor objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAttributeDescriptorArray
```

```objc
@interface MTLAttributeDescriptorArray : NSObject
```

#### Overview

An [`MTLAttributeDescriptorArray`](./mtlattributedescriptorarray.md) defines the data format and index binding for the attribute argument table, using [`MTLAttributeDescriptor`](./mtlattributedescriptor.md) instances.

## Topics

### Accessing attribute state objects
- [subscript(Int) -> MTLAttributeDescriptor!](./mtlattributedescriptorarray/subscript%28_%29.md)
  Returns the state of the specified attribute.

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
- [class MTLBufferLayoutDescriptor](./mtlbufferlayoutdescriptor.md)
  A description of how a compute function fetches input data for an attribute.
- [class MTLBufferLayoutDescriptorArray](./mtlbufferlayoutdescriptorarray.md)
  An array of buffer layout descriptor objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributedescriptorarray)*