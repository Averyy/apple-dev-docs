# format

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The format used to create the associated graphics renderer.

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

If you specified a format object when you initialized the current renderer ([`UIGraphicsRenderer`](../uigraphicsrenderer.md)) object, then this property provides access to that object. Otherwise, a default format object was created for you using the renderer initialization parameters, tuned to the current device.

## See Also

### Getting the drawing context
- [var cgContext: CGContext](./cgcontext.md)
  The underlying Core Graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/format)*