# PKCanvasView

**Framework**: PencilKit  
**Kind**: class

A view that captures Apple Pencil input and displays the rendered results in an iOS app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class PKCanvasView
```

## Mentions

- [Supporting backward compatibility for ink types](supporting-backward-compatibility-for-ink-types.md)

#### Overview

A [`PKCanvasView`](pkcanvasview.md) object captures content drawn using Apple Pencil or the user’s finger and displays it in your app. The canvas view handles all of the touch events and data coming from Apple Pencil, and renders that information using the tool you specify. The canvas stores the captured input in a [`PKDrawingReference`](pkdrawingreference.md) object.

[`PKCanvasView`](pkcanvasview.md) is a scroll view, so you can make the drawable area bigger than the canvas view’s frame rectangle. To do that, set the inherited [`contentSize`](https://developer.apple.com/documentation/UIKit/UIScrollView/contentSize) property to the size you want. The canvas view automatically scales its underlying content to match the size you specify. Users scroll around the canvas using a two-finger pan gesture. (If the [`allowsFingerDrawing`](pkcanvasview/allowsfingerdrawing.md) property is `false`, users scroll with only one finger.)

A canvas view conforms to the [`PKToolPickerObserver`](pktoolpickerobserver.md) protocol, so you can add it as an observer of the window’s tool picker. The tool picker displays a floating palette of tools that the user can choose from. As the user interacts with items in the palette, such as changing ink colors, or line widths, the canvas automatically updates its drawing environment accordingly.

## Topics

### Responding to drawing-related changes
- [var delegate: (any PKCanvasViewDelegate)?](pkcanvasview/delegate.md)
  The object you use to respond to changes in the drawn content or with the selected tool.
- [protocol PKCanvasViewDelegate](pkcanvasviewdelegate.md)
  Methods for monitoring drawing related changes in a canvas view.
### Configuring the drawing environment
- [var tool: any PKTool](pkcanvasview/tool-1kj57.md)
  The currently selected tool used for drawing.
- [var isRulerActive: Bool](pkcanvasview/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
- [var allowsFingerDrawing: Bool](pkcanvasview/allowsfingerdrawing.md)
  A Boolean value that indicates whether the canvas accepts input from the user’s finger in addition to Apple Pencil.
- [var drawingPolicy: PKCanvasViewDrawingPolicy](pkcanvasview/drawingpolicy.md)
  The policy that controls the types of touches allowed when drawing on the canvas.
- [enum PKCanvasViewDrawingPolicy](pkcanvasviewdrawingpolicy.md)
  Constants that you use to specify the type of drawing gestures your app permits while the user draws on the canvas.
### Getting the drawing gesture recognizer
- [var drawingGestureRecognizer: UIGestureRecognizer](pkcanvasview/drawinggesturerecognizer.md)
  The gesture recognizer that the canvas uses to track touch events.
### Getting the captured data
- [var drawing: PKDrawing](pkcanvasview/drawing.md)
  The data object that the canvas uses to store drawn content.
### Supporting PencilKit versions
- [var maximumSupportedContentVersion: PKContentVersion](pkcanvasview/maximumsupportedcontentversion.md)
  The maximum version of PencilKit to support.
### Instance Properties
- [var isDrawingEnabled: Bool](pkcanvasview/isdrawingenabled.md)

## Relationships

### Inherits From
- [UIScrollView](../UIKit/UIScrollView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [PKToolPickerObserver](pktoolpickerobserver.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIFocusItemScrollableContainer](../UIKit/UIFocusItemScrollableContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Drawing with PencilKit](drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasview)*