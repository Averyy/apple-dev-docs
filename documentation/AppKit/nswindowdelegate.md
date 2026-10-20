# NSWindowDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.

**Availability**:
- macOS

## Declaration

```swift
protocol NSWindowDelegate : NSObjectProtocol
```

```objc
@protocol NSWindowDelegate <NSObject>
```

## Topics

### Managing Sheets
- [func window(NSWindow, willPositionSheet: NSWindow, using: NSRect) -> NSRect](./nswindowdelegate/window%28_,willpositionsheet,using%29.md)
  Tells the delegate that the window is about to show a sheet at the specified location, giving it the opportunity to return a custom location for the attachment of the sheet to the window.
- [func windowWillBeginSheet(Notification)](./nswindowdelegate/windowwillbeginsheet%28_%29.md)
  Notifies the delegate that the window is about to open a sheet.
- [func windowDidEndSheet(Notification)](./nswindowdelegate/windowdidendsheet%28_%29.md)
  Tells the delegate that the window has closed a sheet.
### Sizing Windows
- [func windowWillResize(NSWindow, to: NSSize) -> NSSize](./nswindowdelegate/windowwillresize%28_,to%29.md)
  Tells the delegate that the window is being resized (whether by the user or through one of the `setFrame...` methods other than [`setFrame(_:display:)`](./nswindow/setframe%28_,display%29.md)).
- [func windowDidResize(Notification)](./nswindowdelegate/windowdidresize%28_%29.md)
  Tells the delegate that the window has been resized.
- [func windowWillStartLiveResize(Notification)](./nswindowdelegate/windowwillstartliveresize%28_%29.md)
  Tells the delegate that the window is about to be live resized.
- [func windowDidEndLiveResize(Notification)](./nswindowdelegate/windowdidendliveresize%28_%29.md)
  Tells the delegate that a live resize operation on the window has ended.
### Minimizing Windows
- [func windowWillMiniaturize(Notification)](./nswindowdelegate/windowwillminiaturize%28_%29.md)
  Tells the delegate that the window is about to be minimized.
- [func windowDidMiniaturize(Notification)](./nswindowdelegate/windowdidminiaturize%28_%29.md)
  Tells the delegate that the window has been minimized.
- [func windowDidDeminiaturize(Notification)](./nswindowdelegate/windowdiddeminiaturize%28_%29.md)
  Tells the delegate that the window has been deminimized.
### Zooming Window
- [func windowWillUseStandardFrame(NSWindow, defaultFrame: NSRect) -> NSRect](./nswindowdelegate/windowwillusestandardframe%28_,defaultframe%29.md)
  Called by `NSWindow`’s [`zoom(_:)`](./nswindow/zoom%28_%29.md) method while determining the frame a window may be zoomed to.
- [func windowShouldZoom(NSWindow, toFrame: NSRect) -> Bool](./nswindowdelegate/windowshouldzoom%28_,toframe%29.md)
  Asks the delegate whether the specified window should zoom to the specified frame.
### Managing Full-Screen Presentation
- [func window(NSWindow, willUseFullScreenContentSize: NSSize) -> NSSize](./nswindowdelegate/window%28_,willusefullscreencontentsize%29.md)
  Called to allow the delegate to modify the full-screen content size.
- [func window(NSWindow, willUseFullScreenPresentationOptions: NSApplication.PresentationOptions) -> NSApplication.PresentationOptions](./nswindowdelegate/window%28_,willusefullscreenpresentationoptions%29.md)
  Returns the presentation options the window uses when transitioning to full-screen mode.
- [func windowWillEnterFullScreen(Notification)](./nswindowdelegate/windowwillenterfullscreen%28_%29.md)
  The window is about to enter full-screen mode.
- [func windowDidEnterFullScreen(Notification)](./nswindowdelegate/windowdidenterfullscreen%28_%29.md)
  The window has entered full-screen mode.
- [func windowWillExitFullScreen(Notification)](./nswindowdelegate/windowwillexitfullscreen%28_%29.md)
  The window is about to exit full-screen mode.
- [func windowDidExitFullScreen(Notification)](./nswindowdelegate/windowdidexitfullscreen%28_%29.md)
  The window has left full-screen mode.
