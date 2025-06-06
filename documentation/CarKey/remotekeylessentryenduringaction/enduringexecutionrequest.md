# RemoteKeylessEntryEnduringAction.EnduringExecutionRequest

**Framework**: CarKey  
**Kind**: class

An object that reports the results of an action with an optional stopping point.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
final class EnduringExecutionRequest
```

#### Overview

When you perform an action, the system creates a [`RemoteKeylessEntryEnduringAction.EnduringExecutionRequest`](remotekeylessentryenduringaction/enduringexecutionrequest.md) object for your request and returns it to your app. Use the object to send a follow-up request to stop the action. You can also use it to determine the status of the original action.

## Topics

### Getting the Vehicle’s Respose
- [func results() async throws -> ExecutionStatus](remotekeylessentryenduringaction/enduringexecutionrequest/results.md)
  Returns the results of a preceding action request.
- [struct ExecutionStatus](executionstatus.md)
  A type that contains the status code a vehicle returns after executing an action.
### Cancelling an Action
- [func stop() throws](remotekeylessentryenduringaction/enduringexecutionrequest/stop.md)
  Sends a request to stop a previously started action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction/enduringexecutionrequest)*