# didTerminate

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An identifier for a message about a stopped task.

**Availability**:
- macOS 26.0+

## Declaration

```swift
static var didTerminate: NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage> { get }
```

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage>`.

## Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`Process.DidTerminateMessage`](../../process/didterminatemessage.md).

## See Also

### Identifying process info messages
- [static var powerStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.PowerStateDidChangeMessage>](./powerstatedidchange.md)
  An identifier for a message about a power state change.
- [static var thermalStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.ThermalStateDidChangeMessage>](./thermalstatedidchange.md)
  An identifier for a message about a thermal state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didterminate)*