### Custom Full-Screen Presentation Animations
- [func customWindowsToEnterFullScreen(for: NSWindow) -> [NSWindow]?](./nswindowdelegate/customwindowstoenterfullscreen%28for%29.md)
  Called when the window is about to enter full-screen mode.
- [func customWindowsToEnterFullScreen(for: NSWindow, on: NSScreen) -> [NSWindow]?](./nswindowdelegate/customwindowstoenterfullscreen%28for,on%29.md)
  Called when the window is about to enter full-screen mode.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenWithDuration: TimeInterval)](./nswindowdelegate/window%28_,startcustomanimationtoenterfullscreenwithduration%29.md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func window(NSWindow, startCustomAnimationToEnterFullScreenOn: NSScreen, withDuration: TimeInterval)](./nswindowdelegate/window%28_,startcustomanimationtoenterfullscreenon,withduration%29.md)
  This method is called to start the window animation into full-screen mode, including transitioning to a new space.
- [func windowDidFailToEnterFullScreen(NSWindow)](./nswindowdelegate/windowdidfailtoenterfullscreen%28_%29.md)
  Called if the window failed to enter full-screen mode.
- [func customWindowsToExitFullScreen(for: NSWindow) -> [NSWindow]?](./nswindowdelegate/customwindowstoexitfullscreen%28for%29.md)
  Called when the window is about to exit full-screen mode.
- [func window(NSWindow, startCustomAnimationToExitFullScreenWithDuration: TimeInterval)](./nswindowdelegate/window%28_,startcustomanimationtoexitfullscreenwithduration%29.md)
  This method is called to start the window animation out of full-screen mode, including transitioning back to the desktop space.
- [func windowDidFailToExitFullScreen(NSWindow)](./nswindowdelegate/windowdidfailtoexitfullscreen%28_%29.md)
  Called if the window failed to exit full-screen mode.
### Moving Windows
- [func windowWillMove(Notification)](./nswindowdelegate/windowwillmove%28_%29.md)
  Tells the delegate that the window is about to move.
- [func windowDidMove(Notification)](./nswindowdelegate/windowdidmove%28_%29.md)
  Tells the delegate that the window has moved.
- [func windowDidChangeScreen(Notification)](./nswindowdelegate/windowdidchangescreen%28_%29.md)
  Tells the delegate that the window has changed screens.
- [func windowDidChangeScreenProfile(Notification)](./nswindowdelegate/windowdidchangescreenprofile%28_%29.md)
  Tells the delegate that the window has changed screen display profiles.
- [func windowDidChangeBackingProperties(Notification)](./nswindowdelegate/windowdidchangebackingproperties%28_%29.md)
  Tells the delegate that the window backing properties changed.
### Closing Windows
- [func windowShouldClose(NSWindow) -> Bool](./nswindowdelegate/windowshouldclose%28_%29.md)
  Tells the delegate that the user has attempted to close a window or the window has received a [`performClose(_:)`](./nswindow/performclose%28_%29.md) message.
- [func windowWillClose(Notification)](./nswindowdelegate/windowwillclose%28_%29.md)
  Tells the delegate that the window is about to close.
### Managing Key Status
- [func windowDidBecomeKey(Notification)](./nswindowdelegate/windowdidbecomekey%28_%29.md)
  Tells the delegate that the window has become the key window.
- [func windowDidResignKey(Notification)](./nswindowdelegate/windowdidresignkey%28_%29.md)
  Tells the delegate that the window has resigned key window status.
### Managing Main Status
- [func windowDidBecomeMain(Notification)](./nswindowdelegate/windowdidbecomemain%28_%29.md)
  Tells the delegate that the window has become main.
- [func windowDidResignMain(Notification)](./nswindowdelegate/windowdidresignmain%28_%29.md)
  Tells the delegate that the window has resigned main window status.
### Managing Field Editors
- [func windowWillReturnFieldEditor(NSWindow, to: Any?) -> Any?](./nswindowdelegate/windowwillreturnfieldeditor%28_,to%29.md)
  Tells the delegate that the field editor for a text-displaying object has been requested.
