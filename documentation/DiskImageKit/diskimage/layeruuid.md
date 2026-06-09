# layerUUID

**Framework**: DiskImageKit  
**Kind**: property

A UUID of the image that the framework uses to validate its compatibility with the layer above it in the stack

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var layerUUID: UUID? { get }
```

#### Discussion

All images contain a layer UUID, except for RAW images.

The layer UUID changes when the framework first writes to an image. In a stacked disk image, the framework can only write to the topmost image. The layer UUID of cache layers never changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/layeruuid)*