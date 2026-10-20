# RemoteKeylessEntryAction.ExecutionRequest

**Framework**: CarKey  
**Kind**: class  
**Role**: Class

An object that reports the results of an automatically ending action asynchronously.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
final class ExecutionRequest
```

#### Overview

When you perform an action, the system creates a [`RemoteKeylessEntryAction.ExecutionRequest`](./executionrequest.md) object for that request and returns it to your app. Use that object to asynchronously determine whether your request completed successfully or reported an error.

## Topics

### Getting the Vehicle’s Response
- [func results() async throws -> ExecutionStatus](./executionrequest/results%28%29.md)
  Returns the results of a preceding action request.
- [struct ExecutionStatus](../executionstatus.md)
  A type that contains the status code a vehicle returns after executing an action.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryaction/executionrequest)*