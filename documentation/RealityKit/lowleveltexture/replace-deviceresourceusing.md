# replace(deviceResource:using:)

**Framework**: RealityKit  
**Kind**: method

Replaces this object’s underlying texture with an existing [`LowLevelDeviceResource`](lowleveldeviceresource.md) created and managed by the application.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func replace(deviceResource: LowLevelDeviceResource, using commandBuffer: (any MTLCommandBuffer)? = nil)
```

#### Discussion

While it’s valid to replace a LowLevelTexture with an externally-managed texture having different dimensions, the LowLevelTexture will remember its initial size and calling replace(using:) to obtain a new MTLTexture will respect the initial size.

## Parameters

- `deviceResource`: The underlying texture this object should refer to.
- `commandBuffer`: The [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) you intend to use for texture modifications. RealityKit waits for the command buffer to complete before utilizing the texture for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltexture/replace(deviceresource:using:))*