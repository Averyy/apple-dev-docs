# ask(_:in:)

**Framework**: PermissionKit  
**Kind**: method

Tells the system to request that the user send the communication permission question to the user’s parent/s and/or guardian/s. Throws an error if the system was unable to request the user to send the question.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
final func ask(_ question: PermissionQuestion<CommunicationTopic>, in window: NSWindow) async throws
```

## Parameters

- `question`: The question to request send of.
- `window`: The window to anchor and present system UI off of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/ask(_:in:)-5tzyy)*