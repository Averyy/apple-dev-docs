# prepare(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Applies the configuration specified in the renderer context to the Core Graphics context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func prepare(_ context: CGContext, with rendererContext: UIGraphicsRendererContext)
```

```objc
+ (void) prepareCGContext:(CGContextRef) context withRendererContext:(UIGraphicsRendererContext *) rendererContext;
```

#### Discussion

The graphics renderer calls this method when the [`runDrawingActions(_:completionActions:)`](./rundrawingactions%28_,completionactions%29.md) method is invoked. Override this method in a subclass to configure the underlying Core Graphics context before the renderer begins renderering.

Core Graphics contexts are reused for repeated calls to the [`runDrawingActions(_:completionActions:)`](./rundrawingactions%28_,completionactions%29.md) method. Therefore, be sure to clean up the context to make it ready for reuse.

## Parameters

- `context`: The Core Graphics context that the graphics renderer performs drawing actions on.
- `rendererContext`: The renderer context object that is provided to the [`runDrawingActions(_:completionActions:)`](./rundrawingactions%28_,completionactions%29.md) method. This object is of the type returned by the [`rendererContextClass()`](./renderercontextclass%28%29.md) static method.

## See Also

### Managing graphics contexts
- [class func context(with: UIGraphicsRendererFormat) -> CGContext?](./context%28with%29.md)
  Creates a Core Graphics context configured according to the supplied format object.
- [class func rendererContextClass() -> AnyClass](./renderercontextclass%28%29.md)
  Specifies the drawing context class used by this graphics renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/prepare(_:with:))*