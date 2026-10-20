# Drawing

**Framework**: AppKit  
**Role**: API Collection

Draw the content of custom views and update that content when the view’s size or appearance changes.

## Topics

### Drawing the View’s Content
- [func updateLayer()](./nsview/updatelayer%28%29.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](./nsview/draw%28_%29.md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [var clipsToBounds: Bool](./nsview/clipstobounds.md)
  A Boolean value that indicates whether the view, and its subviews, confine their drawing areas to the bounds of the view.
- [var canDrawConcurrently: Bool](./nsview/candrawconcurrently.md)
  A Boolean value indicating whether the view can draw its contents on a background thread.
- [var visibleRect: NSRect](./nsview/visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
- [func getRectsBeingDrawn(UnsafeMutablePointer<UnsafePointer<NSRect>?>?, count: UnsafeMutablePointer<Int>?)](./nsview/getrectsbeingdrawn%28_,count%29.md)
  Returns by indirection a list of nonoverlapping rectangles that define the area the view is being asked to draw in [`draw(_:)`](./nsview/draw%28_%29.md).
- [func needsToDraw(NSRect) -> Bool](./nsview/needstodraw%28_%29.md)
  Returns a Boolean value indicating whether the specified rectangle intersects any part of the area that the view is being asked to draw.
- [var wantsDefaultClipping: Bool](./nsview/wantsdefaultclipping.md)
  A Boolean value indicating whether AppKit’s default clipping behavior is in effect.
- [func bitmapImageRepForCachingDisplay(in: NSRect) -> NSBitmapImageRep?](./nsview/bitmapimagerepforcachingdisplay%28in%29.md)
  Returns a bitmap-representation object suitable for caching the specified portion of the view.
- [func cacheDisplay(in: NSRect, to: NSBitmapImageRep)](./nsview/cachedisplay%28in,to%29.md)
  Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.
- [enum NSBorderType](./nsbordertype.md)
  These constants specify the type of a view’s border.
### Drawing the View in Fullscreen Mode
- [func enterFullScreenMode(NSScreen, withOptions: [NSView.FullScreenModeOptionKey : Any]?) -> Bool](./nsview/enterfullscreenmode%28_,withoptions%29.md)
  Sets the view to full screen mode.
- [func exitFullScreenMode(options: [NSView.FullScreenModeOptionKey : Any]?)](./nsview/exitfullscreenmode%28options%29.md)
  Instructs the view to exit full screen mode.
- [var isInFullScreenMode: Bool](./nsview/isinfullscreenmode.md)
  A Boolean value indicating whether the view is in full screen mode.
- [NSView.FullScreenModeOptionKey](./nsview/fullscreenmodeoptionkey.md)
  These constants are keys that you can use in the options dictionary in [`enterFullScreenMode(_:withOptions:)`](./nsview/enterfullscreenmode%28_,withoptions%29.md) and [`exitFullScreenMode(options:)`](./nsview/exitfullscreenmode%28options%29.md).
### Invalidating the View’s Content
- [func setNeedsDisplay(NSRect)](./nsview/setneedsdisplay%28_%29.md)
  Marks the region of the view within the specified rectangle as needing display, increasing the view’s existing invalid region to include it.
- [var needsDisplay: Bool](./nsview/needsdisplay.md)
  A Boolean value that determines whether the view needs to be redrawn before being displayed.
- [func display()](./nsview/display%28%29.md)
  Displays the view and all its subviews if possible, invoking each of the `NSView` methods [`lockFocus()`](./nsview/lockfocus%28%29.md), [`draw(_:)`](./nsview/draw%28_%29.md), and [`unlockFocus()`](./nsview/unlockfocus%28%29.md) as necessary.
- [func display(NSRect)](./nsview/display%28_%29.md)
  Acts as [`display()`](./nsview/display%28%29.md), but confining drawing to a rectangular region of the view.
- [func displayIgnoringOpacity(NSRect)](./nsview/displayignoringopacity%28_%29.md)
  Displays the view but confines drawing to a specified region and does not back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIgnoringOpacity(NSRect, in: NSGraphicsContext)](./nsview/displayignoringopacity%28_,in%29.md)
  Causes the view and its descendants to be redrawn to the specified graphics context.
- [func displayIfNeeded()](./nsview/displayifneeded%28%29.md)
  Displays the view and all its subviews if any part of the view has been marked as needing display.
- [func displayIfNeeded(NSRect)](./nsview/displayifneeded%28_%29.md)
  Acts as [`displayIfNeeded()`](./nsview/displayifneeded%28%29.md), confining drawing to a specified region of the view.
- [func displayIfNeededIgnoringOpacity()](./nsview/displayifneededignoringopacity%28%29.md)
  Acts as [`displayIfNeeded()`](./nsview/displayifneeded%28%29.md), except that this method doesn’t back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIfNeededIgnoringOpacity(NSRect)](./nsview/displayifneededignoringopacity%28_%29.md)
  Acts as [`displayIfNeeded()`](./nsview/displayifneeded%28%29.md), but confining drawing to `aRect` and not backing up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func translateRectsNeedingDisplay(in: NSRect, by: NSSize)](./nsview/translaterectsneedingdisplay%28in,by%29.md)
  Translates the display rectangles by the specified delta.
- [var isOpaque: Bool](./nsview/isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.
- [func viewWillDraw()](./nsview/viewwilldraw%28%29.md)
  Informs the view that it’s required to draw content.
### Updating the View When Property Values Change
- [NSView.Invalidating](./nsview/invalidating.md)
  A property wrapper that notifies the system that a property value change has invalidated an aspect of the containing view.
- [protocol NSViewInvalidating](./nsviewinvalidating.md)
  Implements a type of invalidation that can occur on a view that requires an update.
### Managing Live Resize
- [var inLiveResize: Bool](./nsview/inliveresize.md)
  A Boolean value indicating whether the view is being rendered as part of a live resizing operation.
- [var preservesContentDuringLiveResize: Bool](./nsview/preservescontentduringliveresize.md)
  A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.
- [func getRectsExposedDuringLiveResize(UnsafeMutablePointer<NSRect>, count: UnsafeMutablePointer<Int>)](./nsview/getrectsexposedduringliveresize%28_,count%29.md)
  Returns a list of rectangles indicating the newly exposed areas of the view.
- [var rectPreservedDuringLiveResize: NSRect](./nsview/rectpreservedduringliveresize.md)
  The rectangle identifying the portion of your view that did not change during a live resize operation.
- [func viewWillStartLiveResize()](./nsview/viewwillstartliveresize%28%29.md)
  Informs the view of the start of a live resize—the user has started resizing the view.
- [func viewDidEndLiveResize()](./nsview/viewdidendliveresize%28%29.md)
  Informs the view of the end of a live resize—the user has finished resizing the view.

## See Also

### Managing the view’s content
- [Layout](./layout.md)
  Specify the size and position your view relative to other nearby views using rules that update your view hierarchy automatically.
- [Printing](./nsview-printing.md)
  Create a printable version of your view’s content and handle pagination and printer-related behaviors.
- [protocol NSViewContentSelectionInfo](./nsviewcontentselectioninfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview-drawing)*