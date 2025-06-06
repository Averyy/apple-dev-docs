# prepare(_:with:)

**Framework**: UIKit  
**Kind**: method

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

#### Discussion

The graphics renderer calls this method when the [`runDrawingActions(_:completionActions:)`](uigraphicsrenderer/rundrawingactions(_:completionactions:).md) method is invoked. Override this method in a subclass to configure the underlying Core Graphics context before the renderer begins renderering.

Core Graphics contexts are reused for repeated calls to the [`runDrawingActions(_:completionActions:)`](uigraphicsrenderer/rundrawingactions(_:completionactions:).md) method. Therefore, be sure to clean up the context to make it ready for reuse.

## Parameters

- `context`: The Core Graphics context that the graphics renderer performs drawing actions on.
- `rendererContext`: The renderer context object that is provided to the   method. This object is of the type returned by the   static method.

## See Also

- [class func context(with: UIGraphicsRendererFormat) -> CGContext?](uigraphicsrenderer/context(with:).md)
  Creates a Core Graphics context configured according to the supplied format object.
- [class func rendererContextClass() -> AnyClass](uigraphicsrenderer/renderercontextclass.md)
  Specifies the drawing context class used by this graphics renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/prepare(_:with:))*