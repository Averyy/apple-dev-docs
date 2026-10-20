# renderingMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A setting that determines how the app renders an image.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var renderingMode: UIImage.RenderingMode { get }
```

```objc
@property (nonatomic, readonly) UIImageRenderingMode renderingMode;
```

#### Discussion

The default rendering mode is [`UIImage.RenderingMode.automatic`](./renderingmode-swift.enum/automatic.md).

## See Also

### Getting rendering information
- [UIImage.RenderingMode](./renderingmode-swift.enum.md)
  Constants that specify the possible rendering modes for an image.
- [var imageRendererFormat: UIGraphicsImageRendererFormat](./imagerendererformat.md)
  The preferred image renderer format for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.property)*