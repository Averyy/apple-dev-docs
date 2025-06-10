# NSClipView

**Framework**: AppKit  
**Kind**: class

An object that clips a document view to a scroll view’s frame.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSClipView
```

#### Overview

An [`NSClipView`](nsclipview.md) holds the document view of an [`NSScrollView`](nsscrollview.md), clipping the document view to its frame, handling the details of scrolling in an efficient manner, and updating the [`NSScrollView`](nsscrollview.md) when the document view’s size or position changes.

You don’t typically use the [`NSClipView`](nsclipview.md) class directly; it’s provided primarily as the scrolling machinery for the [`NSScrollView`](nsscrollview.md) class. However, you might use the [`NSClipView`](nsclipview.md) class to implement a class similar to [`NSScrollView`](nsscrollview.md).

##### Interaction with Nsscrollview

When using an [`NSClipView`](nsclipview.md) within an [`NSScrollView`](nsscrollview.md) (the usual configuration), you should access the [`NSScrollView`](nsscrollview.md) properties that control background drawing state, rather than accessing these properties of the [`NSClipView`](nsclipview.md). This recommendation applies to the following properties:

- [`backgroundColor`](nsclipview/backgroundcolor.md)
- [`drawsBackground`](nsclipview/drawsbackground.md)

The [`NSClipView`](nsclipview.md) methods are intended for when the [`NSClipView`](nsclipview.md) is used independently of a containing [`NSScrollView`](nsscrollview.md). In the usual case, [`NSScrollView`](nsscrollview.md) should be allowed to manage the background-drawing properties of its associated [`NSClipView`](nsclipview.md).

There is only one background-drawing state per [`NSScrollView`](nsscrollview.md)/[`NSClipView`](nsclipview.md) pair. The two objects do not maintain independent and distinct [`drawsBackground`](nsclipview/drawsbackground.md) and [`backgroundColor`](nsclipview/backgroundcolor.md) properties; rather, the accessors for these properties on [`NSScrollView`](nsscrollview.md) largely defer to the associated [`NSClipView`](nsclipview.md) and allow the [`NSClipView`](nsclipview.md) to maintain the state. Note that this state is not cached by the [`NSScrollView`](nsscrollview.md) object.

It is also important to note that setting [`drawsBackground`](nsclipview/drawsbackground.md) to [`false`](https://developer.apple.com/documentation/swift/false) in an [`NSScrollView`](nsscrollview.md) has the added effect of setting the [`NSClipView`](nsclipview.md) property [`copiesOnScroll`](nsclipview/copiesonscroll.md) to [`false`](https://developer.apple.com/documentation/swift/false). The side effect of setting the [`drawsBackground`](nsclipview/drawsbackground.md) property directly to the [`NSClipView`](nsclipview.md) is the appearance of “trails” (vestiges of previous drawing) in the document view as it is scrolled.

## Topics

### Setting the Document View
- [var documentView: NSView?](nsclipview/documentview.md)
  The clip view’s document view.
### Scrolling
- [func scroll(to: NSPoint)](nsclipview/scroll(to:).md)
  Changes the origin of the clip view’s bounds rectangle to `newOrigin`.
- [func autoscroll(with: NSEvent) -> Bool](nsclipview/autoscroll(with:).md)
  Scrolls the clip view proportionally to `theEvent`’s distance outside of it.
- [func constrainScroll(NSPoint) -> NSPoint](nsclipview/constrainscroll(_:).md)
  Returns a scroll point adjusted from the proposed new origin, if necessary, to guarantee the view will lie within its document view.
- [func constrainBoundsRect(NSRect) -> NSRect](nsclipview/constrainboundsrect(_:).md)
  Constrains the bounds of the clip view while the user is magnifying and scrolling.
### Determining Scrolling Efficiency
- [var copiesOnScroll: Bool](nsclipview/copiesonscroll.md)
  A Boolean value that indicates if the clip view copies rendered images while scrolling.
### Accessing the Content Insets
- [var contentInsets: NSEdgeInsets](nsclipview/contentinsets.md)
  The distance that the content view is inset from the enclosing scroll view.
- [var automaticallyAdjustsContentInsets: Bool](nsclipview/automaticallyadjustscontentinsets.md)
  A Boolean value that indicates if the clip view automatically accounts for other scroll view subviews.
### Accessing the Visible Portion
- [var documentRect: NSRect](nsclipview/documentrect.md)
  The rectangle defining the document view’s frame, adjusted to the size of the clip view if the document view is smaller.
- [var documentVisibleRect: NSRect](nsclipview/documentvisiblerect.md)
  The exposed rectangle of the clip view’s document view, in the document view’s own coordinate system.
### Setting the Document Cursor
- [var documentCursor: NSCursor?](nsclipview/documentcursor.md)
  The cursor object used when the pointer lies over the view.
### Working with Background Color
- [var drawsBackground: Bool](nsclipview/drawsbackground.md)
  A Boolean value that indicates if the clip view draws its background color.
- [var backgroundColor: NSColor](nsclipview/backgroundcolor.md)
  The color of the clip view’s background.
### Overriding NSView Methods
- [func viewBoundsChanged(Notification)](nsclipview/viewboundschanged(_:).md)
  Handles an [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](nsscrollview.md) based on the new bounds.
- [func viewFrameChanged(Notification)](nsclipview/viewframechanged(_:).md)
  Handles an [`frameDidChangeNotification`](nsview/framedidchangenotification.md), passed in the `aNotification` argument, by updating a containing [`NSScrollView`](nsscrollview.md) based on the new frame.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSScrollView](nsscrollview.md)
  A view that displays a portion of a document view and provides scroll bars that allow the user to move the document view within the scroll view.
- [class NSScroller](nsscroller.md)
  An object that controls scrolling of a document view within a scroll view or other type of container view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview)*