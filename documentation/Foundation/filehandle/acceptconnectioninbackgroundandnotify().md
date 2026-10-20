# acceptConnectionInBackgroundAndNotify()

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
func acceptConnectionInBackgroundAndNotify()
```

```objc
- (void) acceptConnectionInBackgroundAndNotify;
```

#### Discussion

This method asynchronously creates a file handle for the other end of the socket connection and returns that object by posting a [`NSFileHandleConnectionAccepted`](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) notification in the current thread. The notification includes a `userInfo` dictionary with the created `NSFileHandle` object, which is accessible using the `NSFileHandleNotificationFileHandleItem` key.

You must call this method from a thread that has an active run loop.

##### Special Considerations

The receiver must be created by an [`init(fileDescriptor:)`](./init%28filedescriptor%29.md) message that takes as an argument a stream-type socket created by the appropriate system routine, *and that is being listened on*. In other words, you must `bind()` the socket, and ensure that the socket has a connection backlog defined by `listen()`.

The object that will write data to the returned file handle must add itself as an observer of [`NSFileHandleConnectionAccepted`](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md).

Note that this method does not continue to listen for connection requests after it posts [`NSFileHandleConnectionAccepted`](../nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md). If you want to keep getting notified, you need to call [`acceptConnectionInBackgroundAndNotify()`](./acceptconnectioninbackgroundandnotify%28%29.md) again in your observer method.

## See Also

### Related Documentation
- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](../notificationqueue/enqueue%28_,postingstyle,coalescemask,formodes%29.md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
### Reading asynchronously with notifications
- [func acceptConnectionInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](./acceptconnectioninbackgroundandnotify%28formodes%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/acceptconnectioninbackgroundandnotify())*