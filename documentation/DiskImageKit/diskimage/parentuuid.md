# parentUUID

**Framework**: DiskImageKit  
**Kind**: property

A UUID of the image that must be equal to the layer UUID of the layer beneath it in the stack.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var parentUUID: UUID? { get }
```

#### Discussion

This property is in a set state for all images in a stacked disk image, where the layer beneath them has a [`layerUUID`](diskimage/layeruuid.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/parentuuid)*