# init(texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a new [`LowLevelDeviceResource`](lowleveldeviceresource.md) from the specified Metal texture. This is not available on visionOS; device resources on this platform must be initialized from a shared texture using `init(sharedTextureHandle:)` instead.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
init(texture: any MTLTexture)
```

## Parameters

- `texture`: The underlying texture for this memory resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeviceresource/init(texture:))*