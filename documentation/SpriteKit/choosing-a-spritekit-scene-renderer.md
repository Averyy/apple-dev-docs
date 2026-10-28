# Choosing a SpriteKit Scene Renderer

**Framework**: SpriteKit  
**Role**: Article

Compare the different ways to display a SpriteKit scene.

## Overview

To display SpriteKit content in a watch app, you use [`WKInterfaceSKScene`](../WatchKit/wkinterfaceskscene.md), whereas on iOS, macOS, and tvOS, you use [`SKView`](./skview.md) to display a SpriteKit scene. If you need to mix SpriteKit with any custom Metal content, use [`SKRenderer`](./skrenderer.md).

> ❗ **Important**:  SKRenderer is not available on watchOS.

### On iOS, tvOS, and macOS, Draw Using a View or a Renderer

Choose from the options below to display SpriteKit content on iOS, tvOS, or macOS.

#### Draw Using a View

To draw SpriteKit content the most common way, set up an [`SKView`](./skview.md) and set its [`scene`](./skview/scene.md) property. See [Drawing SpriteKit Content in a View](./drawing-spritekit-content-in-a-view.md) for an example of using `SKView`.

#### Draw Using a Renderer

When you want to mix SpriteKit content with your own Metal content, use [`SKRenderer`](./skrenderer.md) to draw your [`SKScene`](./skscene.md). You might use `SKRenderer` to replace specific portions of a SpriteKit app with custom Metal code, or vice versa. `SKRenderer` combines the full control of Metal with the ease of use of SpriteKit and its library of useful objects.

For example, to take full control of just your game’s tiled background while using SpriteKit to draw the rest, use an `SKRenderer` and `MTLView` combination instead of `SKView`, and then write the tiled background code yourself in Metal.` `When you’re ready to mix the SpriteKit content with the Metal content, you call `SKRenderer`‘s [`render(withViewport:commandBuffer:renderPassDescriptor:)`](./skrenderer/render%28withviewport,commandbuffer,renderpassdescriptor%29.md). Finally, call [`present(_:)`](../Metal/mtlcommandbuffer/present%28_%29.md) on a Metal view when you’re ready to present a frame.

### On watchOS, Draw Using an Interface Scene

To display SpriteKit content on Apple Watch, you create a [`WKInterfaceSKScene`](../WatchKit/wkinterfaceskscene.md) and then set its [`scene`](../WatchKit/wkinterfaceskscene/scene.md) property. [`WKInterfaceSKScene`](../WatchKit/wkinterfaceskscene.md) functions much like `SKView`, but without the debugging visualization options.

## See Also

### Scene Renderers
- [class SKView](./skview.md)
  A view subclass that renders a SpriteKit scene.
- [class SKRenderer](./skrenderer.md)
  An object that renders a scene into a custom Metal rendering pipeline and drives the scene update cycle.
- [class WKInterfaceSKScene](../WatchKit/wkinterfaceskscene.md)
  A visual WatchKit element that displays a SpriteKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/choosing-a-spritekit-scene-renderer)*