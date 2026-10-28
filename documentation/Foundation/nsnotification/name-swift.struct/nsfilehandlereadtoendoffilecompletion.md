# NSFileHandleReadToEndOfFileCompletion

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted when the file handle reads all data in the file or, in a communications channel, until the other process signals the end of data.

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
static let NSFileHandleReadToEndOfFileCompletion: NSNotification.Name
```

```c
extern NSNotificationName const NSFileHandleReadToEndOfFileCompletionNotification;
```

## Discussion

It makes the data available to observers by putting it in the `userInfo` dictionary. To cause the posting of this notification, you must send either [`readToEndOfFileInBackgroundAndNotify()`](../../filehandle/readtoendoffileinbackgroundandnotify%28%29.md) or [`readToEndOfFileInBackgroundAndNotify(forModes:)`](../../filehandle/readtoendoffileinbackgroundandnotify%28formodes%29.md) to an appropriate `NSFileHandle` object.

The notification object is the `NSFileHandle` object that sent the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `NSFileHandleNotificationDataItem` | An `NSData` object containing the available data read from a socket connection. |
| `@"NSFileHandleError"` | An `NSNumber` object containing an integer representing the UNIX-type error which occurred. |

## See Also

### Working with notifications
- [static let NSFileHandleConnectionAccepted: NSNotification.Name](./nsfilehandleconnectionaccepted.md)
  Posted when a file handle object establishes a socket connection between two processes, creates a file handle object for one end of the connection, and makes this object available to observers.
- [static let NSFileHandleDataAvailable: NSNotification.Name](./nsfilehandledataavailable.md)
  Posted when the file handle determines that data is currently available for reading in a file or at a communications channel.
- [class let readCompletionNotification: NSNotification.Name](../../filehandle/readcompletionnotification.md)
  Posted when the file handle reads the data currently available in a file or at a communications channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion)*