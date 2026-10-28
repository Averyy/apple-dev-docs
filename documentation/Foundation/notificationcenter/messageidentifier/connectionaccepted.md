# connectionAccepted

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An identifier for a message about a file handle accepting a connection.

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
static var connectionAccepted: NotificationCenter.BaseMessageIdentifier<FileHandle.ConnectionAcceptedMessage> { get }
```

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<FileHandle.ConnectionAcceptedMessage>`.

## Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`FileHandle.ConnectionAcceptedMessage`](../../filehandle/connectionacceptedmessage.md).

## See Also

### Identifying file handle messages
- [static var dataAvailable: NotificationCenter.BaseMessageIdentifier<FileHandle.DataAvailableMessage>](./dataavailable.md)
  An identifier for a message about a file handle having data available for reading.
- [static var readToEndOfFileCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadToEndOfFileCompletionMessage>](./readtoendoffilecompletion.md)
  An identifier for a message about a file handle having reached the end of a file or communication channel.
- [static var readCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadCompletionMessage>](./readcompletion.md)
  An identifier for a message about a file handle having read the currently available data from a file or communication channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/connectionaccepted)*