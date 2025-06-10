# NSScrollView

**Framework**: AppKit  
**Kind**: class

A view that displays a portion of a document view and provides scroll bars that allow the user to move the document view within the scroll view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSScrollView
```

#### Overview

The [`NSScrollView`](nsscrollview.md) class is the central coordinator for AppKit’s scrolling machinery, which is composed of this class, and the [`NSClipView`](nsclipview.md) and [`NSScroller`](nsscroller.md) classes.

When using an [`NSClipView`](nsclipview.md) object within a scroll view (the usual configuration), you should issue messages that control background drawing state to the scroll view directly, rather than messaging the clip view.

## Topics

### Calculating Layout
- [class func frameSize(forContentSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize](nsscrollview/framesize(forcontentsize:horizontalscrollerclass:verticalscrollerclass:bordertype:controlsize:scrollerstyle:).md)
  Returns the frame size of a scroll view that contains a content view with the specified size.
- [class func contentSize(forFrameSize: NSSize, horizontalScrollerClass: AnyClass?, verticalScrollerClass: AnyClass?, borderType: NSBorderType, controlSize: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> NSSize](nsscrollview/contentsize(forframesize:horizontalscrollerclass:verticalscrollerclass:bordertype:controlsize:scrollerstyle:).md)
  Returns the content size calculated from the frame size and the specified specifications.
### Determining Component Sizes
- [var contentSize: NSSize](nsscrollview/contentsize.md)
  The size of the scroll view’s content view.
- [var documentVisibleRect: NSRect](nsscrollview/documentvisiblerect.md)
  The portion of the document view, in its own coordinate system, visible through the scroll view’s content view.
### Managing Graphics Attributes
- [var backgroundColor: NSColor](nsscrollview/backgroundcolor.md)
  The color of the content view’s background.
- [var drawsBackground: Bool](nsscrollview/drawsbackground.md)
  A Boolean that indicates whether the scroll view draws its background.
- [var borderType: NSBorderType](nsscrollview/bordertype.md)
  A value that specifies the appearance of the scroll view’s border.
- [var documentCursor: NSCursor?](nsscrollview/documentcursor.md)
  The content view’s document cursor.
### Managing the Views
- [var contentView: NSClipView](nsscrollview/contentview.md)
  The scroll view’s content view, the view that clips the document view.
- [var documentView: NSView?](nsscrollview/documentview.md)
  The view the scroll view scrolls within its content view.
- [func addFloatingSubview(NSView, for: NSEvent.GestureAxis)](nsscrollview/addfloatingsubview(_:for:).md)
  Adds a floating subview to the document view.
### Managing Scrollers
- [var horizontalScroller: NSScroller?](nsscrollview/horizontalscroller.md)
  The scroll view’s horizontal scroller.
- [var hasHorizontalScroller: Bool](nsscrollview/hashorizontalscroller.md)
  A Boolean that indicates whether the scroll view has a horizontal scroller.
- [var verticalScroller: NSScroller?](nsscrollview/verticalscroller.md)
  The scroll view’s vertical scroller.
- [var hasVerticalScroller: Bool](nsscrollview/hasverticalscroller.md)
  A Boolean that indicates whether the scroll view has a vertical scroller.
- [var autohidesScrollers: Bool](nsscrollview/autohidesscrollers.md)
  A Boolean that indicates whether the scroll view automatically hides its scroll bars when they are not needed.
### Managing Rulers
- [class var rulerViewClass: AnyClass!](nsscrollview/rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var hasHorizontalRuler: Bool](nsscrollview/hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var horizontalRulerView: NSRulerView?](nsscrollview/horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var hasVerticalRuler: Bool](nsscrollview/hasverticalruler.md)
  A Boolean that indicates whether the scroll view keeps a vertical ruler object.
- [var verticalRulerView: NSRulerView?](nsscrollview/verticalrulerview.md)
  The scroll view’s vertical ruler view.
- [var rulersVisible: Bool](nsscrollview/rulersvisible.md)
  A Boolean that indicates whether the scroll view displays its rulers.
### Managing Insets
- [var automaticallyAdjustsContentInsets: Bool](nsscrollview/automaticallyadjustscontentinsets.md)
  A Boolean that indicates whether the scroll view automatically adjusts its content insets.
- [var contentInsets: NSEdgeInsets](nsscrollview/contentinsets.md)
  The distance that the scroll view’s subviews are inset from the enclosing scroll view during tiling.
- [var scrollerInsets: NSEdgeInsets](nsscrollview/scrollerinsets.md)
  The distance the scrollers are inset from the edge of the scroll view.
### Scroller Style
- [var scrollerKnobStyle: NSScroller.KnobStyle](nsscrollview/scrollerknobstyle.md)
  The knob style of scroll views that use the overlay scroller style.
- [var scrollerStyle: NSScroller.Style](nsscrollview/scrollerstyle.md)
  The scroller style used by the scroll view.
### Setting Scrolling Behavior
- [var lineScroll: CGFloat](nsscrollview/linescroll.md)
  The scroll view’s line by line scroll amount.
- [var horizontalLineScroll: CGFloat](nsscrollview/horizontallinescroll.md)
  The scroll view’s horizontal line by line scroll amount.
- [var verticalLineScroll: CGFloat](nsscrollview/verticallinescroll.md)
  The scroll view’s vertical line by line scroll amount.
- [var pageScroll: CGFloat](nsscrollview/pagescroll.md)
  The amount of the document view kept visible when scrolling page by page.
- [var horizontalPageScroll: CGFloat](nsscrollview/horizontalpagescroll.md)
  The amount of the document view kept visible when scrolling horizontally page by page.
- [var verticalPageScroll: CGFloat](nsscrollview/verticalpagescroll.md)
  The amount of the document view kept visible when scrolling vertically page by page.
- [var scrollsDynamically: Bool](nsscrollview/scrollsdynamically.md)
  A Boolean that indicates whether the scroll view redraws its document view while scrolling continuously.
- [func scrollWheel(with: NSEvent)](nsscrollview/scrollwheel(with:).md)
  Scrolls the receiver up or down, in response to the user moving the mouse’s scroll wheel specified by `theEvent`.
### Updating Display After Scrolling
- [func reflectScrolledClipView(NSClipView)](nsscrollview/reflectscrolledclipview(_:).md)
  Adjusts the receiver’s scrollers to reflect the size and positioning of its content view.
### Arranging Components
- [func tile()](nsscrollview/tile.md)
  Lays out the components of the receiver: the content view, the scrollers, and the ruler views.
### Find Bar Positioning
- [var findBarPosition: NSScrollView.FindBarPosition](nsscrollview/findbarposition-swift.property.md)
  The position of the find bar.
### Specifying a Document’s Predominant Scrolling Behavior
- [var usesPredominantAxisScrolling: Bool](nsscrollview/usespredominantaxisscrolling.md)
  A Boolean that indicates whether the scroll view uses a predominant scrolling axis for content.
### Specifying the Scroll View Elasticity
- [var horizontalScrollElasticity: NSScrollView.Elasticity](nsscrollview/horizontalscrollelasticity.md)
  The scroll view’s horizontal scrolling elasticity mode.
- [var verticalScrollElasticity: NSScrollView.Elasticity](nsscrollview/verticalscrollelasticity.md)
  The scroll view’s vertical scrolling elasticity mode.
### Flashing Overlay Scroll Bars
- [func flashScrollers()](nsscrollview/flashscrollers.md)
  Flash the overlay scroll bars.
### Zooming the Scroll View
- [var allowsMagnification: Bool](nsscrollview/allowsmagnification.md)
  Allows the user to magnify the scroll view.
- [var magnification: CGFloat](nsscrollview/magnification.md)
  The amount by which the content is currently scaled.
- [func magnify(toFit: NSRect)](nsscrollview/magnify(tofit:).md)
  Magnifies the content view proportionally such that the given rectangle fits centered in the scroll view.
- [var maxMagnification: CGFloat](nsscrollview/maxmagnification.md)
  The maximum value to which the content can be magnified.
- [var minMagnification: CGFloat](nsscrollview/minmagnification.md)
  The minimum value to which the content can be magnified.
- [func setMagnification(CGFloat, centeredAt: NSPoint)](nsscrollview/setmagnification(_:centeredat:).md)
  Magnify the content by the given amount and center the result on the given point.
### Constants
- [NSScrollView.Elasticity](nsscrollview/elasticity.md)
  These constants determine the elasticity behavior for an axis of the scrollview.
- [NSScrollView.FindBarPosition](nsscrollview/findbarposition-swift.enum.md)
  These constants define the position of the find bar in relation to the scroll view.
### Notifications
- [class let willStartLiveMagnifyNotification: NSNotification.Name](nsscrollview/willstartlivemagnifynotification.md)
  Posted at the beginning of a magnify gesture.
- [class let didEndLiveMagnifyNotification: NSNotification.Name](nsscrollview/didendlivemagnifynotification.md)
  Posted at the end of a magnify gesture.
- [class let willStartLiveScrollNotification: NSNotification.Name](nsscrollview/willstartlivescrollnotification.md)
  Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [class let didLiveScrollNotification: NSNotification.Name](nsscrollview/didlivescrollnotification.md)
  Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.
- [class let didEndLiveScrollNotification: NSNotification.Name](nsscrollview/didendlivescrollnotification.md)
  Posted on the main thread at the end of live scroll tracking.
### Initializers
- [init?(coder: NSCoder)](nsscrollview/init(coder:).md)
- [init(frame: NSRect)](nsscrollview/init(frame:).md)

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
- [NSTextFinderBarContainer](nstextfinderbarcontainer.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSScroller](nsscroller.md)
  An object that controls scrolling of a document view within a scroll view or other type of container view.
- [class NSClipView](nsclipview.md)
  An object that clips a document view to a scroll view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview)*