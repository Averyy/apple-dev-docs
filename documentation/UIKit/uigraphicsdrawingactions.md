# UIGraphicsDrawingActions

**Framework**: UIKit  
**Kind**: typealias

A closure that executes a set of drawing instructions that the renderer applies to the Core Graphics context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias UIGraphicsDrawingActions = (UIGraphicsRendererContext) -> Void
```

#### Discussion

[`UIGraphicsDrawingActions`](uigraphicsdrawingactions.md) defines a block type that takes a [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) object as an argument and has no return value.

You provide a block of this type as an argument to the graphics drawing methods on [`UIGraphicsRenderer`](uigraphicsrenderer.md). Your block should use the provided renderer context to perform the drawing operations you want the renderer to execute.

## See Also

- [UIGraphicsImageRenderer.DrawingActions](uigraphicsimagerenderer/drawingactions.md)
  A closure for drawing an image.
- [UIGraphicsPDFRenderer.DrawingActions](uigraphicspdfrenderer/drawingactions.md)
  A closure for drawing PDF content.
- [func runDrawingActions((UIGraphicsRendererContext) -> Void, completionActions: ((UIGraphicsRendererContext) -> Void)?) throws](uigraphicsrenderer/rundrawingactions(_:completionactions:).md)
  Performs drawing actions on a Core Graphics context that the renderer prepares.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsdrawingactions)*