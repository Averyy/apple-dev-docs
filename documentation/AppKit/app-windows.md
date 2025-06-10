# App Windows

**Framework**: AppKit

Show, hide, minimize, arrange, and update your app’s windows.

## Topics

### Managing App Windows
- [var keyWindow: NSWindow?](nsapplication/keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](nsapplication/mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](nsapplication/window(withwindownumber:).md)
  Returns the window corresponding to the specified window number.
- [var windows: [NSWindow]](nsapplication/windows.md)
  An array of the app’s window objects.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](nsapplication/makewindowsperform(_:inorder:).md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](nsapplication/enumeratewindows(options:using:).md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](nsapplication/windowlistoptions.md)
  This constant indicates a window ordering.
### Minimizing Windows
- [func miniaturizeAll(Any?)](nsapplication/miniaturizeall(_:).md)
  Miniaturizes all the receiver’s windows.
### Hiding Windows
- [var isHidden: Bool](nsapplication/ishidden.md)
  A Boolean value indicating whether the app is hidden.
- [func hide(Any?)](nsapplication/hide(_:).md)
  Hides all the receiver’s windows, and the next app in line is activated.
- [func unhide(Any?)](nsapplication/unhide(_:).md)
  Restores hidden windows to the screen and makes the receiver active.
- [func unhideWithoutActivation()](nsapplication/unhidewithoutactivation.md)
  Restores hidden windows without activating their owner (the receiver).
### Updating Windows
- [func updateWindows()](nsapplication/updatewindows.md)
  Sends an [`update()`](nswindow/update().md) message to each onscreen window.
- [func setWindowsNeedUpdate(Bool)](nsapplication/setwindowsneedupdate(_:).md)
  Sets whether the receiver’s windows need updating when the receiver has finished processing the current event.
### Managing Window Layers
- [func preventWindowOrdering()](nsapplication/preventwindowordering.md)
  Suppresses the usual window ordering in handling the most recent mouse-down event.
- [func arrangeInFront(Any?)](nsapplication/arrangeinfront(_:).md)
  Arranges windows listed in the Window menu in front of all other windows.
### Drawing Windows
- [var context: NSGraphicsContext?](nsapplication/context.md)
  The graphics context associated with the app.
### Getting the Occlusion State
- [var occlusionState: NSApplication.OcclusionState](nsapplication/occlusionstate-swift.property.md)
  The occlusion state of the app.
- [NSApplication.OcclusionState](nsapplication/occlusionstate-swift.struct.md)
  This constant indicates whether at least part of any window owned by this app is visible.
### Restoring App Windows at Launch
- [var isProtectedDataAvailable: Bool](nsapplication/isprotecteddataavailable.md)
- [func extendStateRestoration()](nsapplication/extendstaterestoration.md)
  Allows an app to extend its state restoration period.
- [func completeStateRestoration()](nsapplication/completestaterestoration.md)
  Completes the extended state restoration.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void) -> Bool](nsapplication/restorewindow(withidentifier:state:completionhandler:).md)
  Invoked to request that a window be restored.
### Managing Run Loops
- [class var displayWindowRunLoopOrdering: Int](nsapplication/displaywindowrunloopordering.md)
  The priority at which windows are displayed.
- [class var resetCursorRectsRunLoopOrdering: Int](nsapplication/resetcursorrectsrunloopordering.md)
  The priority at which cursor rects are reset.
- [NSUpdateWindowsRunLoopOrdering](nsupdatewindowsrunloopordering.md)
  This constant is used by the `NSRunLoop` method [`perform(_:target:argument:order:modes:)`](https://developer.apple.com/documentation/Foundation/RunLoop/perform(_:target:argument:order:modes:)).

## See Also

- [Modal Windows and Panels](modal-windows-and-panels.md)
  Display a modal window or show one of the standard app panels, such as the app’s About panel.
- [Menus](menus.md)
  Access the app’s main menu items and update the window and services menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/app-windows)*