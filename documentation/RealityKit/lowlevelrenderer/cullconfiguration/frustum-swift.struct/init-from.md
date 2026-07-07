# init(from:)

**Framework**: RealityKit  
**Kind**: init

Creates a frustum by computing the culling planes for the given camera.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(from camera: LowLevelRenderer.Camera)
```

#### Discussion

Produces up to six outward-facing planes corresponding to the camera’s view volume. For perspective cameras with an infinite far plane, the far plane is omitted, yielding five planes.

## Parameters

- `camera`: The camera whose view volume defines the frustum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cullconfiguration/frustum-swift.struct/init(from:))*