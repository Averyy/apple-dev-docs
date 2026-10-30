# willMoveNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A notification that the window object is about to move.

**Availability**:
- macOS

## Declaration

```swift
class let willMoveNotification: NSNotification.Name
```

```c
extern NSNotificationName NSWindowWillMoveNotification;
```

## Discussion

The notification object is the `NSWindow` object that’s about to move. This notification doesn’t contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSWindow.WillMoveMessage`](./willmovemessage.md).

## See Also

### Notifications
- [class let didBecomeKeyNotification: NSNotification.Name](./didbecomekeynotification.md)
  A notification that the window object became the key window.
- [NSWindow.DidBecomeKeyMessage](./didbecomekeymessage.md)
  A message that reports that the window object became the key window.
- [class let didBecomeMainNotification: NSNotification.Name](./didbecomemainnotification.md)
  A notification that the window object became the main window.
- [NSWindow.DidBecomeMainMessage](./didbecomemainmessage.md)
  A message that reports that the window object became the main window.
- [class let didChangeScreenNotification: NSNotification.Name](./didchangescreennotification.md)
  A notification that a portion of the window object’s frame moved onto or off of a screen.
- [NSWindow.DidChangeScreenMessage](./didchangescreenmessage.md)
  A message that reports that a portion of the window object’s frame moved onto or off of a screen.
- [class let didChangeScreenProfileNotification: NSNotification.Name](./didchangescreenprofilenotification.md)
  A notification that the screen containing the window changed.
- [NSWindow.DidChangeScreenProfileMessage](./didchangescreenprofilemessage.md)
  A message that reports that the screen containing the window changed.
- [class let didDeminiaturizeNotification: NSNotification.Name](./diddeminiaturizenotification.md)
  A notification that the window is no longer minimized.
- [NSWindow.DidDeminiaturizeMessage](./diddeminiaturizemessage.md)
  A message that reports that the window is no longer minimized.
- [class let didEndSheetNotification: NSNotification.Name](./didendsheetnotification.md)
  A notification that the window object closed an attached sheet.
- [NSWindow.DidEndSheetMessage](./didendsheetmessage.md)
  A message that reports that the window object closed an attached sheet.
- [class let didEndLiveResizeNotification: NSNotification.Name](./didendliveresizenotification.md)
  A notification that the user resized the window object.
- [NSWindow.DidEndLiveResizeMessage](./didendliveresizemessage.md)
  A message that reports that a person resized the window object.
- [class let didExposeNotification: NSNotification.Name](./didexposenotification.md)
  A notification that a window exposed a portion of its nonretained content.
- [NSWindowDidMiniaturizeNotification](./didminiaturizenotification.md)
  A notification that the window object minimized.
- [NSWindowDidMoveNotification](./didmovenotification.md)
  A notification that the window object moved.
- [NSWindowDidResignKeyNotification](./didresignkeynotification.md)
  A notification that the window object resigned its status as key window.
- [NSWindowDidResignMainNotification](./didresignmainnotification.md)
  A notification that the window object resigned its status as main window.
- [NSWindowDidResizeNotification](./didresizenotification.md)
  A notification that the window object size changed.
- [NSWindowDidUpdateNotification](./didupdatenotification.md)
  A notification that the window object received an update message.
- [NSWindowWillBeginSheetNotification](./willbeginsheetnotification.md)
  A notification that the window object is about to open a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/willmovenotification)*