# readInBackgroundAndNotify()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Reads from the file or communications channel in the background and posts a notification when finished.

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
func readInBackgroundAndNotify()
```

```objc
- (void) readInBackgroundAndNotify;
```

## Discussion

This method performs an asynchronous [`availableData`](./availabledata.md) operation on a file or communications channel and posts an [`readCompletionNotification`](./readcompletionnotification.md) notification on the current thread when that operation is complete. You must call this method from a thread that has an active run loop.

The length of the data is limited to the buffer size of the underlying operating system. The notification includes a `userInfo` dictionary that contains the data read; access this object using the `NSFileHandleNotificationDataItem` key.

Any object interested in receiving this data asynchronously must add itself as an observer of [`readCompletionNotification`](./readcompletionnotification.md). In communication via stream-type sockets, the receiver is often the object returned in the `userInfo` dictionary of [`NSFileHandleConnectionAccepted`](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md).

Note that this method does not cause a continuous stream of notifications to be sent. If you wish to keep getting notified, you’ll also need to call [`readInBackgroundAndNotify()`](./readinbackgroundandnotify%28%29.md) in your observer method.

## See Also

### Related Documentation
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](../notificationqueue/enqueue%28_,postingstyle,coalescemask,formodes%29.md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
### Reading asynchronously with notifications
- [func acceptConnectionInBackgroundAndNotify()](./acceptconnectioninbackgroundandnotify%28%29.md)
  Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [func acceptConnectionInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](./acceptconnectioninbackgroundandnotify%28formodes%29.md)
  Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/readinbackgroundandnotify())*