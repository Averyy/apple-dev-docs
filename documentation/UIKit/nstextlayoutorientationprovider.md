# NSTextLayoutOrientationProvider

**Framework**: UIKit  
**Kind**: protocol

A set of methods that define the orientation of text for an object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSTextLayoutOrientationProvider
```

#### Overview

In macOS, the [`NSTextContainer`](nstextcontainer.md) and [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView) classes adopt this protocol; in iOS, only the [`NSTextContainer`](nstextcontainer.md) class implements it. An [`NSTextContainer`](nstextcontainer.md) object returns the value from its associated text view when present; otherwise, it returns [`NSLayoutManager.TextLayoutOrientation.horizontal`](nslayoutmanager/textlayoutorientation/horizontal.md) by default. If you define a custom [`NSTextContainer`](nstextcontainer.md) object, you can override this method and return [`NSLayoutManager.TextLayoutOrientation.vertical`](nslayoutmanager/textlayoutorientation/vertical.md) to support laying out text vertically.

## Topics

### Getting layout orientation
- [var layoutOrientation: NSLayoutManager.TextLayoutOrientation](nstextlayoutorientationprovider/layoutorientation.md)
  The default layout orientation.
- [NSLayoutManager.TextLayoutOrientation](nslayoutmanager/textlayoutorientation.md)
  Constants that describe the text layout orientation.

## Relationships

### Conforming Types
- [NSTextContainer](nstextcontainer.md)

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
- [protocol NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md)
  A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutorientationprovider)*