# MTLOrigin

**Framework**: Metal  
**Kind**: struct

The coordinates for the front upper-left corner of a region.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLOrigin
```

## Topics

### Creating Origin Points
- [init()](mtlorigin/init.md)
  Initializes a new origin.
- [init(x: Int, y: Int, z: Int)](mtlorigin/init(x:y:z:).md)
  Initializes a new origin with the specified coordinates.
- [func MTLOriginMake(Int, Int, Int) -> MTLOrigin](mtloriginmake(_:_:_:).md)
  Returns a new origin with the specified coordinates.
### Getting and Setting Coordinate Values
- [var x: Int](mtlorigin/x.md)
  The x coordinate of the origin.
- [var y: Int](mtlorigin/y.md)
  The y coordinate of the origin.
- [var z: Int](mtlorigin/z.md)
  The z coordinate of the origin.

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
- [struct MTLStageInRegionIndirectArguments](mtlstageinregionindirectarguments.md)
  The data layout required for the arguments needed to specify the stage-in region.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlorigin)*