# FileHandle.DataAvailableMessage

**Framework**: Foundation  
**Kind**: struct

A message a file handle sends when it determines data is available for reading from a file or communications channel.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct DataAvailableMessage
```

#### Overview

Before adding an observer for this message type, call either [`waitForDataInBackgroundAndNotify()`](filehandle/waitfordatainbackgroundandnotify().md) or [`waitForDataInBackgroundAndNotify(forModes:)`](filehandle/waitfordatainbackgroundandnotify(formodes:).md) on an appropriate [`FileHandle`](filehandle.md) object.

Observe this message with the identifier [`dataAvailable`](notificationcenter/messageidentifier/dataavailable.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`FileHandle`](filehandle.md).

This message interoperates with the notification [`NSFileHandleDataAvailable`](nsnotification/name-swift.struct/nsfilehandledataavailable.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](filehandle/dataavailablemessage/init.md)
  Creates a message that indicates a file handle has data available for reading.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [FileHandle.ConnectionAcceptedMessage](filehandle/connectionacceptedmessage.md)
  A message a file handle sends when it creates a socket connection between two processes and creates a file handle for one end of the connection.
- [FileHandle.ReadCompletionMessage](filehandle/readcompletionmessage.md)
  A message a file handle sends when it reads the data currently available in a file or a communication channel.
- [FileHandle.ReadToEndOfFileCompletionMessage](filehandle/readtoendoffilecompletionmessage.md)
  A message a file handle sends when it reads all data in a file, or another process in a communication channel signals the end of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/dataavailablemessage)*