# NSTextViewportRenderingSurface

**Framework**: UIKit  
**Kind**: protocol

A protocol that identifies a view or layer as a drawable element for a text layout fragment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol NSTextViewportRenderingSurface : NSObjectProtocol
```

#### Overview

Conform a view or layer to `NSTextViewportRenderingSurface` to associate it with an [`NSTextLayoutFragment`](nstextlayoutfragment.md) during viewport layout. TextKit uses this to track, configure, and reuse visual elements across layout passes.

This protocol has no required methods. It gives TextKit a way to identify and manage the visual elements your delegate provides through [`NSTextViewportLayoutControllerDelegate`](nstextviewportlayoutcontrollerdelegate.md).

##### Implement a Rendering Surface

You can conform any `UIView`, `NSView`, or `CALayer` subclass to this protocol:

```swift
class TextFragmentView: UIView, NSTextViewportRenderingSurface {
    var layoutFragment: NSTextLayoutFragment?
}
```

Return instances from [`textViewportLayoutController(_:configureRenderingSurfaceFor:)`](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:configurerenderingsurfacefor:).md) so TextKit can manage them during layout.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [protocol NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md)
  A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportrenderingsurface)*