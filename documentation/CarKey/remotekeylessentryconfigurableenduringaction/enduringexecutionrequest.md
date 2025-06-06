# RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest

**Framework**: CarKey  
**Kind**: class

An object that reports the results of an action with an optional stopping point.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
@objc
final class EnduringExecutionRequest
```

#### Overview

When you perform an action, the system creates a [`RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest`](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest.md) object for your request and returns it to your app. Use the object to send a follow-up request to stop the action. You can also use it to determine the status of the original action.

## Topics

### Structures
- [RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest.ContinuationRequest](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/continuationrequest.md)
  Continuation Request
### Instance Properties
- [var eventStream: AsyncStream<RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest.Event>](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/eventstream.md)
  The asynchronous event stream on which Continuation Requests are sent
### Instance Methods
- [func results() async throws -> ExecutionStatus](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/results.md)
  Returns the results of a preceding action request.
- [func stop() throws](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/stop.md)
  Sends a request to stop a previously started action.
### Enumerations
- [RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest.Event](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/event.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryconfigurableenduringaction/enduringexecutionrequest)*