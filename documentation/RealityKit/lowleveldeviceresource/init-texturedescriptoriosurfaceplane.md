# init(textureDescriptor:iosurface:plane:)

**Framework**: RealityKit  
**Kind**: init

Creates a new [`LowLevelDeviceResource`](lowleveldeviceresource.md) from the specified `IOSurface`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(textureDescriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) throws
```

#### Discussion

> **Note**: If a the texture descriptor is incompatible with the specified IOSurface

## Parameters

- `textureDescriptor`: A description of the properties for the texture.
- `iosurface`: The underlying IOSurface for this memory resource.
- `plane`: The plane within the IOSurface to use.

## See Also

- [init(sharedTextureHandle: MTLSharedTextureHandle) throws](lowleveldeviceresource/init(sharedtexturehandle:).md)
  Creates a new [`LowLevelDeviceResource`](lowleveldeviceresource.md) from the specified Metal shared texture handle. Throws if an MTLTexture cannot be created from the specified handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeviceresource/init(texturedescriptor:iosurface:plane:))*