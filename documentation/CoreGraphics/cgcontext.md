# CGContext

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A Quartz 2D drawing environment.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CGContext
```

```c
typedef struct CGContext * CGContextRef;
```

#### Overview

A `CGContext` instance represents a Quartz 2D drawing destination. A graphics context contains drawing parameters and all device-specific information needed to render the paint on a page to the destination, whether the destination is a window in an application, a bitmap image, a PDF document, or a printer.

## Topics

### Creating Bitmap Graphics Contexts
- [typealias CGBitmapContextReleaseDataCallback](./cgbitmapcontextreleasedatacallback.md)
  A callback function used to release data associate with the bitmap context.
### Creating PDF Graphics Contexts
- [init?(CFURL, mediaBox: UnsafePointer<CGRect>?, CFDictionary?)](./cgcontext/init%28_,mediabox,_%29.md)
  Creates a URL-based PDF graphics context.
- [init?(consumer: CGDataConsumer, mediaBox: UnsafePointer<CGRect>?, CFDictionary?)](./cgcontext/init%28consumer,mediabox,_%29.md)
  Creates a PDF graphics context.
- [Auxiliary Dictionary Keys](./auxiliary-dictionary-keys.md)
  Keys for the auxiliary info dictionary you specify when creating a PDF context.
### Converting Between Coordinate Spaces
- [var userSpaceToDeviceSpaceTransform: CGAffineTransform](./cgcontext/userspacetodevicespacetransform.md)
  Returns an affine transform that maps user space coordinates to device space coordinates.
- [func convertToDeviceSpace(CGPoint) -> CGPoint](./cgcontext/converttodevicespace%28_%29-53m7u.md)
  Returns a point that is transformed from user space coordinates to device space coordinates.
- [func convertToUserSpace(CGPoint) -> CGPoint](./cgcontext/converttouserspace%28_%29-3mtg3.md)
  Returns a point that is transformed from device space coordinates to user space coordinates.
- [func convertToDeviceSpace(CGRect) -> CGRect](./cgcontext/converttodevicespace%28_%29-91x5g.md)
  Returns a rectangle that is transformed from user space coordinate to device space coordinates.
- [func convertToUserSpace(CGRect) -> CGRect](./cgcontext/converttouserspace%28_%29-1hk5r.md)
  Returns a rectangle that is transformed from device space coordinate to user space coordinates.
- [func convertToDeviceSpace(CGSize) -> CGSize](./cgcontext/converttodevicespace%28_%29-224h2.md)
  Returns a size that is transformed from user space coordinates to device space coordinates.
- [func convertToUserSpace(CGSize) -> CGSize](./cgcontext/converttouserspace%28_%29-693ur.md)
  Returns a size that is transformed from device space coordinates to user space coordinates.
### Constructing a Current Graphics Path
- [func beginPath()](./cgcontext/beginpath%28%29.md)
  Creates a new empty path in a graphics context.
- [func move(to: CGPoint)](./cgcontext/move%28to%29.md)
  Begins a new subpath at the specified point.
- [func addLine(to: CGPoint)](./cgcontext/addline%28to%29.md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines(between: [CGPoint])](./cgcontext/addlines%28between%29.md)
  Adds a sequence of connected straight-line segments to the current path.
- [func addRect(CGRect)](./cgcontext/addrect%28_%29.md)
  Adds a rectangular path to the current path.
- [func addRects([CGRect])](./cgcontext/addrects%28_%29.md)
  Adds a set of rectangular paths to the current path.
- [func addEllipse(in: CGRect)](./cgcontext/addellipse%28in%29.md)
  Adds an ellipse that fits inside the specified rectangle.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./cgcontext/addarc%28center,radius,startangle,endangle,clockwise%29.md)
  Adds an arc of a circle to the current path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat)](./cgcontext/addarc%28tangent1end,tangent2end,radius%29.md)
  Adds an arc of a circle to the current path, specified with a radius and two tangent lines.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)](./cgcontext/addcurve%28to,control1,control2%29.md)
  Adds a cubic Bézier curve to the current path, with the specified end point and control points.
- [func addQuadCurve(to: CGPoint, control: CGPoint)](./cgcontext/addquadcurve%28to,control%29.md)
  Adds a quadratic Bézier curve to the current path, with the specified end point and control point.
- [func addPath(CGPath)](./cgcontext/addpath%28_%29.md)
  Adds a previously created path object to the current path in a graphics context.
- [func closePath()](./cgcontext/closepath%28%29.md)
  Closes and terminates the current path’s subpath.
- [var path: CGPath?](./cgcontext/path.md)
  Returns a path object built from the current path information in a graphics context.
- [func replacePathWithStrokedPath()](./cgcontext/replacepathwithstrokedpath%28%29.md)
  Replaces the path in the graphics context with the stroked version of the path.
### Examining the Current Graphics Path
- [var boundingBoxOfPath: CGRect](./cgcontext/boundingboxofpath.md)
  Returns the smallest rectangle that contains the current path.
- [var currentPointOfPath: CGPoint](./cgcontext/currentpointofpath.md)
  Returns the current point in a non-empty path.
- [var isPathEmpty: Bool](./cgcontext/ispathempty.md)
  Indicates whether the current path contains any subpaths.
- [func pathContains(CGPoint, mode: CGPathDrawingMode) -> Bool](./cgcontext/pathcontains%28_,mode%29.md)
  Checks to see whether the specified point is contained in the current path.
### Drawing the Current Graphics Path
- [func drawPath(using: CGPathDrawingMode)](./cgcontext/drawpath%28using%29.md)
  Draws the current path using the provided drawing mode.
- [enum CGPathDrawingMode](./cgpathdrawingmode.md)
  Options for rendering a path.
- [func fillPath(using: CGPathFillRule)](./cgcontext/fillpath%28using%29.md)
  Paints the area within the current path, as determined by the specified fill rule.
- [func strokePath()](./cgcontext/strokepath%28%29.md)
  Paints a line along the current path.
### Drawing Shapes
- [func clear(CGRect)](./cgcontext/clear%28_%29.md)
  Paints a transparent rectangle.
- [func fill(CGRect)](./cgcontext/fill%28_%29-7a0rk.md)
  Paints the area contained within the provided rectangle, using the fill color in the current graphics state.
- [func fill([CGRect])](./cgcontext/fill%28_%29-6jc4y.md)
  Paints the areas contained within the provided rectangles, using the fill color in the current graphics state.
- [func fillEllipse(in: CGRect)](./cgcontext/fillellipse%28in%29.md)
  Paints the area of the ellipse that fits inside the provided rectangle, using the fill color in the current graphics state.
- [func stroke(CGRect)](./cgcontext/stroke%28_%29.md)
  Paints a rectangular path.
- [func stroke(CGRect, width: CGFloat)](./cgcontext/stroke%28_,width%29.md)
  Paints a rectangular path, using the specified line width.
- [func strokeEllipse(in: CGRect)](./cgcontext/strokeellipse%28in%29.md)
  Strokes an ellipse that fits inside the specified rectangle.
- [func strokeLineSegments(between: [CGPoint])](./cgcontext/strokelinesegments%28between%29.md)
  Strokes a sequence of line segments.
### Drawing Images and PDF Content
- [func draw(CGImage, in: CGRect, byTiling: Bool)](./cgcontext/draw%28_,in,bytiling%29.md)
  Draws an image in the specified area.
- [func drawPDFPage(CGPDFPage)](./cgcontext/drawpdfpage%28_%29.md)
  Draws the content of a PDF page into the current graphics context.
- [var interpolationQuality: CGInterpolationQuality](./cgcontext/interpolationquality.md)
  Returns the current level of interpolation quality for a graphics context.
- [enum CGInterpolationQuality](./cginterpolationquality.md)
  Levels of interpolation quality for rendering an image.
### Drawing Gradients and Shadings
- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](./cgcontext/drawlineargradient%28_,start,end,options%29.md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](./cgcontext/drawradialgradient%28_,startcenter,startradius,endcenter,endradius,options%29.md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [struct CGGradientDrawingOptions](./cggradientdrawingoptions.md)
  Drawing locations for gradients.
- [func drawShading(CGShading)](./cgcontext/drawshading%28_%29.md)
  Fills the clipping path of a context with the specified shading.
### Drawing Text
- [var textMatrix: CGAffineTransform](./cgcontext/textmatrix.md)
  Returns the current text matrix.
- [var textPosition: CGPoint](./cgcontext/textposition.md)
- [func selectFont(name: UnsafePointer<CChar>, size: CGFloat, textEncoding: CGTextEncoding)](./cgcontext/selectfont%28name,size,textencoding%29.md)
  Sets the font and font size in a graphics context.
- [func setCharacterSpacing(CGFloat)](./cgcontext/setcharacterspacing%28_%29.md)
  Sets the current character spacing.
- [func setFont(CGFont)](./cgcontext/setfont%28_%29.md)
  Sets the platform font in a graphics context.
- [func setFontSize(CGFloat)](./cgcontext/setfontsize%28_%29.md)
  Sets the current font size.
- [func setTextDrawingMode(CGTextDrawingMode)](./cgcontext/settextdrawingmode%28_%29.md)
  Sets the current text drawing mode.
- [func setAllowsFontSmoothing(Bool)](./cgcontext/setallowsfontsmoothing%28_%29.md)
  Sets whether or not to allow font smoothing for a graphics context.
- [func setAllowsFontSubpixelPositioning(Bool)](./cgcontext/setallowsfontsubpixelpositioning%28_%29.md)
  Sets whether or not to allow subpixel positioning for a graphics context.
- [func setAllowsFontSubpixelQuantization(Bool)](./cgcontext/setallowsfontsubpixelquantization%28_%29.md)
  Sets whether or not to allow subpixel quantization for a graphics context.
- [func setShouldSmoothFonts(Bool)](./cgcontext/setshouldsmoothfonts%28_%29.md)
  Enables or disables font smoothing in a graphics context.
- [func setShouldSubpixelPositionFonts(Bool)](./cgcontext/setshouldsubpixelpositionfonts%28_%29.md)
  Enables or disables subpixel positioning in a graphics context.
- [func setShouldSubpixelQuantizeFonts(Bool)](./cgcontext/setshouldsubpixelquantizefonts%28_%29.md)
  Enables or disables subpixel quantization in a graphics context.
- [func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)](./cgcontext/showglyphs%28g,count%29.md)
  Displays an array of glyphs at the current text position.
- [func showGlyphs([CGGlyph], at: [CGPoint])](./cgcontext/showglyphs%28_,at%29.md)
  Draws a set of glyphs at a set of corresponding positions.
- [func showGlyphsAtPoint(x: CGFloat, y: CGFloat, glyphs: UnsafePointer<CGGlyph>?, count: Int)](./cgcontext/showglyphsatpoint%28x,y,glyphs,count%29.md)
  Displays an array of glyphs at a position you specify.
- [func showGlyphsWithAdvances(glyphs: UnsafePointer<CGGlyph>?, advances: UnsafePointer<CGSize>?, count: Int)](./cgcontext/showglyphswithadvances%28glyphs,advances,count%29.md)
  Draws an array of glyphs with varying offsets.
- [func showText(string: UnsafePointer<CChar>, length: Int)](./cgcontext/showtext%28string,length%29.md)
  Displays a character array at the current text position, a point specified by the current text matrix.
- [func showTextAtPoint(x: CGFloat, y: CGFloat, string: UnsafePointer<CChar>, length: Int)](./cgcontext/showtextatpoint%28x,y,string,length%29.md)
  Displays a character string at a position you specify.
- [enum CGTextDrawingMode](./cgtextdrawingmode.md)
  Modes for rendering text.
### Drawing Core Graphics Layers
- [func draw(CGLayer, at: CGPoint)](./cgcontext/draw%28_,at%29.md)
  Draws the contents of a layer object at the specified point.
- [func draw(CGLayer, in: CGRect)](./cgcontext/draw%28_,in%29.md)
  Draws the contents of a layer object into the specified rectangle.
### Setting Fill, Stroke, and Shadow Colors
- [func setFillColor(CGColor)](./cgcontext/setfillcolor%28_%29-8lhn8.md)
  Sets the current fill color in a graphics context, using a CGColor.
- [func setFillColor(UnsafePointer<CGFloat>)](./cgcontext/setfillcolor%28_%29-756dy.md)
  Sets the current fill color.
- [func setFillColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](./cgcontext/setfillcolor%28cyan,magenta,yellow,black,alpha%29.md)
  Sets the current fill color to a value in the DeviceCMYK color space.
- [func setFillColor(gray: CGFloat, alpha: CGFloat)](./cgcontext/setfillcolor%28gray,alpha%29.md)
  Sets the current fill color to a value in the DeviceGray color space.
- [func setFillColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./cgcontext/setfillcolor%28red,green,blue,alpha%29.md)
  Sets the current fill color to a value in the DeviceRGB color space.
- [func setFillColorSpace(CGColorSpace)](./cgcontext/setfillcolorspace%28_%29.md)
  Sets the fill color space in a graphics context.
- [func setShadow(offset: CGSize, blur: CGFloat)](./cgcontext/setshadow%28offset,blur%29.md)
  Enables shadowing in a graphics context.
- [func setShadow(offset: CGSize, blur: CGFloat, color: CGColor?)](./cgcontext/setshadow%28offset,blur,color%29.md)
  Enables shadowing with color a graphics context.
- [func setStrokeColor(CGColor)](./cgcontext/setstrokecolor%28_%29-1sskg.md)
  Sets the current stroke color in a context, using a CGColor.
- [func setStrokeColor(UnsafePointer<CGFloat>)](./cgcontext/setstrokecolor%28_%29-4pd8p.md)
  Sets the current stroke color.
- [func setStrokeColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](./cgcontext/setstrokecolor%28cyan,magenta,yellow,black,alpha%29.md)
  Sets the current stroke color to a value in the DeviceCMYK color space.
- [func setStrokeColor(gray: CGFloat, alpha: CGFloat)](./cgcontext/setstrokecolor%28gray,alpha%29.md)
  Sets the current stroke color to a value in the DeviceGray color space.
- [func setStrokeColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./cgcontext/setstrokecolor%28red,green,blue,alpha%29.md)
  Sets the current stroke color to a value in the DeviceRGB color space.
- [func setStrokeColorSpace(CGColorSpace)](./cgcontext/setstrokecolorspace%28_%29.md)
  Sets the stroke color space in a graphics context.
- [func setStrokePattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](./cgcontext/setstrokepattern%28_,colorcomponents%29.md)
  Sets the stroke pattern in the specified graphics context.
- [func setAlpha(CGFloat)](./cgcontext/setalpha%28_%29.md)
  Sets the opacity level for objects drawn in a graphics context.
### Working with the Current Clipping Path
- [func clip(using: CGPathFillRule)](./cgcontext/clip%28using%29.md)
  Modifies the current clipping path.
- [func clip(to: CGRect)](./cgcontext/clip%28to%29-7cbwq.md)
  Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [func clip(to: [CGRect])](./cgcontext/clip%28to%29-2eg0.md)
  Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [func clip(to: CGRect, mask: CGImage)](./cgcontext/clip%28to,mask%29.md)
  Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.
- [var boundingBoxOfClipPath: CGRect](./cgcontext/boundingboxofclippath.md)
  Returns the bounding box of a clipping path.
### Working with Transparency Layers
- [func beginTransparencyLayer(in: CGRect, auxiliaryInfo: CFDictionary?)](./cgcontext/begintransparencylayer%28in,auxiliaryinfo%29.md)
  Begins a transparency layer whose contents are bounded by the specified rectangle.
- [func beginTransparencyLayer(auxiliaryInfo: CFDictionary?)](./cgcontext/begintransparencylayer%28auxiliaryinfo%29.md)
  Begins a transparency layer.
- [func endTransparencyLayer()](./cgcontext/endtransparencylayer%28%29.md)
  Ends a transparency layer.
### Working with the Current Transformation Matrix
- [var ctm: CGAffineTransform](./cgcontext/ctm.md)
  Returns the current transformation matrix.
- [func rotate(by: CGFloat)](./cgcontext/rotate%28by%29.md)
  Rotates the user coordinate system in a context.
- [func scaleBy(x: CGFloat, y: CGFloat)](./cgcontext/scaleby%28x,y%29.md)
  Changes the scale of the user coordinate system in a context.
- [func translateBy(x: CGFloat, y: CGFloat)](./cgcontext/translateby%28x,y%29.md)
  Changes the origin of the user coordinate system in a context.
- [func concatenate(CGAffineTransform)](./cgcontext/concatenate%28_%29.md)
  Transforms the user coordinate system in a context using a specified matrix.
### Setting Path Drawing Options
- [func setAllowsAntialiasing(Bool)](./cgcontext/setallowsantialiasing%28_%29.md)
  Sets whether or not to allow antialiasing for a graphics context.
- [func setFlatness(CGFloat)](./cgcontext/setflatness%28_%29.md)
  Sets the accuracy of curved paths in a graphics context.
- [func setLineCap(CGLineCap)](./cgcontext/setlinecap%28_%29.md)
  Sets the style for the endpoints of lines drawn in a graphics context.
- [func setLineDash(phase: CGFloat, lengths: [CGFloat])](./cgcontext/setlinedash%28phase,lengths%29.md)
  Sets the pattern for drawing dashed lines.
- [func setLineJoin(CGLineJoin)](./cgcontext/setlinejoin%28_%29.md)
  Sets the style for the joins of connected lines in a graphics context.
- [func setLineWidth(CGFloat)](./cgcontext/setlinewidth%28_%29.md)
  Sets the line width for a graphics context.
- [func setMiterLimit(CGFloat)](./cgcontext/setmiterlimit%28_%29.md)
  Sets the miter limit for the joins of connected lines in a graphics context.
- [func setPatternPhase(CGSize)](./cgcontext/setpatternphase%28_%29.md)
  Sets the pattern phase of a context.
- [func setFillPattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](./cgcontext/setfillpattern%28_,colorcomponents%29.md)
  Sets the fill pattern in the specified graphics context.
- [func setShouldAntialias(Bool)](./cgcontext/setshouldantialias%28_%29.md)
  Sets antialiasing on or off for a graphics context.
### Saving and Restoring Graphics State
- [func saveGState()](./cgcontext/savegstate%28%29.md)
  Pushes a copy of the current graphics state onto the graphics state stack for the context.
- [func restoreGState()](./cgcontext/restoregstate%28%29.md)
  Sets the current graphics state to the state most recently saved.
### Managing a Graphics Context
- [func flush()](./cgcontext/flush%28%29.md)
  Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [func synchronize()](./cgcontext/synchronize%28%29.md)
  Marks a window context for update.
- [func setBlendMode(CGBlendMode)](./cgcontext/setblendmode%28_%29.md)
  Sets how sample values are composited by a graphics context.
- [enum CGBlendMode](./cgblendmode.md)
  Compositing operations for images.
- [func setRenderingIntent(CGColorRenderingIntent)](./cgcontext/setrenderingintent%28_%29.md)
  Sets the rendering intent in the current graphics state.
### Managing a Bitmap Graphics Context
- [var bitmapInfo: CGBitmapInfo](./cgcontext/bitmapinfo.md)
  Obtains the bitmap information associated with a bitmap graphics context.
- [var alphaInfo: CGImageAlphaInfo](./cgcontext/alphainfo.md)
  Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.
- [var bitsPerComponent: Int](./cgcontext/bitspercomponent.md)
  Returns the bits per component of a bitmap context.
- [var bitsPerPixel: Int](./cgcontext/bitsperpixel.md)
  Returns the bits per pixel of a bitmap context.
- [var bytesPerRow: Int](./cgcontext/bytesperrow.md)
  Returns the bytes per row of a bitmap context.
- [var colorSpace: CGColorSpace?](./cgcontext/colorspace.md)
  Returns the color space of a bitmap context.
- [var data: UnsafeMutableRawPointer?](./cgcontext/data.md)
  Returns a pointer to the image data associated with a bitmap context.
- [var height: Int](./cgcontext/height.md)
  Returns the height in pixels of a bitmap context.
- [var width: Int](./cgcontext/width.md)
  Returns the width in pixels of a bitmap context.
- [func makeImage() -> CGImage?](./cgcontext/makeimage%28%29.md)
  Creates and returns a CGImage from the pixel data in a bitmap graphics context.
### Managing a PDF Graphics Context
- [func beginPDFPage(CFDictionary?)](./cgcontext/beginpdfpage%28_%29.md)
  Begins a new page in a PDF graphics context.
- [func endPDFPage()](./cgcontext/endpdfpage%28%29.md)
  Ends the current page in the PDF graphics context.
- [func addDestination(CFString, at: CGPoint)](./cgcontext/adddestination%28_,at%29.md)
  Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [func setDestination(CFString, for: CGRect)](./cgcontext/setdestination%28_,for%29.md)
  Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [func setURL(CFURL, for: CGRect)](./cgcontext/seturl%28_,for%29.md)
  Sets the URL associated with a rectangle in a PDF graphics context.
- [func addDocumentMetadata(CFData?)](./cgcontext/adddocumentmetadata%28_%29.md)
  Associates custom metadata with the PDF document.
- [func closePDF()](./cgcontext/closepdf%28%29.md)
  Closes a PDF document.
### Managing a Page-Based Graphics Context
- [func beginPage(mediaBox: UnsafePointer<CGRect>?)](./cgcontext/beginpage%28mediabox%29.md)
  Starts a new page in a page-based graphics context.
- [func endPage()](./cgcontext/endpage%28%29.md)
  Ends the current page in a page-based graphics context.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgcontext/typeid.md)
  Returns the type identifier for a graphics context.
### Constants
- [enum CGPathFillRule](./cgpathfillrule.md)
  Rules for determining which regions are interior to a path, used by the [`fillPath(using:)`](./cgcontext/fillpath%28using%29.md) and [`clip(using:)`](./cgcontext/clip%28using%29.md) methods.
- [enum CGTextEncoding](./cgtextencoding.md)
  Text encodings for fonts.
### Instance Methods
- [func draw(CGImage, in: CGRect, by: CGToneMapping, options: CFDictionary?) -> Bool](./cgcontext/draw%28_,in,by,options%29.md)
- [func resetClip()](./cgcontext/resetclip%28%29.md)
- [func setEDRTargetHeadroom(Float) -> Bool](./cgcontext/setedrtargetheadroom%28_%29.md)
- [func addStructureTreeRootChild(CGPDFStructureElement) -> OSStatus](./cgcontext/addstructuretreerootchild%28_%29.md)
- [func beginMarkedContentSequence(CGPDFTagType) -> CGPDFMarkedContentItem?](./cgcontext/beginmarkedcontentsequence%28_%29.md)
- [func beginNonStructuralMarkedContentSequence(CGPDFTagType)](./cgcontext/beginnonstructuralmarkedcontentsequence%28_%29.md)
- [func beginObjectReference() -> CGPDFMarkedContentItem?](./cgcontext/beginobjectreference%28%29.md)
- [func endMarkedContentSequence()](./cgcontext/endmarkedcontentsequence%28%29.md)
- [func endObjectReference()](./cgcontext/endobjectreference%28%29.md)
- [func synchronizeAttributes()](./cgcontext/synchronizeattributes%28%29.md)
### Structures
- [CGContext.AuxiliaryInfo](./cgcontext/auxiliaryinfo.md)
### Initializers
- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace?, bitmapInfo: CGBitmapInfo)](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo%29-10b3i.md)
- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32)](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo%29-4fkaf.md)
- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace?, bitmapInfo: CGBitmapInfo, releaseCallback: CGBitmapContextReleaseDataCallback?, releaseInfo: UnsafeMutableRawPointer?)](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo,releasecallback,releaseinfo%29-4yzt5.md)
- [init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32, releaseCallback: CGBitmapContextReleaseDataCallback?, releaseInfo: UnsafeMutableRawPointer?)](./cgcontext/init%28data,width,height,bitspercomponent,bytesperrow,space,bitmapinfo,releasecallback,releaseinfo%29-71ea9.md)
### Instance Properties
- [var contentToneMappingInfo: CGContentToneMappingInfo](./cgcontext/contenttonemappinginfo.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
### 2D Drawing
- [class CGImage](./cgimage.md)
  A bitmap image or image mask.
- [class CGPath](./cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGMutablePath](./cgmutablepath.md)
  A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGLayer](./cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext)*