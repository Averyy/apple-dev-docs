# SKRenderer

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

An object that renders a scene into a custom Metal rendering pipeline and drives the scene update cycle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class SKRenderer
```

```objc
@interface SKRenderer : NSObject
```

## Mentions

- [Choosing a SpriteKit Scene Renderer](./choosing-a-spritekit-scene-renderer.md)

#### Overview

[`SKRenderer`](./skrenderer.md) allows an app to mix SpriteKit and Metal content by rendering an [`SKScene`](./skscene.md) into a Metal command buffer. The reasons an app may do this instead of displaying a scene in [`SKView`](./skview.md) are:

1. Apps that are built in Metal can mix in SpriteKit content. While it’s possible to add [`SKView`](./skview.md) as a subview to a Metal view, plugging [`SKRenderer`](./skrenderer.md) into their Metal pipeline allows layering SpriteKit content at a specific z-position.
2. You might be writing a SpriteKit app and decide later to take full control over some portion of renderering by implementing it with Metal, yet continue to use SpriteKit for the rest of the app. For example, you might write the environmental effects layer of your app that does fog, clouds, and rain, with custom Metal shaders, and continue to layer content below and above that with SpriteKit.

## Topics

### First Steps
- [init(device: any MTLDevice)](./skrenderer/init%28device%29.md)
  Initializes with a specific GPU to render into.
- [var scene: SKScene?](./skrenderer/scene.md)
  The scene this renderer will draw into the Metal command buffer.
### Rendering the Scene
- [func render(withViewport: CGRect, commandBuffer: any MTLCommandBuffer, renderPassDescriptor: MTLRenderPassDescriptor)](./skrenderer/render%28withviewport,commandbuffer,renderpassdescriptor%29.md)
- [func render(withViewport: CGRect, renderCommandEncoder: any MTLRenderCommandEncoder, renderPassDescriptor: MTLRenderPassDescriptor, commandQueue: any MTLCommandQueue)](./skrenderer/render%28withviewport,rendercommandencoder,renderpassdescriptor,commandqueue%29.md)
### Driving the Scene’s Update Cycle
- [func update(atTime: TimeInterval)](./skrenderer/update%28attime%29.md)
### Configuring Performance Related Toggles
- [var ignoresSiblingOrder: Bool](./skrenderer/ignoressiblingorder.md)
- [var shouldCullNonVisibleNodes: Bool](./skrenderer/shouldcullnonvisiblenodes.md)
### Enabling Visual Statistics for Debugging
- [var showsNodeCount: Bool](./skrenderer/showsnodecount.md)
  A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.
- [var showsDrawCount: Bool](./skrenderer/showsdrawcount.md)
  A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.
- [var showsQuadCount: Bool](./skrenderer/showsquadcount.md)
  A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.
- [var showsPhysics: Bool](./skrenderer/showsphysics.md)
  A Boolean value that indicates whether the view displays physics-related debugging information.
- [var showsFields: Bool](./skrenderer/showsfields.md)
  A Boolean value that indicates whether the view displays information about physics fields in the scene.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Scene Renderers
- [Choosing a SpriteKit Scene Renderer](./choosing-a-spritekit-scene-renderer.md)
  Compare the different ways to display a SpriteKit scene.
- [class SKView](./skview.md)
  A view subclass that renders a SpriteKit scene.
- [class WKInterfaceSKScene](../WatchKit/wkinterfaceskscene.md)
  A visual WatchKit element that displays a SpriteKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrenderer)*