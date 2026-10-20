# arrayLength

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The number of items in the texture array.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var arrayLength: UInt64 { get }
```

```c
uint64_t cp_texture_topology_get_array_length(cp_texture_topology_t texture_topology);
```

#### Discussion

Array-based texture types such as [`MTLTextureType.type2DArray`](../../Metal/mtltexturetype/type2darray.md) manage one or more images of the same size. The array length represents the number of separate images the texture manages. Other array types store only one image.

## See Also

### Getting the layer’s texture topology
- [var textureType: MTLTextureType](./texturetype.md)
  The texture type value that specifies how the underlying texture organizes its views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/texturetopology/arraylength)*