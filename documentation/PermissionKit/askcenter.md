# AskCenter

**Framework**: PermissionKit  
**Kind**: class

A class that manages permission requests you send to parents or guardians for approval.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.2+

## Declaration

```swift
final class AskCenter
```

#### Overview

Use `AskCenter` to send permission questions to parents or guardians when a person needs approval for app communication permissions or significant updates. The system routes your questions through the appropriate family sharing channels and delivers responses back to your app when parents make their decisions.

Access the shared instance to send permission requests and register for response notifications. The system handles the underlying communication with parents and manages the approval workflow automatically.

## Topics

### Getting the shared instance
- [static let shared: AskCenter](askcenter/shared.md)
  The shared instance you use to send permission requests and receive responses.
### Making permission requests
- [func ask(PermissionQuestion<SignificantAppUpdateTopic>, in: NSWindow) async throws](askcenter/ask(_:in:)-39vi7.md)
  Tells the system to request that the person send the communication permission question to the person’s parent or guardian.
- [func ask(PermissionQuestion<CommunicationTopic>, in: NSWindow) async throws](askcenter/ask(_:in:)-3znb6.md)
  Tells the system to request that the person send the communication permission question to the person’s parent or guardian.
- [func ask(PermissionQuestion<CommunicationTopic>, in: UIViewController) async throws](askcenter/ask(_:in:)-6xupo.md)
  Tells the system to request that a person send the communication permission question to the person’s parent or guardian.
- [func ask(PermissionQuestion<SignificantAppUpdateTopic>, in: UIViewController) async throws](askcenter/ask(_:in:)-8ks48.md)
  Tells the system to request that a person send the the significant app update permission question to their parent or guardian.
### Receiving responses
- [func responses<Topic>(for: Topic.Type) -> some AsyncSequence<PermissionResponse<Topic>, Never>
](askcenter/responses(for:).md)
  Registers the topic type with the system and returns an asynchronous sequence of responses.

## See Also

- [Creating a communication experience](creating-a-communication-experience.md)
  Request permission from a parent or guardian to modify a child’s communication rules.
- [class PermissionQuestion](permissionquestion.md)
  A class that captures a permission question posed by a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askcenter)*