# thermalStateDidChange

**Framework**: Foundation  
**Kind**: property

An identifier for a message about a thermal state change.

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
static var thermalStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.ThermalStateDidChangeMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`ProcessInfo.ThermalStateDidChangeMessage`](processinfo/thermalstatedidchangemessage.md).

## See Also

- [static var powerStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.PowerStateDidChangeMessage>](notificationcenter/messageidentifier/powerstatedidchange.md)
  An identifier for a message about a power state change.
- [static var didTerminate: NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage>](notificationcenter/messageidentifier/didterminate.md)
  An identifier for a message about a stopped task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/thermalstatedidchange)*