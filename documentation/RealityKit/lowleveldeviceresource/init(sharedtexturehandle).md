# init(sharedTextureHandle:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a new [`LowLevelDeviceResource`](../lowleveldeviceresource.md) from the specified Metal shared texture handle. Throws if an MTLTexture cannot be created from the specified handle.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(sharedTextureHandle: MTLSharedTextureHandle) throws
```

## Discussion

> **Throws**: If a MTLTexture couldn’t be created from the specified handle.

## Parameters

- `sharedTextureHandle`: The underlying shared texture handle for this memory resource.

## See Also

### Creating a device resource
- [init(textureDescriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) throws](./init%28texturedescriptor,iosurface,plane%29.md)
  Creates a new [`LowLevelDeviceResource`](../lowleveldeviceresource.md) from the specified `IOSurface`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeviceresource/init(sharedtexturehandle:))*