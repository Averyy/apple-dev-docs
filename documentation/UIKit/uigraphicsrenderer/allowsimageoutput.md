# allowsImageOutput

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value specifying whether the renderer can create output images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var allowsImageOutput: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL allowsImageOutput;
```

## Discussion

If [`true`](../../Swift/true.md), this renderer can be used to generate [`CGImage`](../../CoreGraphics/cgimage.md) objects.

## See Also

### Configuring the renderer
- [var format: UIGraphicsRendererFormat](./format.md)
  The format used to create the graphics renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/allowsimageoutput)*