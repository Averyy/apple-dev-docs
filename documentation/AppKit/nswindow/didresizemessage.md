# NSWindow.DidResizeMessage

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A message that reports that the window object’s size changed.

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct DidResizeMessage
```

## Discussion

Use this message to observe the [`didResizeNotification`](./didresizenotification.md) notification using Swift concurrency.

## Topics

### Creating a message
- [init(window: NSWindow)](./didresizemessage/init%28window%29.md)
### Getting the message’s values
- [var window: NSWindow](./didresizemessage/window.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [class let didResizeNotification: NSNotification.Name](./didresizenotification.md)
  A notification that the window object size changed.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/didresizemessage)*