# FileHandle.ConnectionAcceptedMessage

**Framework**: Foundation  
**Kind**: struct

A message a file handle sends when it creates a socket connection between two processes and creates a file handle for one end of the connection.

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
struct ConnectionAcceptedMessage
```

#### Overview

Before adding an observer for this message type, call either [`acceptConnectionInBackgroundAndNotify()`](filehandle/acceptconnectioninbackgroundandnotify().md) or [`acceptConnectionInBackgroundAndNotify(forModes:)`](filehandle/acceptconnectioninbackgroundandnotify(formodes:).md) on a [`FileHandle`](filehandle.md) object that represents a server stream-type socket.

Observe this message with the identifier [`connectionAccepted`](notificationcenter/messageidentifier/connectionaccepted.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`FileHandle`](filehandle.md).

This message interoperates with the notification [`NSFileHandleConnectionAccepted`](nsnotification/name-swift.struct/nsfilehandleconnectionaccepted.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init(fileHandleItem: Result<FileHandle, POSIXError>)](filehandle/connectionacceptedmessage/init(filehandleitem:).md)
  Creates a message for a file handle connection acceptance.
### Working with message properties
- [var fileHandleItem: Result<FileHandle, POSIXError>](filehandle/connectionacceptedmessage/filehandleitem.md)
  A result instance that contains either the file handle representing the “near” end of a socket connection, or an error.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [FileHandle.DataAvailableMessage](filehandle/dataavailablemessage.md)
  A message a file handle sends when it determines data is available for reading from a file or communications channel.
- [FileHandle.ReadCompletionMessage](filehandle/readcompletionmessage.md)
  A message a file handle sends when it reads the data currently available in a file or a communication channel.
- [FileHandle.ReadToEndOfFileCompletionMessage](filehandle/readtoendoffilecompletionmessage.md)
  A message a file handle sends when it reads all data in a file, or another process in a communication channel signals the end of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/connectionacceptedmessage)*