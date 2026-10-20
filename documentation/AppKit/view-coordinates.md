# View Coordinates

**Framework**: AppKit  
**Role**: API Collection

Manage the frame and bounds rectangles that determine the size and position of the view in the view hierarchy.

## Topics

### Modifying the Frame Rectangle
- [var frame: NSRect](./nsview/frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameOrigin(NSPoint)](./nsview/setframeorigin%28_%29.md)
  Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [func setFrameSize(NSSize)](./nsview/setframesize%28_%29.md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [var frameRotation: CGFloat](./nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](./nsview/framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [NSView.FrameDidChangeMessage](./nsview/framedidchangemessage.md)
- [var postsFrameChangedNotifications: Bool](./nsview/postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.
### Modifying the bounds rectangle
- [var bounds: NSRect](./nsview/bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func setBoundsOrigin(NSPoint)](./nsview/setboundsorigin%28_%29.md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [func setBoundsSize(NSSize)](./nsview/setboundssize%28_%29.md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [var boundsRotation: CGFloat](./nsview/boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [class let boundsDidChangeNotification: NSNotification.Name](./nsview/boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
- [NSView.BoundsDidChangeMessage](./nsview/boundsdidchangemessage.md)
- [var postsBoundsChangedNotifications: Bool](./nsview/postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.
### Examining Coordinate System Modifications
- [var isFlipped: Bool](./nsview/isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
- [var isRotatedFromBase: Bool](./nsview/isrotatedfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds.
- [var isRotatedOrScaledFromBase: Bool](./nsview/isrotatedorscaledfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds, or has been scaled from the window’s base coordinate system.
### Modifying the Coordinate System
- [func translateOrigin(to: NSPoint)](./nsview/translateorigin%28to%29.md)
  Translates the view’s coordinate system so that its origin moves to a new location.
- [func scaleUnitSquare(to: NSSize)](./nsview/scaleunitsquare%28to%29.md)
  Scales the view’s coordinate system so that the unit square scales to the specified dimensions.
- [func rotate(byDegrees: CGFloat)](./nsview/rotate%28bydegrees%29.md)
  Rotates the view’s bounds rectangle by a specified degree value around the origin of the coordinate system, (0.0, 0.0).
### Converting Coordinate Values
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](./nsview/backingalignedrect%28_,options%29.md)
  Returns a backing store pixel-aligned rectangle in local view coordinates.
- [func convertFromBacking(NSPoint) -> NSPoint](./nsview/convertfrombacking%28_%29-229ps.md)
  Converts a point from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSPoint) -> NSPoint](./nsview/converttobacking%28_%29-2xx45.md)
  Converts a point from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSPoint) -> NSPoint](./nsview/convertfromlayer%28_%29-3nsbu.md)
  Convert the point from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSPoint) -> NSPoint](./nsview/converttolayer%28_%29-44u7d.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convertFromBacking(NSRect) -> NSRect](./nsview/convertfrombacking%28_%29-2njpa.md)
  Converts a rectangle from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSRect) -> NSRect](./nsview/converttobacking%28_%29-3zors.md)
  Converts a rectangle from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSRect) -> NSRect](./nsview/convertfromlayer%28_%29-8s5bi.md)
  Convert the rectangle from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSRect) -> NSRect](./nsview/converttolayer%28_%29-160pw.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convertFromBacking(NSSize) -> NSSize](./nsview/convertfrombacking%28_%29-4agf9.md)
  Converts a size from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSSize) -> NSSize](./nsview/converttobacking%28_%29-4ra9y.md)
  Converts a size from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSSize) -> NSSize](./nsview/convertfromlayer%28_%29-3usqp.md)
  Convert the size from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSSize) -> NSSize](./nsview/converttolayer%28_%29-2vozx.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convert(NSPoint, from: NSView?) -> NSPoint](./nsview/convert%28_,from%29-1dq9l.md)
  Converts a point from the coordinate system of a given view to that of the view.
- [func convert(NSPoint, to: NSView?) -> NSPoint](./nsview/convert%28_,to%29-6u9ir.md)
  Converts a point from the view’s coordinate system to that of a given view.
- [func convert(NSSize, from: NSView?) -> NSSize](./nsview/convert%28_,from%29-40x0w.md)
  Converts a size from another view’s coordinate system to that of the view.
- [func convert(NSSize, to: NSView?) -> NSSize](./nsview/convert%28_,to%29-5nptx.md)
  Converts a size from the view’s coordinate system to that of another view.
- [func convert(NSRect, from: NSView?) -> NSRect](./nsview/convert%28_,from%29-7fbb6.md)
  Converts a rectangle from the coordinate system of another view to that of the view.
- [func convert(NSRect, to: NSView?) -> NSRect](./nsview/convert%28_,to%29-3cqqt.md)
  Converts a rectangle from the view’s coordinate system to that of another view.
- [func centerScanRect(NSRect) -> NSRect](./nsview/centerscanrect%28_%29.md)
  Converts the corners of a specified rectangle to lie on the center of device pixels, which is useful in compensating for rendering overscanning when the coordinate system has been scaled.

## See Also

### Configuring the view
- [View Hierarchy](./view-hierarchy.md)
  Manage the subviews, superview, and window of a view and respond to notifications when the view hierarchy changes.
- [Appearance](./nsview-appearance.md)
  Change the view’s visibility, vibrancy, and focus ring and respond to appearance-related changes.
- [Core Animation Support](./core-animation-support.md)
  Manage the layer object that provides the view’s visual representation and accelerates drawing operations.
- [Related UI](./related-ui.md)
  Manage contextual menus, cursors, tool tips, and other system-provided windows and content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/view-coordinates)*