# waitForDataInBackgroundAndNotify(forModes:)

**Framework**: Foundation  
**Kind**: method

Asynchronously checks to see if data is available.

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
func waitForDataInBackgroundAndNotify(forModes modes: [RunLoop.Mode]?)
```

#### Discussion

When the data becomes available, this method posts a [`NSFileHandleDataAvailable`](nsnotification/name-swift.struct/nsfilehandledataavailable.md) notification on the current thread. This method differs from [`waitForDataInBackgroundAndNotify()`](filehandle/waitfordatainbackgroundandnotify().md) in that `modes` specifies the run-loop mode (or modes) in which [`NSFileHandleDataAvailable`](nsnotification/name-swift.struct/nsfilehandledataavailable.md) can be posted.

You must call this method from a thread that has an active run loop.

## Parameters

- `modes`: The runloop modes in which the data available notification can be posted.

## See Also

- [func acceptConnectionInBackgroundAndNotify()](filehandle/acceptconnectioninbackgroundandnotify.md)
  Accepts a socket connection (for stream-type sockets only) in the background and creates a file handle for the “near” (client) end of the communications channel.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/waitfordatainbackgroundandnotify(formodes:))*