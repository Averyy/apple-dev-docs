# DistributedTargetInvocationResultHandler

**Framework**: Distributed  
**Kind**: protocol

Protocol a distributed invocation execution’s result handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol DistributedTargetInvocationResultHandler<SerializationRequirement>
```

#### Overview

An instance conforming to this type must be passed when invoking `executeDistributedTarget(on:target:invocationDecoder:handler:)` while handling an incoming distributed call.

The handler will then be invoked with the return value (or error) that the invoked target returned (or threw).

## Topics

### Associated Types
- [associatedtype SerializationRequirement](distributedtargetinvocationresulthandler/serializationrequirement.md)
  The serialization requirement that the value passed to `onReturn` is required to conform to.
### Instance Methods
- [func onReturn<Success>(value: Success) async throws](distributedtargetinvocationresulthandler/onreturn(value:).md)
  Invoked when the distributed target execution returns successfully. The `value` is the return value of the executed distributed invocation target.
- [func onReturnVoid() async throws](distributedtargetinvocationresulthandler/onreturnvoid.md)
  Invoked when the distributed target execution of a `Void` returning function has completed successfully.
- [func onThrow<Err>(error: Err) async throws](distributedtargetinvocationresulthandler/onthrow(error:).md)
  Invoked when the distributed target execution of a target has thrown an error.

## Relationships

### Conforming Types
- [LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)

## See Also

- [struct RemoteCallTarget](remotecalltarget.md)
  Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.
- [struct RemoteCallArgument](remotecallargument.md)
  Represents an argument passed to a distributed call target.
- [protocol DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md)
  Used to encode an invocation of a distributed target (method or computed property).
- [protocol DistributedTargetInvocationDecoder](distributedtargetinvocationdecoder.md)
  Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationresulthandler)*