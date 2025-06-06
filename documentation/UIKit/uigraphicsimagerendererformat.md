# UIGraphicsImageRendererFormat

**Framework**: UIKit  
**Kind**: class

A set of drawing attributes that represents the configuration of an image renderer context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsImageRendererFormat
```

#### Overview

Use an instance of [`UIGraphicsImageRendererFormat`](uigraphicsimagerendererformat.md) to initialize a [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md) object with nondefault attributes.

The image renderer format object contains properties that determine the attributes of the underlying Core Graphics contexts that the image renderer creates. Use the [`default()`](uigraphicsrendererformat/default().md) class method to create an image renderer format instance optimized for the current device.

## Topics

### Creating the renderer
- [convenience init(for: UITraitCollection)](uigraphicsimagerendererformat/init(for:).md)
  Creates the most suitable format for rendering on a device with the specified traits.
### Configuring the renderer attributes
- [var opaque: Bool](uigraphicsimagerendererformat/opaque.md)
  A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [var scale: CGFloat](uigraphicsimagerendererformat/scale.md)
  The display scale of the image renderer context.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/preferredrange.md)
  The preferred color range of the image renderer context.
- [UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/range.md)
  Constants that specify the color range of the image renderer context.
- [var prefersExtendedRange: Bool](uigraphicsimagerendererformat/prefersextendedrange.md)
  A Boolean value that specifies whether the bitmap context uses extended color.
### Instance Properties
- [var supportsHighDynamicRange: Bool](uigraphicsimagerendererformat/supportshighdynamicrange.md)

## Relationships

### Inherits From
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md)
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
- [class UIGraphicsRendererFormat](uigraphicsrendererformat.md)
  A set of drawing attributes that represents the configuration of a graphics renderer context.
- [class UIGraphicsImageRenderer](uigraphicsimagerenderer.md)
  A graphics renderer for creating Core Graphics-backed images.
- [class UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md)
  The drawing environment for an image renderer.
- [class UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)
  A graphics renderer for creating PDFs.
- [class UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)
  The drawing environment for a PDF renderer.
- [class UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)
  A set of drawing attributes that represents the configuration of a PDF renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat)*