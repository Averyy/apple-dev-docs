# appending(_:)

**Framework**: DiskImageKit  
**Kind**: method

Appends a layer to this disk image, creating or extending a stack.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
consuming func appending(_ layer: consuming DiskImage) throws -> any StackedImage
```

#### Return Value

A [`StackedImage`](stackedimage.md) containing all layers.

#### Discussion

> **Note**: The framework allows only one cache layer per stacked disk image.

This method creates a stacked disk image by appending a layer to either a base image or an existing stacked image. When the image is already a stacked image, the framework adds the new layer on top of the existing stack.

> **Note**: [`IncompatibleStackingError`](incompatiblestackingerror.md) if the appended layer isn’t compatible with the stack.

## Parameters

- `layer`: An existing disk image to append as the new top layer.

## See Also

- [DiskImage.StackableLayer](diskimage/stackablelayer.md)
  A marker protocol that stackable disk image layer configuration objects conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/appending(_:)-4wifj)*