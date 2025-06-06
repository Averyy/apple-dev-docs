# init(device:)

**Framework**: SpriteKit  
**Kind**: init

Initializes with a specific GPU to render into.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice)
```

#### Return Value

A new renderer object.

#### Discussion

Pass in the same Metal device that is associated to the Metal command buffer passed into [`render(withViewport:commandBuffer:renderPassDescriptor:)`](skrenderer/render(withviewport:commandbuffer:renderpassdescriptor:).md).

## Parameters

- `device`: A Metal device.

## See Also

- [var scene: SKScene?](skrenderer/scene.md)
  The scene this renderer will draw into the Metal command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrenderer/init(device:))*