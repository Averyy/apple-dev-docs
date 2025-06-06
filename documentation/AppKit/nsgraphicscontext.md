# NSGraphicsContext

**Framework**: AppKit  
**Kind**: class

An object that represents a graphics context.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSGraphicsContext
```

#### Overview

You can think of a graphics context as a destination to which drawing and graphics state operations are sent for execution. Each graphics context contains its own graphics environment and state.

The [`NSGraphicsContext`](nsgraphicscontext.md) class is an abstract superclass for destination-specific graphics contexts. You obtain instances of concrete subclasses with the class methods [`current`](nsgraphicscontext/current.md), [`init(attributes:)`](nsgraphicscontext/init(attributes:).md), [`init(bitmapImageRep:)`](nsgraphicscontext/init(bitmapimagerep:).md), [`init(cgContext:flipped:)`](nsgraphicscontext/init(cgcontext:flipped:).md), and [`init(window:)`](nsgraphicscontext/init(window:).md).

At any time there is the notion of the current context. The current context for the current thread may be set using [`current`](nsgraphicscontext/current.md).

Graphics contexts are maintained on a stack. You push a graphics context onto the stack by sending it a [`saveGraphicsState()`](nsgraphicscontext/savegraphicsstate()-swift.method.md) message, and pop it off the stack by sending it a [`restoreGraphicsState()`](nsgraphicscontext/restoregraphicsstate()-swift.method.md) message. By sending [`restoreGraphicsState()`](nsgraphicscontext/restoregraphicsstate()-swift.method.md) to a graphics context object you remove it from the stack, and the next graphics context on the stack becomes the current graphics context.

## Topics

### Creating a Graphics Context
- [init?(attributes: [NSGraphicsContext.AttributeKey : Any])](nsgraphicscontext/init(attributes:).md)
  Creates a graphics context using the specified attributes.
- [init?(bitmapImageRep: NSBitmapImageRep)](nsgraphicscontext/init(bitmapimagerep:).md)
  Creates a new graphics context using the specified bitmap image representation object as the context destination.
- [init(cgContext: CGContext, flipped: Bool)](nsgraphicscontext/init(cgcontext:flipped:).md)
  Creates a new graphics context from the specified Core Graphics context and the initial flipped state.
- [init(window: NSWindow)](nsgraphicscontext/init(window:).md)
  Creates a new graphics context for drawing into a window.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](nsgraphicscontext/init(graphicsport:flipped:).md)
  Creates a new graphics context from the specified graphics port.
### Managing the Current Context
- [class var current: NSGraphicsContext?](nsgraphicscontext/current.md)
  Returns the current graphics context of the current thread.
- [var cgContext: CGContext](nsgraphicscontext/cgcontext.md)
  The Core Graphics context, which is a low-level, platform-specific graphics context.
- [var graphicsPort: UnsafeMutableRawPointer](nsgraphicscontext/graphicsport.md)
  The low-level, platform-specific graphics context represented by the graphic port.
### Managing the Graphics State
- [class func restoreGraphicsState()](nsgraphicscontext/restoregraphicsstate-swift.type.method.md)
  Pops a graphics context from the per-thread stack, makes it current, and sends the context a restore graphics state message.
- [func restoreGraphicsState()](nsgraphicscontext/restoregraphicsstate-swift.method.md)
  Removes the context’s graphics state from the top of the graphics state stack and makes the next graphics state the current graphics state.
- [class func saveGraphicsState()](nsgraphicscontext/savegraphicsstate-swift.type.method.md)
  Saves the graphics state of the current graphics context.
- [func saveGraphicsState()](nsgraphicscontext/savegraphicsstate-swift.method.md)
  Saves the current graphics state and creates a new graphics state on the top of the stack.
- [class func setGraphicsState(Int)](nsgraphicscontext/setgraphicsstate(_:).md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.
### Testing the Drawing Destination
- [class func currentContextDrawingToScreen() -> Bool](nsgraphicscontext/currentcontextdrawingtoscreen.md)
  Returns a Boolean value that indicates whether the current context is drawing to the screen.
- [var isDrawingToScreen: Bool](nsgraphicscontext/isdrawingtoscreen.md)
  A Boolean value that indicates whether the drawing destination is the screen.
### Getting Information About the Context
- [var attributes: [NSGraphicsContext.AttributeKey : Any]?](nsgraphicscontext/attributes.md)
  The attributes used to create this instance.
- [NSGraphicsContext.AttributeKey](nsgraphicscontext/attributekey.md)
  Constants that specify the dictionary keys for the attributes of the graphics context.
- [NSGraphicsContext.RepresentationFormatName](nsgraphicscontext/representationformatname.md)
  Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.
- [var isFlipped: Bool](nsgraphicscontext/isflipped.md)
  A Boolean value that indicates the graphics context’s flipped state.
### Flushing Graphics to the Context
- [func flushGraphics()](nsgraphicscontext/flushgraphics.md)
  Forces any buffered operations or data to be sent to the graphics context’s destination.
### Configuring Rendering Options
- [var compositingOperation: NSCompositingOperation](nsgraphicscontext/compositingoperation.md)
  The graphics context’s global compositing operation setting.
- [enum NSCompositingOperation](nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.
- [var imageInterpolation: NSImageInterpolation](nsgraphicscontext/imageinterpolation.md)
  A constant that specifies the graphics context’s interpolation, or image smoothing, behavior.
- [enum NSImageInterpolation](nsimageinterpolation.md)
  Constants that specify the interpolation, or image smoothing, behavior used by the image interpolation property.
- [var shouldAntialias: Bool](nsgraphicscontext/shouldantialias.md)
  A Boolean value that indicates whether the graphics context uses antialiasing.
- [var patternPhase: NSPoint](nsgraphicscontext/patternphase.md)
  The amount to offset the pattern color when filling the graphics context.
### Getting the Context for Rendering Core Image Objects
- [var ciContext: CIContext?](nsgraphicscontext/cicontext.md)
  A context for Core Image objects that you can use to render into the graphics context.
### Managing Color Rendering
- [var colorRenderingIntent: NSColorRenderingIntent](nsgraphicscontext/colorrenderingintent.md)
  The color rendering intent in the graphics context’s graphics state.
- [enum NSColorRenderingIntent](nscolorrenderingintent.md)
  Constants that specify how Cocoa should handle colors that are not located within the destination color space of a graphics context.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext)*