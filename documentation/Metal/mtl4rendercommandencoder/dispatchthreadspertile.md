# dispatchThreadsPerTile(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that invokes a tile shader function from the encoder’s current tile render pipeline state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func dispatchThreadsPerTile(_ threadsPerTile: MTLSize)
```

## Parameters

- `threadsPerTile`: A   instance that represents the number of threads the render pass uses per tile.   Set the size’s   and   properties to values that are less   than or equal to   and  , respectively. Some GPU families   only support square tile dispatches and require the same value for width and height.   Set   to  .

## See Also

- [var tileWidth: Int](mtl4rendercommandencoder/tilewidth.md)
  Sets the width of a tile for this render pass.
- [var tileHeight: Int](mtl4rendercommandencoder/tileheight.md)
  Sets the height of a tile for this render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/dispatchthreadspertile(_:))*