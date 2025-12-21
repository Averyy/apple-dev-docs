# ask(_:in:)

**Framework**: PermissionKit  
**Kind**: method

Tells the system to request that the user send the communication permission question to the user’s parent/s and/or guardian/s. Throws an error if the system was unable to request the user to send the question.

**Availability**:
- macOS 26.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
final func ask(_ question: PermissionQuestion<CommunicationTopic>, in window: NSWindow) async throws
```

## Parameters

- `question`: The question to request send of.
- `window`: The window to anchor and present system UI off of.

## See Also

- [var updates: some AsyncSequence<PermissionResponse<CommunicationTopic>, Never>](communicationlimits/updates.md)
  Registers the communication topic with the system, so your app can be launched on-demand in the background to receive permission updates.
- [func ask(PermissionQuestion<CommunicationTopic>, in: UIViewController) async throws](communicationlimits/ask(_:in:)-5ou06.md)
  Requests that a child send the communication permission question to their parent or guardian.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/ask(_:in:)-5tzyy)*