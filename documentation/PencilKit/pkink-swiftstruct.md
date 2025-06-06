# PKInk

**Framework**: PencilKit  
**Kind**: struct

A structure that represents an ink that specifies its type, color, and width.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct PKInk
```

## Mentions

- [Supporting backward compatibility for ink types](supporting-backward-compatibility-for-ink-types.md)

## Topics

### Creating an ink object
- [init(PKInk.InkType, color: UIColor)](pkink-swift.struct/init(_:color:)-2rx09.md)
  Creates a new ink, specifying its type and color.
- [init(PKInk.InkType, color: NSColor)](pkink-swift.struct/init(_:color:)-7w46l.md)
  Creates a new ink, specifying its type and color.
- [typealias InkType](pkink-swift.struct/inktype-swift.typealias.md)
  A type alias referring to the ink type of an inking tool.
### Getting the ink attributes
- [var color: UIColor](pkink-swift.struct/color-cg6f.md)
  The color of this ink.
- [var color: NSColor](pkink-swift.struct/color-6lmjp.md)
  The color of this ink.
- [var inkType: PKInk.InkType](pkink-swift.struct/inktype-swift.property.md)
  The line presentation to use for this Ink.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](pkink-swift.struct/requiredcontentversion.md)
  The version of PencilKit necessary to use the ink.
### Using reference types
- [class PKInkReference](pkinkreference.md)
  Provides a description of the creation and rendering of marks on a canvas.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)

## See Also

- [Drawing with PencilKit](drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- [class PKCanvasView](pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [struct PKDrawing](pkdrawing-swift.struct.md)
  A structure representing the drawing information captured by a canvas view.
- [struct PKStroke](pkstroke-swift.struct.md)
  A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.
- [struct PKStrokePath](pkstrokepath-swift.struct.md)
  A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [struct PKStrokePoint](pkstrokepoint-swift.struct.md)
  A structure that represents the properties of a specific point along a stroke’s path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkink-swift.struct)*