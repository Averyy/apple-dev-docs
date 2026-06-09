# layerType

**Framework**: DiskImageKit  
**Kind**: property

The layer type of the disk image.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var layerType: DiskImage.LayerType? { get }
```

#### Discussion

Returns [`cache`](diskimage/layertype-swift.struct/cache.md) for cache layers and [`overlay`](diskimage/layertype-swift.struct/overlay.md) for overlay layers that are part of a stacked disk image. Returns `nil` for standalone images, for the base layer of a stack and for the stacked image itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layertype-swift.property)*