# NSFileHandleNotificationFileHandleItem

**Framework**: Foundation  
**Kind**: var

A key in the userinfo dictionary in a [`NSFileHandleConnectionAccepted`](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md) notification.

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
let NSFileHandleNotificationFileHandleItem: String
```

#### Discussion

The corresponding value is the `NSFileHandle` object representing the “near” end of a socket connection.

## See Also

- [let NSFileHandleNotificationDataItem: String](nsfilehandlenotificationdataitem.md)
  A key in the userinfo dictionary in a [`readCompletionNotification`](filehandle/readcompletionnotification.md) and [`NSFileHandleReadToEndOfFileCompletion`](nsnotification/name-swift.struct/nsfilehandlereadtoendoffilecompletion.md).
- [let NSFileHandleNotificationMonitorModes: String](nsfilehandlenotificationmonitormodes.md)
  Currently unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilehandlenotificationfilehandleitem)*