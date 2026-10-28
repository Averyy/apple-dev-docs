# FileHandle.ReadCompletionMessage

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A message a file handle sends when it reads the data currently available in a file or a communication channel.

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
struct ReadCompletionMessage
```

## Overview

Before adding an observer for this message type, call either [`readInBackgroundAndNotify()`](./readinbackgroundandnotify%28%29.md) or [`readInBackgroundAndNotify(forModes:)`](./readinbackgroundandnotify%28formodes%29.md) on an appropriate [`FileHandle`](../filehandle.md) object.

Observe this message with the identifier [`readCompletion`](../notificationcenter/messageidentifier/readcompletion.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](../notificationcenter/mainactormessage/subject.md) of this message type is [`FileHandle`](../filehandle.md).

This message interoperates with the notification [`readCompletionNotification`](./readcompletionnotification.md). The system notifies observers of the message when the [`NotificationCenter`](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init(dataItem: Result<Data, POSIXError>)](./readcompletionmessage/init%28dataitem%29.md)
  Creates a message that indicates a file handle read data.
### Working with message properties
- [var dataItem: Result<Data, POSIXError>](./readcompletionmessage/dataitem.md)
  A result instance containing either the data read from the file or connection, or else an error.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with notification messages
- [FileHandle.ConnectionAcceptedMessage](./connectionacceptedmessage.md)
  A message a file handle sends when it creates a socket connection between two processes and creates a file handle for one end of the connection.
- [FileHandle.DataAvailableMessage](./dataavailablemessage.md)
  A message a file handle sends when it determines data is available for reading from a file or communications channel.
- [FileHandle.ReadToEndOfFileCompletionMessage](./readtoendoffilecompletionmessage.md)
  A message a file handle sends when it reads all data in a file, or another process in a communication channel signals the end of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/readcompletionmessage)*