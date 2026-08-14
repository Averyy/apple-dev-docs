# NSTextContainer

**Framework**: AppKit  
**Kind**: class

A region where text layout occurs.

**Availability**:
- macOS 10.0+

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
- [var textView: NSTextView?](nstextcontainer/textview.md)
  The text container’s text view.
### Defining the container shape
- [var size: CGSize](nstextcontainer/size.md)
  The size of the text container’s bounding rectangle.
- [var exclusionPaths: [NSBezierPath]](nstextcontainer/exclusionpaths.md)
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
- [convenience init(containerSize: NSSize)](nstextcontainer/init(containersize:).md)
  Initializes a text container with a specified bounding rectangle.
- [func lineFragmentRect(forProposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining: NSRectPointer?) -> NSRect](nstextcontainer/linefragmentrect(forproposedrect:sweepdirection:movementdirection:remaining:).md)
  Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.
- [func contains(NSPoint) -> Bool](nstextcontainer/contains(_:).md)
  Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.
- [var containerSize: NSSize](nstextcontainer/containersize.md)
  The size of the text container’s bounding rectangle.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)

## See Also

- [Using TextKit 2 to interact with text](../uikit/using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Managing viewport layout and attachment reuse in text views](../uikit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)
  Customize layout and preserve attachment views in your text view subclass.
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
- [protocol NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md)
  A protocol that identifies a view or layer as a drawable element for a text layout fragment.
- [protocol NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md)
  A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer)*