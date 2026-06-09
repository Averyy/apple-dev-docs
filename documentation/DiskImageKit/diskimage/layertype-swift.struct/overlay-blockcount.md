# overlay(blockCount:)

**Framework**: DiskImageKit  
**Kind**: method

An overlay layer with a specific block count.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static func overlay(blockCount: Int) -> DiskImage.LayerType
```

#### Discussion

Overlay layers store all the changed blocks from the layers beneath it in the stack. This variant resizes the stacked disk image since the size is determined by the top-most layer.

## Parameters

- `blockCount`: The number of blocks for the overlay layer, which changes the effective size of the entire stack. `blockCount` must be greater than zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layertype-swift.struct/overlay(blockcount:))*