# MTLStageInRegionIndirectArguments

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

The data layout required for the arguments needed to specify the stage-in region.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLStageInRegionIndirectArguments
```

```c
typedef struct { ... } MTLStageInRegionIndirectArguments;
```

## Topics

### Initializers
- [init()](./mtlstageinregionindirectarguments/init%28%29.md)
- [init(stageInOrigin: (UInt32, UInt32, UInt32), stageInSize: (UInt32, UInt32, UInt32))](./mtlstageinregionindirectarguments/init%28stageinorigin,stageinsize%29.md)
### Instance Properties
- [var stageInOrigin: (UInt32, UInt32, UInt32)](./mtlstageinregionindirectarguments/stageinorigin.md)
  The location of the upper-left corner of the block.
- [var stageInSize: (UInt32, UInt32, UInt32)](./mtlstageinregionindirectarguments/stageinsize.md)
  The size of the block.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Indirect compute commands
- [protocol MTLIndirectComputeCommand](./mtlindirectcomputecommand.md)
  A compute command in an indirect command buffer.
- [struct MTLRegion](./mtlregion.md)
  The bounds for a subset of an instance’s elements.
- [struct MTLSize](./mtlsize.md)
  A type that represents one, two, or three dimensions of a type instance, such as an array or texture.
- [struct MTLOrigin](./mtlorigin.md)
  The coordinates for the front upper-left corner of a region.
- [struct MTLDispatchThreadgroupsIndirectArguments](./mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstageinregionindirectarguments)*