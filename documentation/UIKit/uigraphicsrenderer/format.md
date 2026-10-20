# format

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The format used to create the graphics renderer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var format: UIGraphicsRendererFormat { get }
```

```objc
@property (nonatomic, readonly) UIGraphicsRendererFormat * format;
```

#### Discussion

The property returns a copy of the [`UIGraphicsRendererFormat`](../uigraphicsrendererformat.md) instance used to create the graphics renderer.

## See Also

### Configuring the renderer
- [var allowsImageOutput: Bool](./allowsimageoutput.md)
  A Boolean value specifying whether the renderer can create output images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/format)*