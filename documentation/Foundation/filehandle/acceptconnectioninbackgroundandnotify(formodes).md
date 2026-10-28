# acceptConnectionInBackgroundAndNotify(forModes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func acceptConnectionInBackgroundAndNotify(forModes modes: [RunLoop.Mode]?)
```

```objc
- (void) acceptConnectionInBackgroundAndNotifyForModes:(NSArray<NSString *> *) modes;
```

## Discussion

See [`acceptConnectionInBackgroundAndNotify()`](./acceptconnectioninbackgroundandnotify%28%29.md) for details of how this method operates. This method differs from [`acceptConnectionInBackgroundAndNotify()`](./acceptconnectioninbackgroundandnotify%28%29.md) in that `modes` specifies the run-loop mode (or modes) in which [`NSFileHandleConnectionAccepted`](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) can be posted.

You must call this method from a thread that has an active run loop.

## Parameters

- `modes`: The runloop modes in which the connection accepted notification can be posted.

## See Also

### Related Documentation
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](../notificationqueue/enqueue%28_,postingstyle,coalescemask,formodes%29.md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
### Reading asynchronously with notifications
- [func acceptConnectionInBackgroundAndNotify()](./acceptconnectioninbackgroundandnotify%28%29.md)
  Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [func readInBackgroundAndNotify()](./readinbackgroundandnotify%28%29.md)
  Reads from the file or communications channel in the background and posts a notification when finished.
- [func readInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](./readinbackgroundandnotify%28formodes%29.md)
  Reads from the file or communications channel in the background and posts a notification when finished.
- [func readToEndOfFileInBackgroundAndNotify()](./readtoendoffileinbackgroundandnotify%28%29.md)
  Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [func readToEndOfFileInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](./readtoendoffileinbackgroundandnotify%28formodes%29.md)
  Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [func waitForDataInBackgroundAndNotify()](./waitfordatainbackgroundandnotify%28%29.md)
  Asynchronously checks to see if data is available.
- [func waitForDataInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](./waitfordatainbackgroundandnotify%28formodes%29.md)
  Asynchronously checks to see if data is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/acceptconnectioninbackgroundandnotify(formodes:))*