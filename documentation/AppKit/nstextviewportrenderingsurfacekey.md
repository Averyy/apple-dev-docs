# NSTextViewportRenderingSurfaceKey

**Framework**: AppKit  
**Kind**: protocol

A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol NSTextViewportRenderingSurfaceKey : NSObjectProtocol
```

#### Overview

`NSString` and [`NSTextLayoutFragment`](nstextlayoutfragment.md) conform to this protocol.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
### Conforming Types
- [NSTextLayoutFragment](nstextlayoutfragment.md)

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
- [class NSTextViewportLayoutController](nstextviewportlayoutcontroller.md)
  Manages the layout process inside the viewport interacting with its delegate.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.
- [protocol NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md)
  A protocol that identifies a view or layer as a drawable element for a text layout fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportrenderingsurfacekey)*