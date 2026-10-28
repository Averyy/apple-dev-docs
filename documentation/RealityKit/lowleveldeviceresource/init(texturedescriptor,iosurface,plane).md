# init(textureDescriptor:iosurface:plane:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a new [`LowLevelDeviceResource`](../lowleveldeviceresource.md) from the specified `IOSurface`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(textureDescriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) throws
```

## Discussion

> **Throws**: If a the texture descriptor is incompatible with the specified IOSurface

## Parameters

- `textureDescriptor`: A description of the properties for the texture.
- `iosurface`: The underlying IOSurface for this memory resource.
- `plane`: The plane within the IOSurface to use.

## See Also

### Creating a device resource
- [init(sharedTextureHandle: MTLSharedTextureHandle) throws](./init%28sharedtexturehandle%29.md)
  Creates a new [`LowLevelDeviceResource`](../lowleveldeviceresource.md) from the specified Metal shared texture handle. Throws if an MTLTexture cannot be created from the specified handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeviceresource/init(texturedescriptor:iosurface:plane:))*