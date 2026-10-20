# UIImage.RenderingMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the possible rendering modes for an image.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum RenderingMode
```

```c
enum UIImageRenderingMode : NSInteger;
```

#### Overview

The rendering mode controls how UIKit uses color information to display an image. See [Providing images for different appearances](../providing-images-for-different-appearances.md) for creating tintable images with template mode.

## Topics

### Rendering modes
- [UIImage.RenderingMode.automatic](./renderingmode-swift.enum/automatic.md)
  Draw the image using the context’s default rendering mode.
- [UIImage.RenderingMode.alwaysOriginal](./renderingmode-swift.enum/alwaysoriginal.md)
  Always draw the original image, without treating it as a template.
- [UIImage.RenderingMode.alwaysTemplate](./renderingmode-swift.enum/alwaystemplate.md)
  Always draw the image as a template image, ignoring its color information.
### Initializers
- [init?(rawValue: Int)](./renderingmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting rendering information
- [var renderingMode: UIImage.RenderingMode](./renderingmode-swift.property.md)
  A setting that determines how the app renders an image.
- [var imageRendererFormat: UIGraphicsImageRendererFormat](./imagerendererformat.md)
  The preferred image renderer format for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum)*