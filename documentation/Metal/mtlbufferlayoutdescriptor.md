# MTLBufferLayoutDescriptor

**Framework**: Metal  
**Kind**: class

A description of how a compute function fetches input data for an attribute.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLBufferLayoutDescriptor
```

## Topics

### Describing Fetch Behavior
- [var stride: Int](mtlbufferlayoutdescriptor/stride.md)
  The number of bytes from one buffer entry to the next.
- [var stepFunction: MTLStepFunction](mtlbufferlayoutdescriptor/stepfunction.md)
  Determines how and when compute functions fetch data.
- [var stepRate: Int](mtlbufferlayoutdescriptor/steprate.md)
  How frequently the step function should load data.
- [enum MTLStepFunction](mtlstepfunction.md)
  The frequency and locations at which a function fetches attribute data.

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

- [var stageInputDescriptor: MTLStageInputOutputDescriptor?](mtlcomputepipelinedescriptor/stageinputdescriptor.md)
  The organization of input and output data for the next kernel call.
- [class MTLAttributeDescriptor](mtlattributedescriptor.md)
  A descriptor of an argument’s format and where its data is in memory.
- [class MTLAttributeDescriptorArray](mtlattributedescriptorarray.md)
  An array of attribute descriptor objects.
- [class MTLBufferLayoutDescriptorArray](mtlbufferlayoutdescriptorarray.md)
  An array of buffer layout descriptor objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor)*