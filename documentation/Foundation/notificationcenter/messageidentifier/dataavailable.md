# dataAvailable

**Framework**: Foundation  
**Kind**: property

An identifier for a message about a file handle having data available for reading.

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
static var dataAvailable: NotificationCenter.BaseMessageIdentifier<FileHandle.DataAvailableMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`FileHandle.DataAvailableMessage`](filehandle/dataavailablemessage.md).

## See Also

- [static var connectionAccepted: NotificationCenter.BaseMessageIdentifier<FileHandle.ConnectionAcceptedMessage>](notificationcenter/messageidentifier/connectionaccepted.md)
  An identifier for a message about a file handle accepting a connection.
- [static var readToEndOfFileCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadToEndOfFileCompletionMessage>](notificationcenter/messageidentifier/readtoendoffilecompletion.md)
  An identifier for a message about a file handle having reached the end of a file or communication channel.
- [static var readCompletion: NotificationCenter.BaseMessageIdentifier<FileHandle.ReadCompletionMessage>](notificationcenter/messageidentifier/readcompletion.md)
  An identifier for a message about a file handle having read the currently available data from a file or communication channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/dataavailable)*