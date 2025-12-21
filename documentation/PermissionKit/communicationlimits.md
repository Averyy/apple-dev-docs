# CommunicationLimits

**Framework**: PermissionKit  
**Kind**: class

A type that encapsulates the communication limits for your app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class CommunicationLimits
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

#### Overview

Obtain an `AsyncSequence` to handle communication permission responses after launching your app.

```swift
let responses = CommunicationLimits.current.updates
for await response in responses {
   print("Received a communication permission response: \(response)")
}
```

## Topics

### Accessing communication limits
- [static let current: CommunicationLimits](communicationlimits/current.md)
  The singleton app instance.
### Checking known handles
- [func isKnownHandle(CommunicationHandle) async -> Bool](communicationlimits/isknownhandle(_:).md)
  A Boolean that checks if the system knows the given handle.
- [func knownHandles(in: Set<CommunicationHandle>) async -> Set<CommunicationHandle>](communicationlimits/knownhandles(in:).md)
  Checks which handles in a given set are known to the system.
### Deprecated APIs
- [var updates: some AsyncSequence<PermissionResponse<CommunicationTopic>, Never>](communicationlimits/updates.md)
  Registers the communication topic with the system, so your app can be launched on-demand in the background to receive permission updates.
- [func ask(PermissionQuestion<CommunicationTopic>, in: NSWindow) async throws](communicationlimits/ask(_:in:)-5tzyy.md)
  Tells the system to request that the user send the communication permission question to the user’s parent/s and/or guardian/s. Throws an error if the system was unable to request the user to send the question.
- [func ask(PermissionQuestion<CommunicationTopic>, in: UIViewController) async throws](communicationlimits/ask(_:in:)-5ou06.md)
  Requests that a child send the communication permission question to their parent or guardian.

## See Also

- [func responses<Topic>(for: Topic.Type) -> some AsyncSequence<PermissionResponse<Topic>, Never>
](askcenter/responses(for:).md)
  Registers the topic type with the system and returns an asynchronous sequence of responses.
- [struct PermissionResponse](permissionresponse.md)
  A full permission response that includes the original question and chosen answer.
- [struct CommunicationHandle](communicationhandle.md)
  Contact information for identifying and communicating with a person.
- [struct PermissionChoice](permissionchoice.md)
  A class that uniquely identifies a specific, statically defined permission choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits)*