# NSTextContainer

**Framework**: UIKit  
**Kind**: class

A region where text layout occurs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class NSTextContainer
```

#### Overview

An [`NSLayoutManager`](nslayoutmanager.md) uses [`NSTextContainer`](nstextcontainer.md) to determine where to break lines, lay out portions of text, and so on. An [`NSTextContainer`](nstextcontainer.md) object typically defines rectangular regions, but you can define exclusion paths inside the text container to create regions where text doesn’t flow. You can also subclass to create text containers with nonrectangular regions, such as circular regions, regions with holes in them, or regions that flow alongside graphics.

You can access instances of the [`NSTextContainer`](nstextcontainer.md), [`NSLayoutManager`](nslayoutmanager.md), and [`NSTextStorage`](nstextstorage.md) classes from threads other than the main thread as long as the app guarantees access from only one thread at a time.

## Topics

### Creating a text container
- [init(size: CGSize)](nstextcontainer/init(size:).md)
  Initializes a text container with a specified bounding rectangle.
- [init(coder: NSCoder)](nstextcontainer/init(coder:).md)
  Creates a text container from data in an unarchiver.
### Managing text components
- [var layoutManager: NSLayoutManager?](nstextcontainer/layoutmanager.md)
  The text container’s layout manager.
- [var textLayoutManager: NSTextLayoutManager?](nstextcontainer/textlayoutmanager.md)
- [func replaceLayoutManager(NSLayoutManager)](nstextcontainer/replacelayoutmanager(_:).md)
  Replaces the layout manager for the group of text system objects that contains the text container.
- [weak var textView: NSTextView? { get set }](../AppKit/NSTextContainer/textView.md)
  The text container’s text view.
### Defining the container shape
- [var size: CGSize](nstextcontainer/size.md)
  The size of the text container’s bounding rectangle.
- [var exclusionPaths: [UIBezierPath]](nstextcontainer/exclusionpaths.md)
  An array of path objects that represents the regions where text doesn’t display in the text container.
- [var lineBreakMode: NSLineBreakMode](nstextcontainer/linebreakmode.md)
  The behavior of the last line inside the text container.
- [var widthTracksTextView: Bool](nstextcontainer/widthtrackstextview.md)
  A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.
- [var heightTracksTextView: Bool](nstextcontainer/heighttrackstextview.md)
  A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.
### Constraining text layout
- [var maximumNumberOfLines: Int](nstextcontainer/maximumnumberoflines.md)
  The maximum number of lines that the text container can store.
- [var lineFragmentPadding: CGFloat](nstextcontainer/linefragmentpadding.md)
  The value for the text inset within line fragment rectangles.
- [func lineFragmentRect(forProposedRect: CGRect, at: Int, writingDirection: NSWritingDirection, remaining: UnsafeMutablePointer<CGRect>?) -> CGRect](nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:).md)
  Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.
- [var isSimpleRectangularTextContainer: Bool](nstextcontainer/issimplerectangulartextcontainer.md)
  A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.
### Deprecated
- [convenience init(containerSize aContainerSize: NSSize)](../AppKit/NSTextContainer/init(containerSize:).md)
  Initializes a text container with a specified bounding rectangle.
- [func lineFragmentRect(forProposedRect proposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining remainingRect: NSRectPointer?) -> NSRect](../AppKit/NSTextContainer/lineFragmentRect(forProposedRect:sweepDirection:movementDirection:remaining:).md)
  Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.
- [func contains(_ point: NSPoint) -> Bool](../AppKit/NSTextContainer/contains(_:).md)
  Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.
- [var containerSize: NSSize { get set }](../AppKit/NSTextContainer/containerSize.md)
  The size of the text container’s bounding rectangle.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)

## See Also

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md)
  Lay out text in a custom-shaped container and apply glyph substitutions.
- [class NSTextLayoutManager](nstextlayoutmanager.md)
  The primary class that you use to manage text layout and presentation for custom text displays.
- [class NSTextLayoutFragment](nstextlayoutfragment.md)
  A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [class NSTextLineFragment](nstextlinefragment.md)
  A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [class NSTextViewportLayoutController](nstextviewportlayoutcontroller.md)
  Manages the layout process inside the viewport interacting with its delegate.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer)*