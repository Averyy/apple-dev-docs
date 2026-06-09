# overlay

**Framework**: DiskImageKit  
**Kind**: property

An overlay layer that inherits its size from the layer beneath it.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static let overlay: DiskImage.LayerType
```

#### Discussion

Overlay layers store all the changed blocks from the layers beneath it in the stack. This variant inherits the size from the layer beneath it. To create overlay layers with a specific block count, use [`overlay(blockCount:)`](diskimage/layertype-swift.struct/overlay(blockcount:).md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layertype-swift.struct/overlay)*