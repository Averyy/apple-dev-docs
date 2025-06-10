# PencilKit

**Framework**: PencilKit  
**Kind**: module

Capture touch and Apple Pencil input as a drawing, and display that content from your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

#### Overview

PencilKit makes it easy to incorporate hand-drawn content into your iPadOS or macOS apps. PencilKit provides a drawing environment for your iOS app that receives input from Apple Pencil or the user’s finger, and turns it into images you display in iPadOS, iOS, or macOS. The environment comes with tools for creating, erasing, and selecting lines.

You capture content in your iPad app using a [`PKCanvasView`](pkcanvasview.md) object that you integrate into your existing view hierarchy. It supports the low-latency capture of touches originating from Apple Pencil or your finger. The canvas object sends final results as a [`PKDrawing`](pkdrawing-swift.struct.md) object, whose contents you can save with your app’s content. You can also convert the drawn content into an image for display in iOS or macOS app.

For information about handling user interactions on Apple Pencil in your UIKit app, see [`Apple Pencil interactions`](https://developer.apple.com/documentation/UIKit/apple-pencil-interactions).

## Topics

### Canvas
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
- [struct PKInk](pkink-swift.struct.md)
  A structure that represents an ink that specifies its type, color, and width.
### Tools
- [Configuring the PencilKit tool picker](configuring-the-pencilkit-tool-picker.md)
  Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.
- [class PKToolPicker](pktoolpicker.md)
  A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.
- [struct PKInkingTool](pkinkingtool-swift.struct.md)
  A structure that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.
- [struct PKEraserTool](pkerasertool-swift.struct.md)
  A tool for erasing previously drawn content in a canvas view.
- [struct PKLassoTool](pklassotool-swift.struct.md)
  A tool for selecting stroked lines and shapes in a canvas view.
- [protocol PKTool](pktool-swift.protocol.md)
  An interface adopted by drawing and writing tools used by a canvas view.
### Backward compatibility
- [Supporting backward compatibility for ink types](supporting-backward-compatibility-for-ink-types.md)
  Leverage the latest PencilKit features while providing a good user experience in earlier versions of the OS that don’t support those features.
- [enum PKContentVersion](pkcontentversion.md)
  Constants that represent versions of PencilKit for backward compatibility.
### Classes
- [class PKResponderState](pkresponderstate.md)
  The state of PencilKit behavior related to a `UIResponder`.
### Enumerations
- [enum PKToolPickerVisibility](pktoolpickervisibility.md)
  The visibility state of a tool picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PencilKit)*