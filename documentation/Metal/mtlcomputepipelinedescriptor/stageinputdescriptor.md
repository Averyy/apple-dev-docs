# stageInputDescriptor

**Framework**: Metal  
**Kind**: property

The organization of input and output data for the next kernel call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var stageInputDescriptor: MTLStageInputOutputDescriptor? { get set }
```

## See Also

- [class MTLAttributeDescriptor](mtlattributedescriptor.md)
  A descriptor of an argument’s format and where its data is in memory.
- [class MTLAttributeDescriptorArray](mtlattributedescriptorarray.md)
  An array of attribute descriptor objects.
- [class MTLBufferLayoutDescriptor](mtlbufferlayoutdescriptor.md)
  A description of how a compute function fetches input data for an attribute.
- [class MTLBufferLayoutDescriptorArray](mtlbufferlayoutdescriptorarray.md)
  An array of buffer layout descriptor objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/stageinputdescriptor)*