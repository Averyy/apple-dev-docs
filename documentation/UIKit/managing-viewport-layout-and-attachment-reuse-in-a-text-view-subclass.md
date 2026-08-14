# Managing viewport layout and attachment reuse in text views

**Framework**: UIKit

Customize layout and preserve attachment views in your text view subclass.

#### Overview

If you build a text editor with rich attachments — like images, videos, or interactive controls — you may notice that attachment views flicker or lose their state when someone scrolls the attachment out of the viewport, or types in the same paragraph. This is because text views discard and recreate attachment views as part of their normal layout process.

[`UITextView`](uitextview.md) and [`NSTextView`](https://developer.apple.com/documentation/appkit/nstextview) conform to [`NSTextViewportLayoutControllerDelegate`](nstextviewportlayoutcontrollerdelegate.md), giving your subclass direct access to the layout process. You can override the delegate methods to respond to layout events and customize how text fragments appear.

You can also register reuse policies to tell the text view which attachment views to preserve across scrolling and editing, eliminating flicker and preserving states like focus and playback position.

##### Override Viewport Layout Methods

[`layoutViewport()`](nstextviewportlayoutcontroller/layoutviewport().md) encompasses the viewport layout process. Each time the visual state within the viewport changes, TextKit calls it. During each viewport layout process, [`NSTextViewportLayoutController`](nstextviewportlayoutcontroller.md) calls the text view’s delegate methods at three points — before it starts, before each text layout fragment is about to be rendered, and after it completes. Override any of these methods in your [`UITextView`](uitextview.md) (or [`NSTextView`](https://developer.apple.com/documentation/appkit/nstextview) in macOS) subclass to customize what happens at each stage:

```swift
class CustomTextView: UITextView {

    override func textViewportLayoutControllerWillLayout(
        _ textViewportLayoutController: NSTextViewportLayoutController
    ) {
        super.textViewportLayoutControllerWillLayout(textViewportLayoutController)
        // Prepare any state before the layout pass begins.
    }

    override func textViewportLayoutController(
        _ textViewportLayoutController: NSTextViewportLayoutController,
        configureRenderingSurfaceFor textLayoutFragment: NSTextLayoutFragment
    ) {
        super.textViewportLayoutController(textViewportLayoutController, configureRenderingSurfaceFor: textLayoutFragment)
        // Inspect or customize each laid-out text fragment.
    }

    override func textViewportLayoutControllerDidLayout(
        _ textViewportLayoutController: NSTextViewportLayoutController
    ) {
        super.textViewportLayoutControllerDidLayout(textViewportLayoutController)
        // Finalize layout after all fragments are positioned.
    }
}
```

> ❗ **Important**: All overrides of viewport layout delegate methods must call `super`, because omitting it breaks layout. Query any [`NSTextViewportLayoutController`](nstextviewportlayoutcontroller.md) state only inside [`textViewportLayoutControllerDidLayout(_:)`](uitextview/textviewportlayoutcontrollerdidlayout(_:).md); querying it from other delegate methods can cause crashes.

The following table shows the set of available override points:

| Method | When called |
| --- | --- |
| [`textViewportLayoutControllerWillLayout(_:)`](uitextview/textviewportlayoutcontrollerwilllayout(_:).md) | Before each layout pass begins |
| [`textViewportLayoutController(_:configureRenderingSurfaceFor:)`](uitextview/textviewportlayoutcontroller(_:configurerenderingsurfacefor:).md) | Once per laid-out fragment, with its rendering surface |
| [`textViewportLayoutControllerDidLayout(_:)`](uitextview/textviewportlayoutcontrollerdidlayout(_:).md) | After each layout pass completes |
| [`textViewportLayoutControllerReceivedSetNeedsLayout(_:)`](uitextview/textviewportlayoutcontrollerreceivedsetneedslayout(_:).md) | When the viewport requests a layout invalidation |
| [`viewportBounds(for:)`](uitextview/viewportbounds(for:).md) | To query the current viewport bounds |

##### Register Reuse Policies

Use the registration API to preserve attachment views across layout passes. Call [`register(_:forTextAttachmentViewProviderType:)`](uitextview/register(_:fortextattachmentviewprovidertype:).md) once during setup to declare the reuse behavior per provider type:

```swift
// Retain video attachment views across both scrolling and paragraph edits.
textView.register(
    [.onScrollingOutOfViewport, .onEditingInlineParagraphs],
    forTextAttachmentViewProviderType: VideoAttachmentViewProvider.self
)

// Retain drawing views only when they scroll out of view.
textView.register(
    [.onScrollingOutOfViewport],
    forTextAttachmentViewProviderType: DrawingAttachmentViewProvider.self
)
```

After you register a provider type, the text view holds on to those attachment views when scrolling moves them out of view or editing changes the surrounding paragraph, and restores them when they come back. This automatically keeps video playback position and focused controls intact across scrolling and paragraph edits.

## See Also

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md)
  Lay out text in a custom-shaped container and apply glyph substitutions.
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
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass)*