# UIGraphicsRenderer

**Framework**: UIKit  
**Kind**: class

An abstract base class for creating graphics renderers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsRenderer
```

#### Overview

Don’t use [`UIGraphicsRenderer`](uigraphicsrenderer.md) directly. Instead, either use one of the concrete subclasses ([`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md) or [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md)), or create your own subclass.

Graphics renderers provide memory-efficient management of Core Graphics contexts. Core Graphics contexts represent the drawing environment and backing store for 2D Graphics. As you reuse a graphics renderer, it in turn reuses Core Graphics contexts.

##### Subclassing Notes

You can’t use [`UIGraphicsRenderer`](uigraphicsrenderer.md) directly, but if the concrete subclasses ([`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md) and [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md)) don’t provide the functionality you require, you can create your own subclass.

Consider creating a subclass any time you need to create multiple Core Graphics contexts, each with the same dimensions and attributes, and one of the concrete subclasses ([`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md) or [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md)) doesn’t provide the functionality you require.

To create a subclass of [`UIGraphicsRenderer`](uigraphicsrenderer.md), first import the appropriate submodule or header, as shown in the following code.

A graphics renderer manages a pool of Core Graphics contexts that are reused with repeated uses of the renderer. The renderer creates these [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) objects using the [`context(with:)`](uigraphicsrenderer/context(with:).md) class method, and then wraps each of them in an instance of the class returned by the [`rendererContextClass()`](uigraphicsrenderer/renderercontextclass().md) class method. You must therefore override these two methods in your graphics renderer subclass.

To perform drawing actions on a Core Graphics context, call the [`runDrawingActions(_:completionActions:)`](uigraphicsrenderer/rundrawingactions(_:completionactions:).md) method, providing two blocks. Both of these blocks have a [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) argument, providing access to a Core Graphics context.

It is recommended that you create a public method on your renderer subclass that internally wraps the [`runDrawingActions(_:completionActions:)`](uigraphicsrenderer/rundrawingactions(_:completionactions:).md) method. This is how the rendering methods operate on the concrete subclasses, for example the [`image(actions:)`](uigraphicsimagerenderer/image(actions:).md) method on [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md).

Each time the [`runDrawingActions(_:completionActions:)`](uigraphicsrenderer/rundrawingactions(_:completionactions:).md) method is called, the renderer calls the [`prepare(_:with:)`](uigraphicsrenderer/prepare(_:with:).md) method with the [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) and [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) as arguments. Override the [`prepare(_:with:)`](uigraphicsrenderer/prepare(_:with:).md) method to apply the [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) configuration to the underlying [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) before the renderer invokes the drawing actions.

## Topics

### Initializing a graphics renderer
- [convenience init(bounds: CGRect)](uigraphicsrenderer/init(bounds:).md)
  Creates a new graphics renderer with the specified bounds and a default format.
- [init(bounds: CGRect, format: UIGraphicsRendererFormat)](uigraphicsrenderer/init(bounds:format:).md)
  Creates a new graphics renderer with the given bounds and format.
### Configuring the renderer
- [var allowsImageOutput: Bool](uigraphicsrenderer/allowsimageoutput.md)
  A Boolean value specifying whether the renderer can create output images.
- [var format: UIGraphicsRendererFormat](uigraphicsrenderer/format.md)
  The format used to create the graphics renderer.
### Running the drawing actions
- [func runDrawingActions((UIGraphicsRendererContext) -> Void, completionActions: ((UIGraphicsRendererContext) -> Void)?) throws](uigraphicsrenderer/rundrawingactions(_:completionactions:).md)
  Performs drawing actions on a Core Graphics context that the renderer prepares.
- [typealias UIGraphicsDrawingActions](uigraphicsdrawingactions.md)
  A closure that executes a set of drawing instructions that the renderer applies to the Core Graphics context.
### Managing graphics contexts
- [class func context(with: UIGraphicsRendererFormat) -> CGContext?](uigraphicsrenderer/context(with:).md)
  Creates a Core Graphics context configured according to the supplied format object.
- [class func prepare(CGContext, with: UIGraphicsRendererContext)](uigraphicsrenderer/prepare(_:with:).md)
  Applies the configuration specified in the renderer context to the Core Graphics context.
- [class func rendererContextClass() -> AnyClass](uigraphicsrenderer/renderercontextclass.md)
  Specifies the drawing context class used by this graphics renderer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md)
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIGraphicsRendererContext](uigraphicsrenderercontext.md)
  The base class for the drawing environments for graphics renderers.
- [class UIGraphicsRendererFormat](uigraphicsrendererformat.md)
  A set of drawing attributes that represents the configuration of a graphics renderer context.
- [class UIGraphicsImageRenderer](uigraphicsimagerenderer.md)
  A graphics renderer for creating Core Graphics-backed images.
- [class UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md)
  The drawing environment for an image renderer.
- [class UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md)
  A set of drawing attributes that represents the configuration of an image renderer context.
- [class UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)
  A graphics renderer for creating PDFs.
- [class UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)
  The drawing environment for a PDF renderer.
- [class UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)
  A set of drawing attributes that represents the configuration of a PDF renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer)*