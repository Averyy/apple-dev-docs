# MTLStageInRegionIndirectArguments

**Framework**: Metal  
**Kind**: struct

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

## Topics

### Initializers
- [init()](mtlstageinregionindirectarguments/init.md)
- [init(stageInOrigin: (UInt32, UInt32, UInt32), stageInSize: (UInt32, UInt32, UInt32))](mtlstageinregionindirectarguments/init(stageinorigin:stageinsize:).md)
### Instance Properties
- [var stageInOrigin: (UInt32, UInt32, UInt32)](mtlstageinregionindirectarguments/stageinorigin.md)
  The location of the upper-left corner of the block.
- [var stageInSize: (UInt32, UInt32, UInt32)](mtlstageinregionindirectarguments/stageinsize.md)
  The size of the block.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIndirectComputeCommand](mtlindirectcomputecommand.md)
  A compute command in an indirect command buffer.
- [struct MTLRegion](mtlregion.md)
  The bounds for a subset of an object’s elements.
- [struct MTLSize](mtlsize.md)
  The dimensions of an object.
- [struct MTLOrigin](mtlorigin.md)
  The coordinates for the front upper-left corner of a region.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstageinregionindirectarguments)*