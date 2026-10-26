# Drawing

**Framework**: UIKit  
**Role**: API Collection

Configure your app’s drawing environment using colors, renderers, draw paths, strings, and shadows.

## Topics

### UI updates
- [class UIUpdateLink](./uiupdatelink.md)
  An object you use to observe, participate in, and affect the UI update process.
- [class UIUpdateInfo](./uiupdateinfo.md)
  An object that contains detailed information about the current UI update state.
- [class UIUpdateActionPhase](./uiupdateactionphase.md)
  An object that defines specific phases of the UI update process.
### Color
- [class UIColor](./uicolor.md)
  An object that stores color data and sometimes opacity.
### Graphics contexts
- [class UIGraphicsRenderer](./uigraphicsrenderer.md)
  An abstract base class for creating graphics renderers.
- [class UIGraphicsRendererContext](./uigraphicsrenderercontext.md)
  The base class for the drawing environments for graphics renderers.
- [class UIGraphicsRendererFormat](./uigraphicsrendererformat.md)
  A set of drawing attributes that represents the configuration of a graphics renderer context.
- [class UIGraphicsImageRenderer](./uigraphicsimagerenderer.md)
  A graphics renderer for creating Core Graphics-backed images.
- [class UIGraphicsImageRendererContext](./uigraphicsimagerenderercontext.md)
  The drawing environment for an image renderer.
- [class UIGraphicsImageRendererFormat](./uigraphicsimagerendererformat.md)
  A set of drawing attributes that represents the configuration of an image renderer context.
- [class UIGraphicsPDFRenderer](./uigraphicspdfrenderer.md)
  A graphics renderer for creating PDFs.
- [class UIGraphicsPDFRendererContext](./uigraphicspdfrenderercontext.md)
  The drawing environment for a PDF renderer.
- [class UIGraphicsPDFRendererFormat](./uigraphicspdfrendererformat.md)
  A set of drawing attributes that represents the configuration of a PDF renderer context.
### Paths
- [class UIBezierPath](./uibezierpath.md)
  A path that consists of straight and curved line segments that you can render in your custom views.
- [func UIRectFill(CGRect)](./uirectfill%28_%29.md)
  Fills the specified rectangle with the current color.
- [func UIRectFillUsingBlendMode(CGRect, CGBlendMode)](./uirectfillusingblendmode%28_,_%29.md)
  Fills a rectangle with the current fill color using the specified blend mode.
- [func UIRectFrame(CGRect)](./uirectframe%28_%29.md)
  Draws a frame around the inside of the specified rectangle.
- [func UIRectFrameUsingBlendMode(CGRect, CGBlendMode)](./uirectframeusingblendmode%28_,_%29.md)
  Draws a frame around the inside of a rectangle using the specified blend mode.
### Strings
- [class NSStringDrawingContext](./nsstringdrawingcontext.md)
  An object that manages metrics for drawing attributed strings.
- [struct NSStringDrawingOptions](./nsstringdrawingoptions.md)
  Constants that specify the rendering options for drawing a string.
- [enum UIBaselineAdjustment](./uibaselineadjustment.md)
  Vertical adjustment options.
### Shadows
- [class NSShadow](./nsshadow.md)
  An object you use to specify attributes to create and style a drop shadow during drawing operations.
### Graphics context primitives
- [func UIGraphicsGetCurrentContext() -> CGContext?](./uigraphicsgetcurrentcontext%28%29.md)
  Returns the current graphics context.
- [func UIGraphicsPushContext(CGContext)](./uigraphicspushcontext%28_%29.md)
  Makes the specified graphics context the current context.
- [func UIGraphicsPopContext()](./uigraphicspopcontext%28%29.md)
  Removes the current graphics context from the top of the stack, restoring the previous context.
- [func UIRectClip(CGRect)](./uirectclip%28_%29.md)
  Modifies the current clipping path by intersecting it with the specified rectangle.
### Primitive type conversions
- [class func cgAffineTransform(for: String) -> CGAffineTransform](../Foundation/nscoder/cgaffinetransform%28for%29.md)
  Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [class func cgPoint(for: String) -> CGPoint](../Foundation/nscoder/cgpoint%28for%29.md)
  Returns a Core Graphics point structure corresponding to the data in a given string.
- [class func cgRect(for: String) -> CGRect](../Foundation/nscoder/cgrect%28for%29.md)
  Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [class func cgSize(for: String) -> CGSize](../Foundation/nscoder/cgsize%28for%29.md)
  Returns a Core Graphics size structure corresponding to the data in a given string.
- [class func cgVector(for: String) -> CGVector](../Foundation/nscoder/cgvector%28for%29.md)
  Returns a Core Graphics vector corresponding to the data in a given string.
- [class func string(for: CGAffineTransform) -> String](../Foundation/nscoder/string%28for%29-6yx6n.md)
  Returns a string formatted to contain the data from an affine transform.
- [class func string(for: CGPoint) -> String](../Foundation/nscoder/string%28for%29-6ix86.md)
  Returns a string formatted to contain the data from a point.
- [class func string(for: CGRect) -> String](../Foundation/nscoder/string%28for%29-4qz0a.md)
  Returns a string formatted to contain the data from a rectangle.
- [class func string(for: CGSize) -> String](../Foundation/nscoder/string%28for%29-2f1xb.md)
  Returns a string formatted to contain the data from a size data structure.
- [class func string(for: CGVector) -> String](../Foundation/nscoder/string%28for%29-4omzv.md)
  Returns a string formatted to contain the data from a vector data structure.
- [CGAffineTransformFromString](./cgaffinetransformfromstring.md)
  Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGPointFromString](./cgpointfromstring.md)
  Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGRectFromString](./cgrectfromstring.md)
  Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [CGSizeFromString](./cgsizefromstring.md)
  Returns a Core Graphics size structure corresponding to the data in a given string.
- [CGVectorFromString](./cgvectorfromstring.md)
  Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](./nsstringfromcgaffinetransform.md)
  Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGPoint](./nsstringfromcgpoint.md)
  Returns a string formatted to contain the data from a point.
- [NSStringFromCGRect](./nsstringfromcgrect.md)
  Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](./nsstringfromcgsize.md)
  Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](./nsstringfromcgvector.md)
  Returns a string formatted to contain the data from a vector data structure.
### Deprecated
- [Deprecated symbols](./drawing-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## See Also

### Graphics, drawing, and printing
- [Images and PDF](./images-and-pdf.md)
  Create and manage images, including those that use bitmap and PDF formats.
- [Printing](./printing.md)
  Display the system print panels and manage the printing process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/drawing)*