# UIGraphicsImageRendererContext

**Framework**: UIKit  
**Kind**: class

The drawing environment for an image renderer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsImageRendererContext
```

#### Overview

When using the [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md) drawing methods, you must pass a block of type [`UIGraphicsImageRenderer.DrawingActions`](uigraphicsimagerenderer/drawingactions.md) as an argument, which provides a [`UIGraphicsImageRendererContext`](uigraphicsimagerenderercontext.md) instance as an argument. Use the context object to access high-level drawing functions and the underlying Core Graphics context.

> **Note**:  `UIGraphicsImageRendererContext` inherits much of its functionality from its abstract superclass [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md).

To learn how to use a `UIGraphicsImageRendererContext` object in combination with an image renderer, see [`Creating a graphics image renderer`](uigraphicsimagerenderer#Creating-a-graphics-image-renderer.md).

## Topics

### Getting the image
- [var currentImage: UIImage](uigraphicsimagerenderercontext/currentimage.md)
  The current state of the drawing context, expressed as an object that manages image data in your app.
### Getting the image drawing actions
- [UIGraphicsImageRenderer.DrawingActions](uigraphicsimagerenderer/drawingactions.md)
  A closure for drawing an image.

## Relationships

### Inherits From
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIGraphicsRenderer](uigraphicsrenderer.md)
  An abstract base class for creating graphics renderers.
- [class UIGraphicsRendererContext](uigraphicsrenderercontext.md)
  The base class for the drawing environments for graphics renderers.
- [class UIGraphicsRendererFormat](uigraphicsrendererformat.md)
  A set of drawing attributes that represents the configuration of a graphics renderer context.
- [class UIGraphicsImageRenderer](uigraphicsimagerenderer.md)
  A graphics renderer for creating Core Graphics-backed images.
- [class UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md)
  A set of drawing attributes that represents the configuration of an image renderer context.
- [class UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)
  A graphics renderer for creating PDFs.
- [class UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)
  The drawing environment for a PDF renderer.
- [class UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)
  A set of drawing attributes that represents the configuration of a PDF renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderercontext)*