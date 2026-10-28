# RemoteKeylessEntryEnduringAction.EnduringExecutionRequest

**Framework**: CarKey  
**Kind**: class  
**Role**: Class

An object that reports the results of an action with an optional stopping point.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.3+ - Deprecated in 15.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`perform(_:continuationStrategy:)`](../carkeyremotecontrolsession/perform%28_,continuationstrategy%29.md) instead.

## Declaration

```swift
final class EnduringExecutionRequest
```

## Overview

When you perform an action, the system creates a [`RemoteKeylessEntryEnduringAction.EnduringExecutionRequest`](./enduringexecutionrequest.md) object for your request and returns it to your app. Use the object to send a follow-up request to stop the action. You can also use it to determine the status of the original action.

## Topics

### Getting the Vehicle’s Response
- [func results() async throws -> ExecutionStatus](./enduringexecutionrequest/results%28%29.md)
  Returns the results of a preceding action request.
- [struct ExecutionStatus](../executionstatus.md)
  A type that contains the status code a vehicle returns after executing an action.
### Cancelling an Action
- [func stop() throws](./enduringexecutionrequest/stop%28%29.md)
  Sends a request to stop a previously started action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction/enduringexecutionrequest)*