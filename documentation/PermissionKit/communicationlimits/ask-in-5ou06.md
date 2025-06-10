# ask(_:in:)

**Framework**: PermissionKit  
**Kind**: method

Requests that a child send the communication permission question to their parent or guardian.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func ask(_ question: PermissionQuestion<CommunicationTopic>, in viewController: UIViewController) async throws
```

#### Discussion

Throws an error if the system can’t request a child to send the permission question.

## Parameters

- `question`: The question that the system requests the child send.
- `viewController`: The view controller to which to anchor and present system UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/ask(_:in:)-5ou06)*