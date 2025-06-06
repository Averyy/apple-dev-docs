# CARenderer

**Framework**: Core Animation  
**Kind**: class

A layer that allows an application to render a layer tree into a Core OpenGL context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CARenderer
```

#### Overview

For real-time output you should use an instance of [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) to host the layer-tree.

## Topics

### Creating a Renderer
- [init(cglContext: UnsafeMutableRawPointer, options: [AnyHashable : Any]?)](carenderer/init(cglcontext:options:).md)
  Creates and returns a `CARenderer` instance with the render target specified by the Core OpenGL context.
- [init(mtlTexture: any MTLTexture, options: [AnyHashable : Any]?)](carenderer/init(mtltexture:options:).md)
  Creates a layer renderer from a Metal texture.
### Getting the Rendered Layer
- [var layer: CALayer?](carenderer/layer.md)
  The root layer of the layer-tree the receiver should render.
### Determining Layer Bounds
- [var bounds: CGRect](carenderer/bounds.md)
  The bounds of the receiver.
### Rendering a Frame
- [func beginFrame(atTime: CFTimeInterval, timeStamp: UnsafeMutablePointer<CVTimeStamp>?)](carenderer/beginframe(attime:timestamp:).md)
  Begin rendering a frame at the specified time.
- [func updateBounds() -> CGRect](carenderer/updatebounds.md)
  Returns the bounds of the update region that contains all pixels that will be rendered by the current frame.
- [func addUpdate(CGRect)](carenderer/addupdate(_:).md)
  Adds the rectangle to the update region of the current frame.
- [func render()](carenderer/render.md)
  Render the update region of the current frame to the target context.
- [func nextFrameTime() -> CFTimeInterval](carenderer/nextframetime.md)
  Returns the time at which the next update should happen.
- [func endFrame()](carenderer/endframe.md)
  Release any data associated with the current frame.
### Instance Methods
- [func setDestination(any MTLTexture)](carenderer/setdestination(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CAMetalLayer](cametallayer.md)
  A Core Animation layer that Metal can render into, typically displayed onscreen.
- [protocol CAMetalDrawable](cametaldrawable.md)
  A Metal drawable associated with a Core Animation layer.
- [class CAEAGLLayer](caeagllayer.md)
  A layer that supports drawing OpenGL content in iOS and tvOS applications.
- [class CAEDRMetadata](caedrmetadata.md)
  Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [class CAOpenGLLayer](caopengllayer.md)
  A layer that provides a layer suitable for rendering OpenGL content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/carenderer)*