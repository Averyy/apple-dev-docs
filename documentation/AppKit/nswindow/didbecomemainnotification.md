# didBecomeMainNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A notification that the window object became the main window.

**Availability**:
- macOS

## Declaration

```swift
class let didBecomeMainNotification: NSNotification.Name
```

```c
extern NSNotificationName NSWindowDidBecomeMainNotification;
```

## Discussion

The notification object is the `NSWindow` object that has become the main window. This notification doesn’t contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSWindow.DidBecomeMainMessage`](./didbecomemainmessage.md).

## See Also

### Notifications
- [class let didBecomeKeyNotification: NSNotification.Name](./didbecomekeynotification.md)
  A notification that the window object became the key window.
- [class let didChangeScreenNotification: NSNotification.Name](./didchangescreennotification.md)
  A notification that a portion of the window object’s frame moved onto or off of a screen.
- [class let didChangeScreenProfileNotification: NSNotification.Name](./didchangescreenprofilenotification.md)
  A notification that the screen containing the window changed.
- [class let didDeminiaturizeNotification: NSNotification.Name](./diddeminiaturizenotification.md)
  A notification that the window is no longer minimized.
- [class let didEndSheetNotification: NSNotification.Name](./didendsheetnotification.md)
  A notification that the window object closed an attached sheet.
- [class let didEndLiveResizeNotification: NSNotification.Name](./didendliveresizenotification.md)
  A notification that the user resized the window object.
- [class let didExposeNotification: NSNotification.Name](./didexposenotification.md)
  A notification that a window exposed a portion of its nonretained content.
- [class let didMiniaturizeNotification: NSNotification.Name](./didminiaturizenotification.md)
  A notification that the window object minimized.
- [class let didMoveNotification: NSNotification.Name](./didmovenotification.md)
  A notification that the window object moved.
- [class let didResignKeyNotification: NSNotification.Name](./didresignkeynotification.md)
  A notification that the window object resigned its status as key window.
- [class let didResignMainNotification: NSNotification.Name](./didresignmainnotification.md)
  A notification that the window object resigned its status as main window.
- [class let didResizeNotification: NSNotification.Name](./didresizenotification.md)
  A notification that the window object size changed.
- [class let didUpdateNotification: NSNotification.Name](./didupdatenotification.md)
  A notification that the window object received an update message.
- [class let willBeginSheetNotification: NSNotification.Name](./willbeginsheetnotification.md)
  A notification that the window object is about to open a sheet.
- [class let willCloseNotification: NSNotification.Name](./willclosenotification.md)
  A notification that the window object is about to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/didbecomemainnotification)*