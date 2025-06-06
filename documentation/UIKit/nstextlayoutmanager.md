# NSTextLayoutManager

**Framework**: UIKit  
**Kind**: class

The primary class that you use to manage text layout and presentation for custom text displays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class NSTextLayoutManager
```

#### Overview

`NSTextLayoutManager` is the centerpiece of the TextKit object network that maintains the layout geometry through an array of [`NSTextContainer`](nstextcontainer.md) objects. It lays out results using [`NSTextLayoutFragment`](nstextlayoutfragment.md) and [`NSTextElement`](nstextelement.md) objects vended from a [`NSTextContentManager`](nstextcontentmanager.md) that participates in the content layout process.

## Topics

### Creating a layout manager
- [init()](nstextlayoutmanager/init.md)
  Creates a new text layout manager.
- [init?(coder: NSCoder)](nstextlayoutmanager/init(coder:).md)
  Creates a new text layout manager with the coder you provide.
### Configuring global layout manager options
- [var layoutQueue: OperationQueue?](nstextlayoutmanager/layoutqueue.md)
  The queue that the framework dispatches layout operations on.
- [var renderingAttributesValidator: ((NSTextLayoutManager, NSTextLayoutFragment) -> Void)?](nstextlayoutmanager/renderingattributesvalidator.md)
  A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.
- [var usesFontLeading: Bool](nstextlayoutmanager/usesfontleading.md)
  A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.
- [var usesHyphenation: Bool](nstextlayoutmanager/useshyphenation.md)
  A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.
- [var limitsLayoutForSuspiciousContents: Bool](nstextlayoutmanager/limitslayoutforsuspiciouscontents.md)
  A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.
### Managing the layout process
- [var delegate: (any NSTextLayoutManagerDelegate)?](nstextlayoutmanager/delegate.md)
  The delegate for the text layout manager object.
- [protocol NSTextLayoutManagerDelegate](nstextlayoutmanagerdelegate.md)
  Optional methods that delegates implement to respond to layout changes.
### Accessing the text storage
- [var textContentManager: NSTextContentManager?](nstextlayoutmanager/textcontentmanager.md)
  Returns the text content manager associated with this text layout manager.
- [var textContainer: NSTextContainer?](nstextlayoutmanager/textcontainer.md)
  The text container object that provides geometric information for the layout destination.
- [var textSelectionNavigation: NSTextSelectionNavigation](nstextlayoutmanager/textselectionnavigation.md)
  Returns a text selection manager configured to have the text layout manager as its data source.
- [var textSelections: [NSTextSelection]](nstextlayoutmanager/textselections.md)
  An array of text selections associated by the text layout manager.
- [var usageBoundsForTextContainer: CGRect](nstextlayoutmanager/usageboundsfortextcontainer.md)
  Returns the usage bounds for the text container.
- [func enumerateTextSegments(in: NSTextRange, type: NSTextLayoutManager.SegmentType, options: NSTextLayoutManager.SegmentOptions, using: (NSTextRange?, CGRect, CGFloat, NSTextContainer) -> Bool)](nstextlayoutmanager/enumeratetextsegments(in:type:options:using:).md)
  Enumerates text segments of a specific type and in the text range you provide.
- [func replace(NSTextContentManager)](nstextlayoutmanager/replace(_:).md)
  Replaces the current text content manager with a new one you provide.
- [func replaceContents(in: NSTextRange, with: NSAttributedString)](nstextlayoutmanager/replacecontents(in:with:)-2elb.md)
  Replaces content at the location you specify with an attributed string you provide.
- [func replaceContents(in: NSTextRange, with: [NSTextElement])](nstextlayoutmanager/replacecontents(in:with:)-80j0b.md)
  Replaces content at the location you specify with the text elements string you provide.
### Adjusting rendering
- [class var linkRenderingAttributes: [NSAttributedString.Key : Any]](nstextlayoutmanager/linkrenderingattributes.md)
  Returns the default set of attributes for rendering a link.
- [func addRenderingAttribute(NSAttributedString.Key, value: Any?, for: NSTextRange)](nstextlayoutmanager/addrenderingattribute(_:value:for:).md)
  Sets the rendering attribute for the value and range you specify.
- [func enumerateRenderingAttributes(from: any NSTextLocation, reverse: Bool, using: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)](nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:).md)
  Enumerates the rendering attributes from a location you specify.
- [func renderingAttributes(forLink: Any, at: any NSTextLocation) -> [NSAttributedString.Key : Any]](nstextlayoutmanager/renderingattributes(forlink:at:).md)
  Returns a dictionary of rendering attributes for rendering a link.
- [func invalidateRenderingAttributes(for: NSTextRange)](nstextlayoutmanager/invalidaterenderingattributes(for:).md)
  Invalidates the rendering attributes of the specified text range.
- [func removeRenderingAttribute(NSAttributedString.Key, for: NSTextRange)](nstextlayoutmanager/removerenderingattribute(_:for:).md)
  Removes the rendering attribute from the specified text range.
- [func setRenderingAttributes([NSAttributedString.Key : Any], for: NSTextRange)](nstextlayoutmanager/setrenderingattributes(_:for:).md)
  Sets the rendering attributes for the range you specify.
### Causing layout generation
- [var textViewportLayoutController: NSTextViewportLayoutController](nstextlayoutmanager/textviewportlayoutcontroller.md)
  Returns text viewport layout controller associated with the layout manager’s text container.
- [func invalidateLayout(for: NSTextRange)](nstextlayoutmanager/invalidatelayout(for:).md)
  Invalidates the layout information for specified text range.
- [func textLayoutFragment(for: any NSTextLocation) -> NSTextLayoutFragment?](nstextlayoutmanager/textlayoutfragment(for:)-68dez.md)
  Returns the text layout fragment from the document at the specified location.
- [func textLayoutFragment(for: CGPoint) -> NSTextLayoutFragment?](nstextlayoutmanager/textlayoutfragment(for:)-4dhrx.md)
  Returns the text layout fragment at the position you specify in the text container.
- [func ensureLayout(for: CGRect)](nstextlayoutmanager/ensurelayout(for:)-6ptsj.md)
  Performs the layout for filling the bounds you specify inside the last text container.
- [func ensureLayout(for: NSTextRange)](nstextlayoutmanager/ensurelayout(for:)-3duae.md)
  Performs the layout for specified text range.
- [func enumerateTextLayoutFragments(from: (any NSTextLocation)?, options: NSTextLayoutFragment.EnumerationOptions, using: (NSTextLayoutFragment) -> Bool) -> (any NSTextLocation)?](nstextlayoutmanager/enumeratetextlayoutfragments(from:options:using:).md)
  Enumerates the text layout fragments starting at the specified location.
- [NSTextLayoutManager.SegmentType](nstextlayoutmanager/segmenttype.md)
  Values that describe the rendering of selection boundaries.
- [NSTextLayoutManager.SegmentOptions](nstextlayoutmanager/segmentoptions.md)
  Values that describe where and how the framework extends segments of a selection.

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
- [NSTextSelectionDataSource](nstextselectiondatasource.md)

## See Also

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md)
  Lay out text in a custom-shaped container and apply glyph substitutions.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager)*