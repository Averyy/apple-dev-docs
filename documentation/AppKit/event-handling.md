# Event Handling

**Framework**: AppKit

Respond to mouse, keyboard, touch, and tablet events and gestures that originate inside your view.

## Topics

### Handling Events in the View
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nsview/acceptsfirstmouse(for:).md)
  Returns a Boolean value that indicates whether the view accepts the initial mouse-down event.
- [func hitTest(NSPoint) -> NSView?](nsview/hittest(_:).md)
  Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.
- [func isMousePoint(NSPoint, in: NSRect) -> Bool](nsview/ismousepoint(_:in:).md)
  Returns whether a region of the view contains a specified point, accounting for whether the view is flipped or not.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsview/performkeyequivalent(with:).md)
  Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).
- [func rightMouseDown(with: NSEvent)](nsresponder/rightmousedown(with:).md)
  Informs the receiver that the user has pressed the right mouse button.
- [var mouseDownCanMoveWindow: Bool](nsview/mousedowncanmovewindow.md)
  A Boolean value indicating whether the view can pass mouse down events through to its superviews.
- [var inputContext: NSTextInputContext?](nsview/inputcontext.md)
  The text input context object for the view.
### Handling Touch Events
- [var allowedTouchTypes: NSTouch.TouchTypeMask](nsview/allowedtouchtypes.md)
  The types of touch interactions the view allows.
- [var wantsRestingTouches: Bool](nsview/wantsrestingtouches.md)
  A Boolean value indicating whether the view wants resting touches.
- [var candidateListTouchBarItem: NSCandidateListTouchBarItem<AnyObject>?](nsview/candidatelisttouchbaritem.md)
### Managing Gesture Recognizers
- [var gestureRecognizers: [NSGestureRecognizer]](nsview/gesturerecognizers.md)
  The gesture recognize objects currently attached to the view.
- [func addGestureRecognizer(NSGestureRecognizer)](nsview/addgesturerecognizer(_:).md)
  Attaches a gesture recognizer to the view.
- [func removeGestureRecognizer(NSGestureRecognizer)](nsview/removegesturerecognizer(_:).md)
  Detaches a gesture recognizer from the view.
### Managing the Key-View Loop
- [var canBecomeKeyView: Bool](nsview/canbecomekeyview.md)
  A Boolean value indicating whether the view can become key view.
- [var needsPanelToBecomeKey: Bool](nsview/needspaneltobecomekey.md)
  A Boolean value indicating whether the view needs its panel to become the key window before it can handle keyboard input and navigation.
- [var nextKeyView: NSView?](nsview/nextkeyview.md)
  The view object that follows the current view in the key view loop.
- [var nextValidKeyView: NSView?](nsview/nextvalidkeyview.md)
  The closest view object in the key view loop that follows the current view in the key view loop and accepts first responder status.
- [var previousKeyView: NSView?](nsview/previouskeyview.md)
  The view object preceding the current view in the key view loop.
- [var previousValidKeyView: NSView?](nsview/previousvalidkeyview.md)
  The closest view object in the key view loop that precedes the current view and accepts first responder status.
### Handling Smart Magnification
- [func rectForSmartMagnification(at: NSPoint, in: NSRect) -> NSRect](nsview/rectforsmartmagnification(at:in:).md)
  Returns the appropriate rectangle to use when magnifying around the specified point.
### Managing Tracking Areas
- [func addTrackingArea(NSTrackingArea)](nsview/addtrackingarea(_:).md)
  Adds a given tracking area to the view.
- [func removeTrackingArea(NSTrackingArea)](nsview/removetrackingarea(_:).md)
  Removes a given tracking area from the view.
- [var trackingAreas: [NSTrackingArea]](nsview/trackingareas.md)
  An array of the view’s tracking areas.
- [func updateTrackingAreas()](nsview/updatetrackingareas.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](nsview/didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.
### Managing Tracking Rectangles
- [func addTrackingRect(NSRect, owner: Any, userData: UnsafeMutableRawPointer?, assumeInside: Bool) -> NSView.TrackingRectTag](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md)
  Establishes  an area for tracking mouse-entered and mouse-exited events within the view and returns a tag that identifies the tracking rectangle.
- [func removeTrackingRect(NSView.TrackingRectTag)](nsview/removetrackingrect(_:).md)
  Removes the tracking rectangle identified by a tag.
- [typealias TrackingRectTag](nsview/trackingrecttag.md)
  This type describes the rectangle used to track the mouse.
### Scrolling the View
- [func prepareContent(in: NSRect)](nsview/preparecontent(in:).md)
  Prepares the overdraw region for drawing.
- [var preparedContentRect: NSRect](nsview/preparedcontentrect.md)
  The portion of the view that has been rendered and is available for responsive scrolling.
- [func scroll(NSPoint)](nsview/scroll(_:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object so a point in the view lies at the origin of the clip view’s bounds rectangle.
- [func scrollToVisible(NSRect) -> Bool](nsview/scrolltovisible(_:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object the minimum distance needed so a specified region of the view becomes visible in the clip view.
- [func autoscroll(with: NSEvent) -> Bool](nsview/autoscroll(with:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object proportionally to the distance of an event that occurs outside of it.
- [func adjustScroll(NSRect) -> NSRect](nsview/adjustscroll(_:).md)
  Overridden by subclasses to modify a given rectangle, returning the altered rectangle.
- [var enclosingScrollView: NSScrollView?](nsview/enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.
- [func scroll(NSClipView, to: NSPoint)](nsview/scroll(_:to:).md)
  Notifies the superview of a clip view that the clip view needs to reset the origin of its bounds rectangle.
- [func reflectScrolledClipView(NSClipView)](nsview/reflectscrolledclipview(_:).md)
  Notifies a clip view’s superview that either the clip view’s bounds rectangle or the document view’s frame rectangle has changed, and that any indicators of the scroll position need to be adjusted.
- [class var isCompatibleWithResponsiveScrolling: Bool](nsview/iscompatiblewithresponsivescrolling.md)
  A Boolean value that indicates whether views support responsive scrolling.
### Configuring Pressure
- [var pressureConfiguration: NSPressureConfiguration?](nsview/pressureconfiguration.md)
  Configures the behavior and progression of the Force Touch trackpad when responding to touch input produced by the user when the cursor is over the view.
### Dragging Operations
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nsview/registerfordraggedtypes(_:).md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](nsview/unregisterdraggedtypes.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](nsview/registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nsview/begindraggingsession(with:event:source:).md)
  Initiates a dragging session with a group of dragging items.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nsview/shoulddelaywindowordering(for:).md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/event-handling)*