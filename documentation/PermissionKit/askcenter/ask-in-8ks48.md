# ask(_:in:)

**Framework**: PermissionKit  
**Kind**: method

Tells the system to request that a person send the the significant app update permission question to their parent or guardian.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- visionOS 26.2+

## Declaration

```swift
final func ask(_ question: PermissionQuestion<SignificantAppUpdateTopic>, in viewController: UIViewController) async throws
```

#### Overview

Throws an error if the system is unable to request to send the question.

## Parameters

- `question`: The question that the system requests the person send.
- `window`: The window to which you anchor and present system UI.

## See Also

- [func ask(PermissionQuestion<SignificantAppUpdateTopic>, in: NSWindow) async throws](askcenter/ask(_:in:)-39vi7.md)
  Tells the system to request that the person send the communication permission question to the person’s parent or guardian.
- [func ask(PermissionQuestion<CommunicationTopic>, in: NSWindow) async throws](askcenter/ask(_:in:)-3znb6.md)
  Tells the system to request that the person send the communication permission question to the person’s parent or guardian.
- [func ask(PermissionQuestion<CommunicationTopic>, in: UIViewController) async throws](askcenter/ask(_:in:)-6xupo.md)
  Tells the system to request that a person send the communication permission question to the person’s parent or guardian.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askcenter/ask(_:in:)-8ks48)*