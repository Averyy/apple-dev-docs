# context(with:)

**Framework**: UIKit  
**Kind**: method

Creates a Core Graphics context configured according to the supplied format object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func context(with format: UIGraphicsRendererFormat) -> CGContext?
```

#### Return Value

A Core Graphics context configured to represent the attributes in the format object.

#### Discussion

Each time the graphics renderer needs to create a new Core Graphics context, it calls this method, providing the format object supplied at initialization time.

You must override this method when you subclass `UIGraphicsRenderer`. Use the provided [`UIGraphicsRendererFormat`](uigraphicsrendererformat.md) to create and configure a [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) object that is used by the renderer in the drawing routines.

## Parameters

- `format`: The format object that was either supplied to or created by the graphics renderer at initialization time.

## See Also

- [class func prepare(CGContext, with: UIGraphicsRendererContext)](uigraphicsrenderer/prepare(_:with:).md)
  Applies the configuration specified in the renderer context to the Core Graphics context.
- [class func rendererContextClass() -> AnyClass](uigraphicsrenderer/renderercontextclass.md)
  Specifies the drawing context class used by this graphics renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/context(with:))*