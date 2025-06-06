# LocalTestingInvocationEncoder

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
struct LocalTestingInvocationEncoder
```

## Topics

### Instance Methods
- [func doneRecording() throws](localtestinginvocationencoder/donerecording.md)
  Invoked to signal to the encoder that no further `record...` calls will be made on it.
- [func recordArgument<Value>(RemoteCallArgument<Value>) throws](localtestinginvocationencoder/recordargument(_:).md)
  Record an argument of `Argument` type. This will be invoked for every argument of the target, in declaration order.
- [func recordErrorType<E>(E.Type) throws](localtestinginvocationencoder/recorderrortype(_:).md)
  Record the error type of the distributed method. This method will not be invoked if the target is not throwing.
- [func recordGenericSubstitution<T>(T.Type) throws](localtestinginvocationencoder/recordgenericsubstitution(_:).md)
  The arguments must be encoded order-preserving, and once `decodeGenericSubstitutions` is called, the substitutions must be returned in the same order in which they were recorded.
- [func recordReturnType<R>(R.Type) throws](localtestinginvocationencoder/recordreturntype(_:).md)
  Record the return type of the distributed method. This method will not be invoked if the target is returning `Void`.
### Type Aliases
- [LocalTestingInvocationEncoder.SerializationRequirement](localtestinginvocationencoder/serializationrequirement.md)
  The serialization requirement that the types passed to `recordArgument` and `recordReturnType` are required to conform to.

## Relationships

### Conforms To
- [DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md)

## See Also

- [class LocalTestingDistributedActorSystem](localtestingdistributedactorsystem.md)
  A `DistributedActorSystem` designed for local only testing.
- [struct LocalTestingActorID](localtestingactorid.md)
- [typealias LocalTestingActorAddress](localtestingactoraddress.md)
- [class LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)
- [struct LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationencoder)*