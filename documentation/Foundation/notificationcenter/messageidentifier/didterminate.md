# didTerminate

**Framework**: Foundation  
**Kind**: property

An identifier for a message about a stopped task.

**Availability**:
- macOS 26.0+

## Declaration

```swift
static var didTerminate: NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`Process.DidTerminateMessage`](process/didterminatemessage.md).

## See Also

- [static var powerStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.PowerStateDidChangeMessage>](notificationcenter/messageidentifier/powerstatedidchange.md)
  An identifier for a message about a power state change.
- [static var thermalStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.ThermalStateDidChangeMessage>](notificationcenter/messageidentifier/thermalstatedidchange.md)
  An identifier for a message about a thermal state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didterminate)*