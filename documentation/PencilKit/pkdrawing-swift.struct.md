# PKDrawing

**Framework**: PencilKit  
**Kind**: struct  
**Role**: Structure

A structure representing the drawing information captured by a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct PKDrawing
```

## Mentions

- [Supporting backward compatibility for ink types](./supporting-backward-compatibility-for-ink-types.md)
- [Recognizing handwriting and converting it to text](./recognizing-handwriting-and-converting-to-text.md)
- [Importing Bézier path data into PencilKit](./importing-external-drawing-data-into-pencilkit.md)

#### Overview

A [`PKDrawing`](./pkdrawing-swift.struct.md) object stores the user-drawn content from a [`PKCanvasView`](./pkcanvasview.md) object. You use drawing objects to store the data associated with your user’s drawings. You can save this data with the rest of your app’s content, and you can use that saved data to create a new drawing object later. You can also generate an image based on the drawn content that you can copy to the pasteboard, save to disk, or share.

## Topics

### Creating a drawing object
- [init<S>(strokes: S)](./pkdrawing-swift.struct/init%28strokes%29.md)
  Creates a drawing object and populates it with a sequence of strokes the user provides.
- [init(data: Data) throws](./pkdrawing-swift.struct/init%28data%29.md)
  Creates a drawing object and populates it with previously drawn content.
- [init()](./pkdrawing-swift.struct/init%28%29.md)
  Creates an empty drawing object.
### Getting the canvas bounds
- [var bounds: CGRect](./pkdrawing-swift.struct/bounds.md)
  The smallest rectangle used to represent the content’s bounds, taking into account line widths of that content.
### Generating an image
- [func image(from: CGRect, scale: CGFloat) -> UIImage](./pkdrawing-swift.struct/image%28from,scale%29-220d0.md)
  Returns an image object that contains the specified portion of the drawing.
- [func image(from: CGRect, scale: CGFloat) -> NSImage](./pkdrawing-swift.struct/image%28from,scale%29-6p3zc.md)
  Returns an image object that contains the specified portion of the drawing.
### Getting the drawing data
- [var strokes: [PKStroke]](./pkdrawing-swift.struct/strokes.md)
  The array of strokes that make up the drawing.
- [func dataRepresentation() -> Data](./pkdrawing-swift.struct/datarepresentation%28%29.md)
  Returns a raw data representation of the rendered content.
- [let PKAppleDrawingTypeIdentifier: CFString](./pkappledrawingtypeidentifier.md)
  The uniform type identifier for data associated with a drawing object.
### Modifying the drawing
- [func transform(using: CGAffineTransform)](./pkdrawing-swift.struct/transform%28using%29.md)
  Applies the specified transform to the contents of this drawing.
- [func transformed(using: CGAffineTransform) -> PKDrawing](./pkdrawing-swift.struct/transformed%28using%29.md)
  Applies the specified transform and returns a new drawing.
- [func append(PKDrawing)](./pkdrawing-swift.struct/append%28_%29.md)
  Appends the contents of the specified drawing object to an existing drawing object that you provide.
- [func appending(PKDrawing) -> PKDrawing](./pkdrawing-swift.struct/appending%28_%29.md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](./pkdrawing-swift.struct/requiredcontentversion.md)
  The version of PencilKit necessary to use the drawing.
### Using reference types
- [class PKDrawingReference](./pkdrawingreference.md)
  A data structure that contains the drawing information captured by a canvas view.
### Instance Methods
- [func draw(in: CGContext, frame: CGRect, from: CGRect, darkUserInterfaceStyle: Bool) async](./pkdrawing-swift.struct/draw%28in,frame,from,darkuserinterfacestyle%29.md)
  Draws the drawing in the specified rectangle.
- [func erasePath(PKStrokePath, mask: NSBezierPath?, transform: CGAffineTransform)](./pkdrawing-swift.struct/erasepath%28_,mask,transform%29-2b2u3.md)
- [func erasePath(PKStrokePath, mask: UIBezierPath?, transform: CGAffineTransform)](./pkdrawing-swift.struct/erasepath%28_,mask,transform%29-shn.md)
- [func erasingPath(PKStrokePath, mask: NSBezierPath?, transform: CGAffineTransform) -> PKDrawing](./pkdrawing-swift.struct/erasingpath%28_,mask,transform%29-2txi7.md)
- [func erasingPath(PKStrokePath, mask: UIBezierPath?, transform: CGAffineTransform) -> PKDrawing](./pkdrawing-swift.struct/erasingpath%28_,mask,transform%29-9dpi9.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Canvas
- [Drawing with PencilKit](./drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](./customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](./inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- [Importing Bézier path data into PencilKit](./importing-external-drawing-data-into-pencilkit.md)
  Convert existing Bézier-based stroke data into PencilKit drawing strokes.
- [Controlling stroke rendering for animation and editing](./controlling-stroke-rendering-for-animation-and-editing.md)
  Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.
- [class PKCanvasView](./pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [struct PKStroke](./pkstroke-swift.struct.md)
  A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.
- [struct PKStrokePath](./pkstrokepath-swift.struct.md)
  A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [struct PKStrokePoint](./pkstrokepoint-swift.struct.md)
  A structure that represents the properties of a specific point along a stroke’s path.
- [struct PKInk](./pkink-swift.struct.md)
  A structure that represents an ink that specifies its type, color, and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct)*