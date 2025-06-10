# UIImage.RenderingMode

**Framework**: UIKit  
**Kind**: enum

Constants that specify the possible rendering modes for an image.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum RenderingMode
```

#### Overview

The rendering mode controls how UIKit uses color information to display an image. See [`Providing images for different appearances`](providing-images-for-different-appearances.md) for creating tintable images with template mode.

## Topics

### Rendering modes
- [UIImage.RenderingMode.automatic](uiimage/renderingmode-swift.enum/automatic.md)
  Draw the image using the context’s default rendering mode.
- [UIImage.RenderingMode.alwaysOriginal](uiimage/renderingmode-swift.enum/alwaysoriginal.md)
  Always draw the original image, without treating it as a template.
- [UIImage.RenderingMode.alwaysTemplate](uiimage/renderingmode-swift.enum/alwaystemplate.md)
  Always draw the image as a template image, ignoring its color information.
### Initializers
- [init?(rawValue: Int)](uiimage/renderingmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var renderingMode: UIImage.RenderingMode](uiimage/renderingmode-swift.property.md)
  A setting that determines how the app renders an image.
- [var imageRendererFormat: UIGraphicsImageRendererFormat](uiimage/imagerendererformat.md)
  The preferred image renderer format for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum)*