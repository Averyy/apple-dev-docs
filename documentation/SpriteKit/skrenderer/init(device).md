# init(device:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (SKRenderer *) rendererWithDevice:(id<MTLDevice>) device;
```

#### Return Value

A new renderer object.

#### Discussion

Pass in the same Metal device that is associated to the Metal command buffer passed into [`render(withViewport:commandBuffer:renderPassDescriptor:)`](./render%28withviewport,commandbuffer,renderpassdescriptor%29.md).

## Parameters

- `device`: A Metal device.

## See Also

### First Steps
- [var scene: SKScene?](./scene.md)
  The scene this renderer will draw into the Metal command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrenderer/init(device:))*