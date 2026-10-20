# MTLOrigin

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

The coordinates for the front upper-left corner of a region.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MTLOrigin
```

```c
typedef struct { ... } MTLOrigin;
```

## Topics

### Creating origin points
- [init()](./mtlorigin/init%28%29.md)
  Initializes a new origin.
- [init(x: Int, y: Int, z: Int)](./mtlorigin/init%28x,y,z%29.md)
  Initializes a new origin with the specified coordinates.
- [func MTLOriginMake(Int, Int, Int) -> MTLOrigin](./mtloriginmake%28_,_,_%29.md)
  Returns a new origin with the specified coordinates.
### Getting and setting coordinate values
- [var x: Int](./mtlorigin/x.md)
  The x coordinate of the origin.
- [var y: Int](./mtlorigin/y.md)
  The y coordinate of the origin.
- [var z: Int](./mtlorigin/z.md)
  The z coordinate of the origin.

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
- [struct MTLStageInRegionIndirectArguments](./mtlstageinregionindirectarguments.md)
  The data layout required for the arguments needed to specify the stage-in region.
- [struct MTLDispatchThreadgroupsIndirectArguments](./mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlorigin)*