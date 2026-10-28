# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func lockFocus()](./nsview/lockfocus%28%29.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func lockFocusIfCanDraw() -> Bool](./nsview/lockfocusifcandraw%28%29.md)
  Locks the focus to the view atomically if the `canDraw` method returns `true` and returns the value of `canDraw`.
- [func lockFocusIfCanDraw(in: NSGraphicsContext) -> Bool](./nsview/lockfocusifcandraw%28in%29.md)
  Locks the focus to the view atomically if drawing can occur in the specified graphics context.
- [func unlockFocus()](./nsview/unlockfocus%28%29.md)
  Unlocks focus from the current view.
- [func scroll(NSRect, by: NSSize)](./nsview/scroll%28_,by%29.md)
  Copies the visible portion of the view’s rendered image within a region and lays that portion down again at a specified offset .
- [func shouldDrawColor() -> Bool](./nsview/shoulddrawcolor%28%29.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
- [func allocateGState()](./nsview/allocategstate%28%29.md)
  Causes the view to maintain a private graphics state object, which encapsulates all parameters of the graphics environment.
- [func gState() -> Int](./nsview/gstate%28%29.md)
  Returns the identifier for the view’s graphics state object, or 0 if the view doesn’t have a graphics state object.
- [func setUpGState()](./nsview/setupgstate%28%29.md)
  Overridden by subclasses to (re)initialize the view’s graphics state object.
- [func renewGState()](./nsview/renewgstate%28%29.md)
  Invalidates the view’s graphics state object, if it has one.
- [func releaseGState()](./nsview/releasegstate%28%29.md)
  Frees the view’s graphics state object, if it has one.
- [func dragFile(String, from: NSRect, slideBack: Bool, event: NSEvent) -> Bool](./nsview/dragfile%28_,from,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag a file icon to any application that has window or view objects that accept files.
- [func dragPromisedFiles(ofTypes: [String], from: NSRect, source: Any, slideBack: Bool, event: NSEvent) -> Bool](./nsview/dragpromisedfiles%28oftypes,from,source,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag one or more promised files (or directories) into any application that has window or view objects that accept promised file data.
- [- convertPointToBase:](./nsview/convertpointtobase_.md)
  Converts the point from the view’s coordinate system to the base coordinate system.
- [- convertPointFromBase:](./nsview/convertpointfrombase_.md)
  Converts the point from the base coordinate system to the view’s coordinate system.
- [- convertSizeToBase:](./nsview/convertsizetobase_.md)
  Converts the size from the view’s coordinate system to the base coordinate system.
- [- convertSizeFromBase:](./nsview/convertsizefrombase_.md)
  Converts the size from the base coordinate system to the view’s coordinate system.
- [- convertRectToBase:](./nsview/convertrecttobase_.md)
  Converts the rectangle from the view’s coordinate system to the base coordinate system.
- [- convertRectFromBase:](./nsview/convertrectfrombase_.md)
  Converts the rectangle from the base coordinate system to the view’s coordinate system.
- [- performMnemonic:](./nsview/performmnemonic_.md)
  Implemented by subclasses to respond to mnemonics.
- [- dragImage:at:offset:event:pasteboard:source:slideBack:](./nsview/dragimage_at_offset_event_pasteboard_source_slideback_.md)
  Initiates a dragging operation from the view, allowing the user to drag arbitrary data with a specified icon into any application that has window or view objects that accept dragged data.
### Deprecated properties
- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](./nsview/wantsextendeddynamicrangeopenglsurface.md)
- [var acceptsTouchEvents: Bool](./nsview/acceptstouchevents.md)
  A Boolean value indicating whether the view accepts touch events.
- [var canDraw: Bool](./nsview/candraw.md)
  A Boolean value indicating whether drawing commands will produce any results.
- [var wantsBestResolutionOpenGLSurface: Bool](./nsview/wantsbestresolutionopenglsurface.md)
  A Boolean value indicating whether the view wants an OpenGL backing surface with a resolution greater than 1 pixel per point.
### Deprecated notifications
- [class let globalFrameDidChangeNotification: NSNotification.Name](./nsview/globalframedidchangenotification.md)
  Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated.
- [NSViewNoInstrinsicMetric](./nsviewnoinstrinsicmetric.md)
  Used to indicate that a view has no intrinsic metric for a given numeric property.
- [NSViewFocusDidChangeNotification](./nsviewfocusdidchangenotification.md)
  Deprecated in macOS 10.4 and later. Posted for an `NSView` object and each of its descendants (recursively) whenever the frame or bounds geometry of the view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview-deprecated-symbols)*