# NSWindowDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSWindowDelegate : NSObjectProtocol
```

## Topics

### Managing Sheets
- [func window(NSWindow, willPositionSheet: NSWindow, using: NSRect) -> NSRect](nswindowdelegate/window(_:willpositionsheet:using:).md)
  Tells the delegate that the window is about to show a sheet at the specified location, giving it the opportunity to return a custom location for the attachment of the sheet to the window.
- [func windowWillBeginSheet(Notification)](nswindowdelegate/windowwillbeginsheet(_:).md)
  Notifies the delegate that the window is about to open a sheet.
- [func windowDidEndSheet(Notification)](nswindowdelegate/windowdidendsheet(_:).md)
  Tells the delegate that the window has closed a sheet.
### Sizing Windows
- [func windowWillResize(NSWindow, to: NSSize) -> NSSize](nswindowdelegate/windowwillresize(_:to:).md)
  Tells the delegate that the window is being resized (whether by the user or through one of the `setFrame...` methods other than [`setFrame(_:display:)`](nswindow/setframe(_:display:).md)).
- [func windowDidResize(Notification)](nswindowdelegate/windowdidresize(_:).md)
  Tells the delegate that the window has been resized.
- [func windowWillStartLiveResize(Notification)](nswindowdelegate/windowwillstartliveresize(_:).md)
  Tells the delegate that the window is about to be live resized.
- [func windowDidEndLiveResize(Notification)](nswindowdelegate/windowdidendliveresize(_:).md)
  Tells the delegate that a live resize operation on the window has ended.
### Minimizing Windows
- [func windowWillMiniaturize(Notification)](nswindowdelegate/windowwillminiaturize(_:).md)
  Tells the delegate that the window is about to be minimized.
- [func windowDidMiniaturize(Notification)](nswindowdelegate/windowdidminiaturize(_:).md)
  Tells the delegate that the window has been minimized.
- [func windowDidDeminiaturize(Notification)](nswindowdelegate/windowdiddeminiaturize(_:).md)
  Tells the delegate that the window has been deminimized.
### Zooming Window
- [func windowWillUseStandardFrame(NSWindow, defaultFrame: NSRect) -> NSRect](nswindowdelegate/windowwillusestandardframe(_:defaultframe:).md)
  Called by `NSWindow`’s [`zoom(_:)`](nswindow/zoom(_:).md) method while determining the frame a window may be zoomed to.
- [func windowShouldZoom(NSWindow, toFrame: NSRect) -> Bool](nswindowdelegate/windowshouldzoom(_:toframe:).md)
  Asks the delegate whether the specified window should zoom to the specified frame.
### Managing Full-Screen Presentation
- [func window(NSWindow, willUseFullScreenContentSize: NSSize) -> NSSize](nswindowdelegate/window(_:willusefullscreencontentsize:).md)
  Called to allow the delegate to modify the full-screen content size.
- [func window(NSWindow, willUseFullScreenPresentationOptions: NSApplication.PresentationOptions) -> NSApplication.PresentationOptions](nswindowdelegate/window(_:willusefullscreenpresentationoptions:).md)
  Returns the presentation options the window uses when transitioning to full-screen mode.
- [func windowWillEnterFullScreen(Notification)](nswindowdelegate/windowwillenterfullscreen(_:).md)
  The window is about to enter full-screen mode.
- [func windowDidEnterFullScreen(Notification)](nswindowdelegate/windowdidenterfullscreen(_:).md)
  The window has entered full-screen mode.
- [func windowWillExitFullScreen(Notification)](nswindowdelegate/windowwillexitfullscreen(_:).md)
  The window is about to exit full-screen mode.
- [func windowDidExitFullScreen(Notification)](nswindowdelegate/windowdidexitfullscreen(_:).md)
  The window has left full-screen mode.
### Custom Full-Screen Presentation Animations
- [func customWindowsToEnterFullScreen(for: NSWindow) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:).md)
  Called when the window is about to enter full-screen mode.
- [func customWindowsToEnterFullScreen(for: NSWindow, on: NSScreen) -> [NSWindow]?](nswindowdelegate/customwindowstoenterfullscreen(for:on:).md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenwithduration:).md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenOn: NSScreen, withDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoenterfullscreenon:withduration:).md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func windowDidFailToEnterFullScreen(NSWindow)](nswindowdelegate/windowdidfailtoenterfullscreen(_:).md)
  Called if the window failed to enter full-screen mode.
- [func customWindowsToExitFullScreen(for: NSWindow) -> [NSWindow]?](nswindowdelegate/customwindowstoexitfullscreen(for:).md)
  Called when the window is about to exit full-screen mode.
- [func window(NSWindow, startCustomAnimationToExitFullScreenWithDuration: TimeInterval)](nswindowdelegate/window(_:startcustomanimationtoexitfullscreenwithduration:).md)
  This method is called to start the window animation out of full-screen mode, including transitioning back to the desktop space.
- [func windowDidFailToExitFullScreen(NSWindow)](nswindowdelegate/windowdidfailtoexitfullscreen(_:).md)
  Called if the window failed to exit full-screen mode.
### Moving Windows
- [func windowWillMove(Notification)](nswindowdelegate/windowwillmove(_:).md)
  Tells the delegate that the window is about to move.
- [func windowDidMove(Notification)](nswindowdelegate/windowdidmove(_:).md)
  Tells the delegate that the window has moved.
- [func windowDidChangeScreen(Notification)](nswindowdelegate/windowdidchangescreen(_:).md)
  Tells the delegate that the window has changed screens.
- [func windowDidChangeScreenProfile(Notification)](nswindowdelegate/windowdidchangescreenprofile(_:).md)
  Tells the delegate that the window has changed screen display profiles.
- [func windowDidChangeBackingProperties(Notification)](nswindowdelegate/windowdidchangebackingproperties(_:).md)
  Tells the delegate that the window backing properties changed.
### Closing Windows
- [func windowShouldClose(NSWindow) -> Bool](nswindowdelegate/windowshouldclose(_:).md)
  Tells the delegate that the user has attempted to close a window or the window has received a [`performClose(_:)`](nswindow/performclose(_:).md) message.
- [func windowWillClose(Notification)](nswindowdelegate/windowwillclose(_:).md)
  Tells the delegate that the window is about to close.
### Managing Key Status
- [func windowDidBecomeKey(Notification)](nswindowdelegate/windowdidbecomekey(_:).md)
  Tells the delegate that the window has become the key window.
- [func windowDidResignKey(Notification)](nswindowdelegate/windowdidresignkey(_:).md)
  Tells the delegate that the window has resigned key window status.
### Managing Main Status
- [func windowDidBecomeMain(Notification)](nswindowdelegate/windowdidbecomemain(_:).md)
  Tells the delegate that the window has become main.
- [func windowDidResignMain(Notification)](nswindowdelegate/windowdidresignmain(_:).md)
  Tells the delegate that the window has resigned main window status.
### Managing Field Editors
- [func windowWillReturnFieldEditor(NSWindow, to: Any?) -> Any?](nswindowdelegate/windowwillreturnfieldeditor(_:to:).md)
  Tells the delegate that the field editor for a text-displaying object has been requested.
### Updating Windows
- [func windowDidUpdate(Notification)](nswindowdelegate/windowdidupdate(_:).md)
  Tells the delegate that the window received an [`update()`](nswindow/update().md) message.
### Exposing Windows
- [func windowDidExpose(Notification)](nswindowdelegate/windowdidexpose(_:).md)
  Tells the delegate that the window has been exposed.
### Managing Occlusion State
- [func windowDidChangeOcclusionState(Notification)](nswindowdelegate/windowdidchangeocclusionstate(_:).md)
  Tells the delegate that the window changed its occlusion state.
### Dragging Windows
- [func window(NSWindow, shouldDragDocumentWith: NSEvent, from: NSPoint, with: NSPasteboard) -> Bool](nswindowdelegate/window(_:shoulddragdocumentwith:from:with:).md)
  Asks the delegate whether a user can drag the document icon from the window’s title bar.
### Getting the Undo Manager
- [func windowWillReturnUndoManager(NSWindow) -> UndoManager?](nswindowdelegate/windowwillreturnundomanager(_:).md)
  Tells the delegate that the window’s undo manager has been requested. Returns the appropriate undo manager for the window.
### Managing Titles
- [func window(NSWindow, shouldPopUpDocumentPathMenu: NSMenu) -> Bool](nswindowdelegate/window(_:shouldpopupdocumentpathmenu:).md)
  Asks the delegate whether the window displays the title pop-up menu in response to a Command-click or Control-click on its title.
### Managing Restorable State
- [func window(NSWindow, willEncodeRestorableState: NSCoder)](nswindowdelegate/window(_:willencoderestorablestate:).md)
  Tells the delegate the window is about to add its restorable state to a given archiver.
- [func window(NSWindow, didDecodeRestorableState: NSCoder)](nswindowdelegate/window(_:diddecoderestorablestate:).md)
  Tells the delegate the window is has extracted its restorable state from a given archiver.
### Managing Presentation in Version Browsers
- [func window(NSWindow, willResizeForVersionBrowserWithMaxPreferredSize: NSSize, maxAllowedSize: NSSize) -> NSSize](nswindowdelegate/window(_:willresizeforversionbrowserwithmaxpreferredsize:maxallowedsize:).md)
  Tells the delegate the window will resize for presentation during version browsing.
- [func windowWillEnterVersionBrowser(Notification)](nswindowdelegate/windowwillenterversionbrowser(_:).md)
  Tells the delegate the window is about to enter version browsing.
- [func windowDidEnterVersionBrowser(Notification)](nswindowdelegate/windowdidenterversionbrowser(_:).md)
  Tells the delegate that the window has entered version browsing.
- [func windowWillExitVersionBrowser(Notification)](nswindowdelegate/windowwillexitversionbrowser(_:).md)
  Tells the delegate that the window is about to leave version browsing.
- [func windowDidExitVersionBrowser(Notification)](nswindowdelegate/windowdidexitversionbrowser(_:).md)
  Tells the delegate that the window has left version browsing.
### Instance Methods
- [func previewRepresentableActivityItems(for: NSWindow) -> [any NSPreviewRepresentableActivityItem]?](nswindowdelegate/previewrepresentableactivityitems(for:).md)
- [func windowForSharingRequest(from: NSWindow) -> NSWindow?](nswindowdelegate/windowforsharingrequest(from:).md)
  Method called to get the window to share once sharing is confirmed, after a request is initiated by requestSharingOfWindowUsingPreview:title:completionHandler:. Implement this on the delegate of the requesting window

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSWindow](nswindow.md)
  A window that an app displays on the screen.
- [class NSPanel](nspanel.md)
  A special kind of window that typically performs a function that is auxiliary to the main window.
- [class NSWindowTab](nswindowtab.md)
  A tab associated with a window that is part of a tabbing group.
- [class NSWindowTabGroup](nswindowtabgroup.md)
  A group of windows that display together as a single tabbed window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate)*