### Updating Windows
- [func windowDidUpdate(Notification)](./nswindowdelegate/windowdidupdate%28_%29.md)
  Tells the delegate that the window received an [`update()`](./nswindow/update%28%29.md) message.
### Exposing Windows
- [func windowDidExpose(Notification)](./nswindowdelegate/windowdidexpose%28_%29.md)
  Tells the delegate that the window has been exposed.
### Managing Occlusion State
- [func windowDidChangeOcclusionState(Notification)](./nswindowdelegate/windowdidchangeocclusionstate%28_%29.md)
  Tells the delegate that the window changed its occlusion state.
### Dragging Windows
- [func window(NSWindow, shouldDragDocumentWith: NSEvent, from: NSPoint, with: NSPasteboard) -> Bool](./nswindowdelegate/window%28_,shoulddragdocumentwith,from,with%29.md)
  Asks the delegate whether a user can drag the document icon from the window’s title bar.
### Getting the Undo Manager
- [func windowWillReturnUndoManager(NSWindow) -> UndoManager?](./nswindowdelegate/windowwillreturnundomanager%28_%29.md)
  Tells the delegate that the window’s undo manager has been requested. Returns the appropriate undo manager for the window.
### Managing Titles
- [func window(NSWindow, shouldPopUpDocumentPathMenu: NSMenu) -> Bool](./nswindowdelegate/window%28_,shouldpopupdocumentpathmenu%29.md)
  Asks the delegate whether the window displays the title pop-up menu in response to a Command-click or Control-click on its title.
### Managing Restorable State
- [func window(NSWindow, willEncodeRestorableState: NSCoder)](./nswindowdelegate/window%28_,willencoderestorablestate%29.md)
  Tells the delegate the window is about to add its restorable state to a given archiver.
- [func window(NSWindow, didDecodeRestorableState: NSCoder)](./nswindowdelegate/window%28_,diddecoderestorablestate%29.md)
  Tells the delegate the window is has extracted its restorable state from a given archiver.
### Managing Presentation in Version Browsers
- [func window(NSWindow, willResizeForVersionBrowserWithMaxPreferredSize: NSSize, maxAllowedSize: NSSize) -> NSSize](./nswindowdelegate/window%28_,willresizeforversionbrowserwithmaxpreferredsize,maxallowedsize%29.md)
  Tells the delegate the window will resize for presentation during version browsing.
- [func windowWillEnterVersionBrowser(Notification)](./nswindowdelegate/windowwillenterversionbrowser%28_%29.md)
  Tells the delegate the window is about to enter version browsing.
- [func windowDidEnterVersionBrowser(Notification)](./nswindowdelegate/windowdidenterversionbrowser%28_%29.md)
  Tells the delegate that the window has entered version browsing.
- [func windowWillExitVersionBrowser(Notification)](./nswindowdelegate/windowwillexitversionbrowser%28_%29.md)
  Tells the delegate that the window is about to leave version browsing.
- [func windowDidExitVersionBrowser(Notification)](./nswindowdelegate/windowdidexitversionbrowser%28_%29.md)
  Tells the delegate that the window has left version browsing.
### Instance Methods
- [func previewRepresentableActivityItems(for: NSWindow) -> [any NSPreviewRepresentableActivityItem]?](./nswindowdelegate/previewrepresentableactivityitems%28for%29.md)
  A collection of Preview-representable activity items, used for sharing and collaboration.
- [func windowForSharingRequest(from: NSWindow) -> NSWindow?](./nswindowdelegate/windowforsharingrequest%28from%29.md)
  Method called to get the window to share once sharing is confirmed, after a request is initiated by requestSharingOfWindowUsingPreview:title:completionHandler:. Implement this on the delegate of the requesting window

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Windows
- [class NSWindow](./nswindow.md)
  A window that an app displays on the screen.
- [class NSPanel](./nspanel.md)
  A special kind of window that typically performs a function that is auxiliary to the main window.
- [class NSWindowTab](./nswindowtab.md)
  A tab associated with a window that is part of a tabbing group.
- [class NSWindowTabGroup](./nswindowtabgroup.md)
  A group of windows that display together as a single tabbed window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate)*