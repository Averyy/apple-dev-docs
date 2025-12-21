# Drawing

**Framework**: UIKit

Configure your app’s drawing environment using colors, renderers, draw paths, strings, and shadows.

## Topics

### UI updates
- [class UIUpdateLink](uiupdatelink.md)
  An object you use to observe, participate in, and affect the UI update process.
- [class UIUpdateInfo](uiupdateinfo.md)
  An object that contains detailed information about the current UI update state.
- [class UIUpdateActionPhase](uiupdateactionphase.md)
  An object that defines specific phases of the UI update process.
### Color
- [class UIColor](uicolor.md)
  An object that stores color data and sometimes opacity.
### Graphics contexts
- [class UIGraphicsRenderer](uigraphicsrenderer.md)
  An abstract base class for creating graphics renderers.
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
### Paths
- [class UIBezierPath](uibezierpath.md)
  A path that consists of straight and curved line segments that you can render in your custom views.
- [func UIRectFill(CGRect)](uirectfill(_:).md)
  Fills the specified rectangle with the current color.
- [func UIRectFillUsingBlendMode(CGRect, CGBlendMode)](uirectfillusingblendmode(_:_:).md)
  Fills a rectangle with the current fill color using the specified blend mode.
- [func UIRectFrame(CGRect)](uirectframe(_:).md)
  Draws a frame around the inside of the specified rectangle.
- [func UIRectFrameUsingBlendMode(CGRect, CGBlendMode)](uirectframeusingblendmode(_:_:).md)
  Draws a frame around the inside of a rectangle using the specified blend mode.
### Strings
- [class NSStringDrawingContext](nsstringdrawingcontext.md)
  An object that manages metrics for drawing attributed strings.
- [struct NSStringDrawingOptions](nsstringdrawingoptions.md)
  Constants that specify the rendering options for drawing a string.
- [enum UIBaselineAdjustment](uibaselineadjustment.md)
  Vertical adjustment options.
### Shadows
- [class NSShadow](nsshadow.md)
  An object you use to specify attributes to create and style a drop shadow during drawing operations.
### Graphics context primitives
- [func UIGraphicsGetCurrentContext() -> CGContext?](uigraphicsgetcurrentcontext().md)
  Returns the current graphics context.
- [func UIGraphicsPushContext(CGContext)](uigraphicspushcontext(_:).md)
  Makes the specified graphics context the current context.
- [func UIGraphicsPopContext()](uigraphicspopcontext().md)
  Removes the current graphics context from the top of the stack, restoring the previous context.
- [func UIGraphicsBeginImageContextWithOptions(CGSize, Bool, CGFloat)](uigraphicsbeginimagecontextwithoptions(_:_:_:).md)
  Creates a bitmap-based graphics context with the specified options.
- [func UIRectClip(CGRect)](uirectclip(_:).md)
  Modifies the current clipping path by intersecting it with the specified rectangle.
### Primitive type conversions
- [class func cgAffineTransform(for: String) -> CGAffineTransform](../Foundation/NSCoder/cgAffineTransform(for:).md)
  Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [class func cgPoint(for: String) -> CGPoint](../Foundation/NSCoder/cgPoint(for:).md)
  Returns a Core Graphics point structure corresponding to the data in a given string.
- [class func cgRect(for: String) -> CGRect](../Foundation/NSCoder/cgRect(for:).md)
  Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [class func cgSize(for: String) -> CGSize](../Foundation/NSCoder/cgSize(for:).md)
  Returns a Core Graphics size structure corresponding to the data in a given string.
- [class func cgVector(for: String) -> CGVector](../Foundation/NSCoder/cgVector(for:).md)
  Returns a Core Graphics vector corresponding to the data in a given string.
- [class func string(for: CGAffineTransform) -> String](../Foundation/NSCoder/string(for:)-6yx6n.md)
  Returns a string formatted to contain the data from an affine transform.
- [class func string(for: CGPoint) -> String](../Foundation/NSCoder/string(for:)-6ix86.md)
  Returns a string formatted to contain the data from a point.
- [class func string(for: CGRect) -> String](../Foundation/NSCoder/string(for:)-4qz0a.md)
  Returns a string formatted to contain the data from a rectangle.
- [class func string(for: CGSize) -> String](../Foundation/NSCoder/string(for:)-2f1xb.md)
  Returns a string formatted to contain the data from a size data structure.
- [class func string(for: CGVector) -> String](../Foundation/NSCoder/string(for:)-4omzv.md)
  Returns a string formatted to contain the data from a vector data structure.

## See Also

- [Images and PDF](images-and-pdf.md)
  Create and manage images, including those that use bitmap and PDF formats.
- [Printing](printing.md)
  Display the system print panels and manage the printing process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/drawing)*