# NSTextLayoutFragment

**Framework**: UIKit  
**Kind**: class

A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class NSTextLayoutFragment
```

## Topics

### Creating a layout fragment
- [init?(coder: NSCoder)](nstextlayoutfragment/init(coder:).md)
  Creates a new layout fragment with the coder you provide.
- [init(textElement: NSTextElement, range: NSTextRange?)](nstextlayoutfragment/init(textelement:range:).md)
  Create a new layout fragment using the provided text element and range.
### Getting line fragments
- [var textLineFragments: [NSTextLineFragment]](nstextlayoutfragment/textlinefragments.md)
  An array of text line fragments.
- [NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func textLineFragment(for: any NSTextLocation, isUpstreamAffinity: Bool) -> NSTextLineFragment?](nstextlayoutfragment/textlinefragment(for:isupstreamaffinity:).md)
  Returns a text line fragment from a specific text location in the document.
- [func textLineFragment(forVerticalOffset: CGFloat, requiresExactMatch: Bool) -> NSTextLineFragment?](nstextlayoutfragment/textlinefragment(forverticaloffset:requiresexactmatch:).md)
  Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.
### Getting element information
- [var state: NSTextLayoutFragment.State](nstextlayoutfragment/state-swift.property.md)
  The layout information state.
- [NSTextLayoutFragment.State](nstextlayoutfragment/state-swift.enum.md)
  Values that describe the possible layout states.
- [var rangeInElement: NSTextRange](nstextlayoutfragment/rangeinelement.md)
  The range inside the text element relative to the document origin.
- [var textElement: NSTextElement?](nstextlayoutfragment/textelement.md)
  The parent text element.
### Accessing the layout manager
- [var textLayoutManager: NSTextLayoutManager?](nstextlayoutfragment/textlayoutmanager.md)
  The layout manager for this text layout fragment.
### Drawing the fragment and attachments
- [var layoutFragmentFrame: CGRect](nstextlayoutfragment/layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [var renderingSurfaceBounds: CGRect](nstextlayoutfragment/renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func draw(at: CGPoint, in: CGContext)](nstextlayoutfragment/draw(at:in:).md)
  Renders the visual representation of this element in the specified graphics context.
- [func invalidateLayout()](nstextlayoutfragment/invalidatelayout.md)
  Invalidates any layout information associated with the text layout fragment.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](nstextlayoutfragment/textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](nstextlayoutfragment/framefortextattachment(at:).md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.
### Accessing the layout processing queue
- [var layoutQueue: OperationQueue?](nstextlayoutfragment/layoutqueue.md)
  The queue on which the framework dispatches layout operations.
### Defining margins and padding
- [var bottomMargin: CGFloat](nstextlayoutfragment/bottommargin.md)
  The amount of space reserved during paragraph layout between the bottom of the last line in the paragraph and the bottom of the text layout fragment.
- [var leadingPadding: CGFloat](nstextlayoutfragment/leadingpadding.md)
  The amount of margin space reserved during paragraph layout between the leading edge of the text layout fragment and the start of the lines in the paragraph.
- [var topMargin: CGFloat](nstextlayoutfragment/topmargin.md)
  The amount of space reserved during paragraph layout between the top of the text layout fragment and the top of the first line in the paragraph.
- [var trailingPadding: CGFloat](nstextlayoutfragment/trailingpadding.md)
  The amount of margin space reserved during paragraph layout between the end of the lines in the paragraph and the trailing edge of the text layout fragment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md)
  Lay out text in a custom-shaped container and apply glyph substitutions.
- [class NSTextLayoutManager](nstextlayoutmanager.md)
  The primary class that you use to manage text layout and presentation for custom text displays.
- [class NSTextContainer](nstextcontainer.md)
  A region where text layout occurs.
- [class NSTextLineFragment](nstextlinefragment.md)
  A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [class NSTextViewportLayoutController](nstextviewportlayoutcontroller.md)
  Manages the layout process inside the viewport interacting with its delegate.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment)*