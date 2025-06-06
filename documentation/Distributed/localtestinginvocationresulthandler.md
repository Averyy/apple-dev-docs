# LocalTestingInvocationResultHandler

**Framework**: Distributed  
**Kind**: struct

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
struct LocalTestingInvocationResultHandler
```

## Topics

### Instance Methods
- [func onReturn<Success>(value: Success) async throws](localtestinginvocationresulthandler/onreturn(value:).md)
  Invoked when the distributed target execution returns successfully. The `value` is the return value of the executed distributed invocation target.
- [func onReturnVoid() async throws](localtestinginvocationresulthandler/onreturnvoid.md)
  Invoked when the distributed target execution of a `Void` returning function has completed successfully.
- [func onThrow<Err>(error: Err) async throws](localtestinginvocationresulthandler/onthrow(error:).md)
  Invoked when the distributed target execution of a target has thrown an error.
### Type Aliases
- [LocalTestingInvocationResultHandler.SerializationRequirement](localtestinginvocationresulthandler/serializationrequirement.md)
  The serialization requirement that the value passed to `onReturn` is required to conform to.

## Relationships

### Conforms To
- [DistributedTargetInvocationResultHandler](distributedtargetinvocationresulthandler.md)

## See Also

- [class LocalTestingDistributedActorSystem](localtestingdistributedactorsystem.md)
  A `DistributedActorSystem` designed for local only testing.
- [struct LocalTestingActorID](localtestingactorid.md)
- [typealias LocalTestingActorAddress](localtestingactoraddress.md)
- [struct LocalTestingInvocationEncoder](localtestinginvocationencoder.md)
- [class LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationresulthandler)*