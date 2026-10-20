# ask(_:in:)

**Framework**: PermissionKit  
**Kind**: method  
**Role**: Instance Method

Requests that a child send the communication permission question to their parent or guardian.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

> **Deprecated**: Use AskCenter.ask(_:in:) instead.

## Declaration

```swift
final func ask(_ question: PermissionQuestion<CommunicationTopic>, in viewController: UIViewController) async throws
```

#### Discussion

Throws an error if the system can’t request a child to send the permission question.

## Parameters

- `question`: The question that the system requests the child send.
- `viewController`: The view controller to which to anchor and present system UI.

## See Also

### Deprecated APIs
- [var updates: some AsyncSequence<PermissionResponse<CommunicationTopic>, Never>](./updates.md)
  Registers the communication topic with the system, so your app can be launched on-demand in the background to receive permission updates.
- [func ask(PermissionQuestion<CommunicationTopic>, in: NSWindow) async throws](./ask%28_,in%29-5tzyy.md)
  Tells the system to request that the user send the communication permission question to the user’s parent/s and/or guardian/s. Throws an error if the system was unable to request the user to send the question.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/ask(_:in:)-5ou06)*