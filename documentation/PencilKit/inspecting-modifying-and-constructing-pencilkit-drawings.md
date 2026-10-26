# Inspecting, Modifying, and Constructing PencilKit Drawings

**Framework**: PencilKit  
**Role**: Sample Code  
**Download**: [InspectingModifyingAndConstructingPencilKitDrawings.zip](https://docs-assets.developer.apple.com/published/9ab4eccb5c46/InspectingModifyingAndConstructingPencilKitDrawings.zip)

Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- Xcode 11.5+

#### Overview

> **Note**: This sample code project is associated with WWDC20 session [10148: Inspect, Modify, and Construct PencilKit Drawings](https://developer.apple.com/videos/play/wwdc2020/10148/).

This sample code project must be run on a physical device with Apple Pencil.

## See Also

### Canvas
- [Drawing with PencilKit](./drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](./customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Importing Bézier path data into PencilKit](./importing-external-drawing-data-into-pencilkit.md)
  Convert existing Bézier-based stroke data into PencilKit drawing strokes.
- [Controlling stroke rendering for animation and editing](./controlling-stroke-rendering-for-animation-and-editing.md)
  Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.
- [class PKCanvasView](./pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [struct PKDrawing](./pkdrawing-swift.struct.md)
  A structure representing the drawing information captured by a canvas view.
- [struct PKStroke](./pkstroke-swift.struct.md)
  A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.
- [struct PKStrokePath](./pkstrokepath-swift.struct.md)
  A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [struct PKStrokePoint](./pkstrokepoint-swift.struct.md)
  A structure that represents the properties of a specific point along a stroke’s path.
- [struct PKInk](./pkink-swift.struct.md)
  A structure that represents an ink that specifies its type, color, and width.
- [PKDrawing](./pkdrawingreference.md)
  A data structure that contains the drawing information captured by a canvas view.
- [PKStroke](./pkstrokereference.md)
  A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.
- [PKStrokePath](./pkstrokepathreference.md)
  A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [PKStrokePoint](./pkstrokepointreference.md)
  A class that represents the properties of a specific point along a stroke’s path.
- [PKInk](./pkinkreference.md)
  Provides a description of the creation and rendering of marks on a canvas.
- [PKStrokeRenderState](./pkstrokerenderstatereference.md)
  An object that captures the render-time state of a stroke, such as grain texture position.
- [PKConvertedBezierPoint](./pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.
- [PKFloatRange](./pkfloatrange.md)
  A utility class that represents range components of a stroke.
- [PKInkTypeReed](./pkinktypereed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/inspecting-modifying-and-constructing-pencilkit-drawings)*