# NSTextViewportLayoutController

**Framework**: AppKit  
**Kind**: class

Manages the layout process inside the viewport interacting with its delegate.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class NSTextViewportLayoutController
```

#### Overview

A viewport is a rectangular area within a flipped coordinate system expanding along the y-axis. With text contents, lines advance expanding the view in the current writing direction. The viewport defines the active area where the framework lays out text fragments. In most cases, the area corresponds to the user visible area with an additional over-scroll region.

## Topics

### Creating a viewport layout controller
- [init(textLayoutManager: NSTextLayoutManager)](nstextviewportlayoutcontroller/init(textlayoutmanager:).md)
  Creates a new instance with the text layout manager you provide.
### Accessing the layout manager
- [var textLayoutManager: NSTextLayoutManager?](nstextviewportlayoutcontroller/textlayoutmanager.md)
  Returns the text layout manager for this viewport layout controller.
### Responding to changes in viewport layout
- [var delegate: (any NSTextViewportLayoutControllerDelegate)?](nstextviewportlayoutcontroller/delegate.md)
  The delegate for the text layout manager object.
- [protocol NSTextViewportLayoutControllerDelegate](nstextviewportlayoutcontrollerdelegate.md)
  Optional methods that delegates implement to respond to viewport layout changes.
### Accessing the viewport characteristics
- [var viewportBounds: CGRect](nstextviewportlayoutcontroller/viewportbounds.md)
  Returns the visible bounds of the view, plus the overdraw area.
- [var viewportRange: NSTextRange?](nstextviewportlayoutcontroller/viewportrange.md)
  Returns the text range of the current viewport layout.
- [func adjustViewport(byVerticalOffset: CGFloat)](nstextviewportlayoutcontroller/adjustviewport(byverticaloffset:).md)
  Adjusts the viewport rect by the specified offset if needed.
- [func layoutViewport()](nstextviewportlayoutcontroller/layoutviewport.md)
  Performs layout in the viewport.
- [func relocateViewport(to: any NSTextLocation) -> CGFloat](nstextviewportlayoutcontroller/relocateviewport(to:).md)
  Relocates the viewport to the location you specify.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Using TextKit 2 to interact with text](../uikit/using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Managing viewport layout and attachment reuse in text views](../uikit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)
  Customize layout and preserve attachment views in your text view subclass.
- [class NSTextLayoutManager](nstextlayoutmanager.md)
  The primary class that you use to manage text layout and presentation for custom text displays.
- [class NSTextContainer](nstextcontainer.md)
  A region where text layout occurs.
- [class NSTextLayoutFragment](nstextlayoutfragment.md)
  A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [class NSTextLineFragment](nstextlinefragment.md)
  A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.
- [protocol NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md)
  A protocol that identifies a view or layer as a drawable element for a text layout fragment.
- [protocol NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md)
  A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontroller)*