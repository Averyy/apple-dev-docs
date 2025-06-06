# acceptConnectionInBackgroundAndNotify(forModes:)

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
func acceptConnectionInBackgroundAndNotify(forModes modes: [RunLoop.Mode]?)
```

#### Discussion

See [`acceptConnectionInBackgroundAndNotify()`](filehandle/acceptconnectioninbackgroundandnotify().md) for details of how this method operates. This method differs from [`acceptConnectionInBackgroundAndNotify()`](filehandle/acceptconnectioninbackgroundandnotify().md) in that `modes` specifies the run-loop mode (or modes) in which [`NSFileHandleConnectionAccepted`](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) can be posted.

You must call this method from a thread that has an active run loop.

## Parameters

- `modes`: The runloop modes in which the connection accepted notification can be posted.

## See Also

- [func enqueue(Notification, postingStyle: NotificationQueue.PostingStyle, coalesceMask: NotificationQueue.NotificationCoalescing, forModes: [RunLoop.Mode]?)](notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:).md)
  Adds a notification to the notification queue with a specified posting style, criteria for coalescing, and run loop mode.
- [func acceptConnectionInBackgroundAndNotify()](filehandle/acceptconnectioninbackgroundandnotify.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/acceptconnectioninbackgroundandnotify(formodes:))*