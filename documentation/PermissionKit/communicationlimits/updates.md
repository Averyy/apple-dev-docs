# updates

**Framework**: PermissionKit  
**Kind**: property  
**Role**: Instance Property

Registers the communication topic with the system, so your app can be launched on-demand in the background to receive permission updates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

> **Deprecated**: Use AskCenter.responses(for:) instead.

## Declaration

```swift
final var updates: some AsyncSequence<PermissionResponse<CommunicationTopic>, Never> { get }
```

## Mentions

- [Creating a communication experience](../creating-a-communication-experience.md)

## See Also

### Deprecated APIs
- [func ask(PermissionQuestion<CommunicationTopic>, in: NSWindow) async throws](./ask%28_,in%29-5tzyy.md)
  Tells the system to request that the user send the communication permission question to the user’s parent/s and/or guardian/s. Throws an error if the system was unable to request the user to send the question.
- [func ask(PermissionQuestion<CommunicationTopic>, in: UIViewController) async throws](./ask%28_,in%29-5ou06.md)
  Requests that a child send the communication permission question to their parent or guardian.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/updates)*