# NSFileHandleConnectionAccepted

**Framework**: Foundation  
**Kind**: property

Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.

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
static let NSFileHandleConnectionAccepted: NSNotification.Name
```

#### Discussion

To cause the posting of this notification, you must send either [`acceptConnectionInBackgroundAndNotify()`](filehandle/acceptconnectioninbackgroundandnotify().md) or [`acceptConnectionInBackgroundAndNotify(forModes:)`](filehandle/acceptconnectioninbackgroundandnotify(formodes:).md) to an `NSFileHandle` object representing a server stream-type socket.

The notification object is the `NSFileHandle` object that sent the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `NSFileHandleNotificationFileHandleItem` | The `NSFileHandle` object representing the “near” end of a socket connection. |
| `@"NSFileHandleError"` | An `NSNumber` object containing an integer representing the UNIX-type error which occurred. |

## See Also

- [static let NSFileHandleDataAvailable: NSNotification.Name](nsnotification/name-swift.struct/nsfilehandledataavailable.md)
  Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [class let readCompletionNotification: NSNotification.Name](filehandle/readcompletionnotification.md)
  Posted when the file handle reads the data currently available in a file or at a communications channel.
- [static let NSFileHandleReadToEndOfFileCompletion: NSNotification.Name](nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion.md)
  Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsfilehandleconnectionaccepted)*