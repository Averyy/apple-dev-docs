# CommunicationLimits

**Framework**: PermissionKit  
**Kind**: class

A type that encapsulates the communication limits for your app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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

### Registering communication and requesting authorization
- [var updates: some AsyncSequence<PermissionResponse<CommunicationTopic>, Never>](communicationlimits/updates.md)
  Registers the communication topic with the system, so your app can be launched on-demand in the background to receive permission updates.
- [static let current: CommunicationLimits](communicationlimits/current.md)
  The singleton app instance.
### Instance Methods
- [func ask(PermissionQuestion<CommunicationTopic>, in: UIViewController) async throws](communicationlimits/ask(_:in:)-5ou06.md)
  Requests that a child send the communication permission question to their parent or guardian.
- [func ask(PermissionQuestion<CommunicationTopic>, in: NSWindow) async throws](communicationlimits/ask(_:in:)-5tzyy.md)
  Tells the system to request that the user send the communication permission question to the user’s parent/s and/or guardian/s. Throws an error if the system was unable to request the user to send the question.
- [func isKnownHandle(CommunicationHandle) async -> Bool](communicationlimits/isknownhandle(_:).md)
  A Boolean that checks if the system knows the given handle.
- [func knownHandles(in: Set<CommunicationHandle>) async -> Set<CommunicationHandle>](communicationlimits/knownhandles(in:).md)
  Checks which handles in a given set are known to the system.

## See Also

- [struct CommunicationHandle](communicationhandle.md)
  A piece of identifying information that can be used to communicate with someone.
- [struct PermissionResponse](permissionresponse.md)
  A full permission response that includes the original question and chosen answer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits)*