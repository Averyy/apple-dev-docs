# runDrawingActions(_:completionActions:)

**Framework**: UIKit  
**Kind**: method

Performs drawing actions on a Core Graphics context that the renderer prepares.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func runDrawingActions(_ drawingActions: (UIGraphicsRendererContext) -> Void, completionActions: ((UIGraphicsRendererContext) -> Void)? = nil) throws
```

#### Discussion

This method invokes the `drawingActions` block in a Core Graphics context. This context was created by the [`context(with:)`](uigraphicsrenderer/context(with:).md) method, captured in an instance of the class returned by the [`rendererContextClass()`](uigraphicsrenderer/renderercontextclass().md) method, and prepared by the [`prepare(_:with:)`](uigraphicsrenderer/prepare(_:with:).md) method.

Do not override this method. Instead, consider invoking it from a utility method in your subclass, as the [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md) and [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md) classes do.

## Parameters

- `drawingActions`: A   block that represents a set of drawing instructions that the renderer applies to the Core Graphics context.
- `completionActions`: A   block that the renderer calls after executing the   block.

## See Also

- [typealias UIGraphicsDrawingActions](uigraphicsdrawingactions.md)
  A closure that executes a set of drawing instructions that the renderer applies to the Core Graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/rundrawingactions(_:completionactions:))*