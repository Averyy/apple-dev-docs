# cache

**Framework**: DiskImageKit  
**Kind**: property

A cache layer.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static let cache: DiskImage.LayerType
```

#### Discussion

Cache layers store all the blocks read from the layers beneath it in the stack. A cache layer is useful when the base image is on a network mount, for example.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layertype-swift.struct/cache)*