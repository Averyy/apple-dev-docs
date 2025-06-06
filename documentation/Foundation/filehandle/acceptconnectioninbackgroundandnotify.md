# acceptConnectionInBackgroundAndNotify()

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

This method asynchronously creates a file handle for the other end of the socket connection and returns that object by posting a [`NSFileHandleConnectionAccepted`](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) notification in the current thread. The notification includes a `userInfo` dictionary with the created `NSFileHandle` object, which is accessible using the `NSFileHandleNotificationFileHandleItem` key.

You must call this method from a thread that has an active run loop.

##### Special Considerations

The receiver must be created by an [`init(fileDescriptor:)`](filehandle/init(filedescriptor:).md) message that takes as an argument a stream-type socket created by the appropriate system routine, . In other words, you must `bind()` the socket, and ensure that the socket has a connection backlog defined by `listen()`.

The object that will write data to the returned file handle must add itself as an observer of [`NSFileHandleConnectionAccepted`](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md).

Note that this method does not continue to listen for connection requests after it posts [`NSFileHandleConnectionAccepted`](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md). If you want to keep getting notified, you need to call [`acceptConnectionInBackgroundAndNotify()`](filehandle/acceptconnectioninbackgroundandnotify().md) again in your observer method.

## See Also

- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:).md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [func acceptConnectionInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](filehandle/acceptconnectioninbackgroundandnotify(formodes:).md)
  Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
- [func readInBackgroundAndNotify()](filehandle/readinbackgroundandnotify.md)
  Reads from the file or communications channel in the background and posts a notification when finished.
- [func readInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](filehandle/readinbackgroundandnotify(formodes:).md)
  Reads from the file or communications channel in the background and posts a notification when finished.
- [func readToEndOfFileInBackgroundAndNotify()](filehandle/readtoendoffileinbackgroundandnotify.md)
  Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [func readToEndOfFileInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](filehandle/readtoendoffileinbackgroundandnotify(formodes:).md)
  Reads to the end of file from the file or communications channel in the background and posts a notification when finished.
- [func waitForDataInBackgroundAndNotify()](filehandle/waitfordatainbackgroundandnotify.md)
  Asynchronously checks to see if data is available.
- [func waitForDataInBackgroundAndNotify(forModes: [RunLoop.Mode]?)](filehandle/waitfordatainbackgroundandnotify(formodes:).md)
  Asynchronously checks to see if data is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/acceptconnectioninbackgroundandnotify())*