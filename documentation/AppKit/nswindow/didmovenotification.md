# didMoveNotification

**Framework**: Appkit  
**Kind**: property

A notification that the window object moved.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didMoveNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSWindow` object that has moved. This notification doesn’t contain a `userInfo` dictionary.

> **Note**:  The system sends this notification when the window that moved didn’t also change size. See [`didResizeNotification`](nswindow/didresizenotification.md) for more information.

## See Also

- [class let didBecomeKeyNotification: NSNotification.Name](nswindow/didbecomekeynotification.md)
  A notification that the window object became the key window.
- [class let didBecomeMainNotification: NSNotification.Name](nswindow/didbecomemainnotification.md)
  A notification that the window object became the main window.
- [class let didChangeScreenNotification: NSNotification.Name](nswindow/didchangescreennotification.md)
  A notification that a portion of the window object’s frame moved onto or off of a screen.
- [class let didChangeScreenProfileNotification: NSNotification.Name](nswindow/didchangescreenprofilenotification.md)
  A notification that the screen containing the window changed.
- [class let didDeminiaturizeNotification: NSNotification.Name](nswindow/diddeminiaturizenotification.md)
  A notification that the window is no longer minimized.
- [class let didEndSheetNotification: NSNotification.Name](nswindow/didendsheetnotification.md)
  A notification that the window object closed an attached sheet.
- [class let didEndLiveResizeNotification: NSNotification.Name](nswindow/didendliveresizenotification.md)
  A notification that the user resized the window object.
- [class let didExposeNotification: NSNotification.Name](nswindow/didexposenotification.md)
  A notification that a window exposed a portion of its nonretained content.
- [class let didMiniaturizeNotification: NSNotification.Name](nswindow/didminiaturizenotification.md)
  A notification that the window object minimized.
- [class let didResignKeyNotification: NSNotification.Name](nswindow/didresignkeynotification.md)
  A notification that the window object resigned its status as key window.
- [class let didResignMainNotification: NSNotification.Name](nswindow/didresignmainnotification.md)
  A notification that the window object resigned its status as main window.
- [class let didResizeNotification: NSNotification.Name](nswindow/didresizenotification.md)
  A notification that the window object size changed.
- [class let didUpdateNotification: NSNotification.Name](nswindow/didupdatenotification.md)
  A notification that the window object received an update message.
- [class let willBeginSheetNotification: NSNotification.Name](nswindow/willbeginsheetnotification.md)
  A notification that the window object is about to open a sheet.
- [class let willCloseNotification: NSNotification.Name](nswindow/willclosenotification.md)
  A notification that the window object is about to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nswindow/didmovenotification)*