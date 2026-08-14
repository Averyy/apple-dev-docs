# NSTextViewportRenderingSurfaceKey

**Framework**: UIKit  
**Kind**: protocol

A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol NSTextViewportRenderingSurfaceKey : NSObjectProtocol
```

#### Overview

When TextKit lays out text in a viewport, it can ask your delegate to store and retrieve rendering surfaces across layout passes. Objects that conform to `NSTextViewportRenderingSurfaceKey` act as the identifier for each surface — TextKit passes them to your delegate when it needs to store or look one up.

Two types conform to this protocol by default:

- **`NSTextLayoutFragment`** — Use a layout fragment as a key to cache a rendering surface per fragment. This is the most common approach.
- **`NSString`** — Use a string as a key when you want to associate a rendering surface with a name rather than a fragment.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
### Conforming Types
- [NSTextLayoutFragment](nstextlayoutfragment.md)

## See Also

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md)
  Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)
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
- [protocol NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md)
  A protocol that identifies a view or layer as a drawable element for a text layout fragment.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportrenderingsurfacekey)*