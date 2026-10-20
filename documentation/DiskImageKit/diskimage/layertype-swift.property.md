# layerType

**Framework**: DiskImageKit  
**Kind**: property  
**Role**: Instance Property

The layer type of the disk image.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var layerType: DiskImage.LayerType? { get }
```

#### Discussion

Returns [`cache`](./layertype-swift.struct/cache.md) for cache layers and [`overlay`](./layertype-swift.struct/overlay.md) for overlay layers that are part of a stacked disk image. Returns `nil` for standalone images, for the base layer of a stack and for the stacked image itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layertype-swift.property)*