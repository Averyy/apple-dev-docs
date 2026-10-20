# powerStateDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An identifier for a message about a power state change.

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
static var powerStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.PowerStateDidChangeMessage> { get }
```

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<ProcessInfo.PowerStateDidChangeMessage>`.

#### Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`ProcessInfo.PowerStateDidChangeMessage`](../../processinfo/powerstatedidchangemessage.md).

## See Also

### Identifying process info messages
- [static var thermalStateDidChange: NotificationCenter.BaseMessageIdentifier<ProcessInfo.ThermalStateDidChangeMessage>](./thermalstatedidchange.md)
  An identifier for a message about a thermal state change.
- [static var didTerminate: NotificationCenter.BaseMessageIdentifier<Process.DidTerminateMessage>](./didterminate.md)
  An identifier for a message about a stopped task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/powerstatedidchange)*