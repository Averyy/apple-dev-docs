# UIGraphicsRendererFormat

**Framework**: UIKit  
**Kind**: class

A set of drawing attributes that represents the configuration of a graphics renderer context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsRendererFormat
```

#### Overview

Create a [`UIGraphicsRendererFormat`](uigraphicsrendererformat.md) object, or one of its subclasses ([`UIGraphicsImageRendererFormat`](uigraphicsimagerendererformat.md) and [`UIGraphicsPDFRendererFormat`](uigraphicspdfrendererformat.md)), and use it to construct a graphics renderer by providing the format object as a parameter in a [`UIGraphicsRenderer`](uigraphicsrenderer.md) subclass intializer.

The graphics renderer uses the format object you provided to configure any context objects ([`UIGraphicsRendererContext`](uigraphicsrenderercontext.md)) it creates as part of the rendering process.

If you use a graphics renderer initializer that doesn’t require a format argument, the renderer creates a format object using the [`default()`](uigraphicsrendererformat/default().md) class method.

The renderer format object contains properties that represent the immutable aspects of the renderer’s configuration. This means that repeated uses of a single graphics renderer object will always use the same format object.

## Topics

### Creating a format
- [class func `default`() -> Self](uigraphicsrendererformat/default.md)
  Returns a format that represents the highest fidelity that the current device supports.
- [class func preferred() -> Self](uigraphicsrendererformat/preferred.md)
  Returns the most suitable format for the main screen’s current configuration.
### Getting the bounds
- [var bounds: CGRect](uigraphicsrendererformat/bounds.md)
  The bounds of the graphics context.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md)
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIGraphicsRenderer](uigraphicsrenderer.md)
  An abstract base class for creating graphics renderers.
- [class UIGraphicsRendererContext](uigraphicsrenderercontext.md)
  The base class for the drawing environments for graphics renderers.
- [class UIGraphicsImageRenderer](uigraphicsimagerenderer.md)
  A graphics renderer for creating Core Graphics-backed images.
- [class UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md)
  The drawing environment for an image renderer.
- [class UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md)
  A set of drawing attributes that represents the configuration of an image renderer context.
- [class UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)
  A graphics renderer for creating PDFs.
- [class UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)
  The drawing environment for a PDF renderer.
- [class UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)
  A set of drawing attributes that represents the configuration of a PDF renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrendererformat)*