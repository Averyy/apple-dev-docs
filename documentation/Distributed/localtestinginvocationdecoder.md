# LocalTestingInvocationDecoder

**Framework**: Distributed  
**Kind**: class

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
final class LocalTestingInvocationDecoder
```

## Topics

### Instance Methods
- [func decodeErrorType() throws -> (any Any.Type)?](localtestinginvocationdecoder/decodeerrortype.md)
  Decode the specific error type that the distributed invocation target has recorded. Currently this effectively can only ever be `Error.self`.
- [func decodeGenericSubstitutions() throws -> [any Any.Type]](localtestinginvocationdecoder/decodegenericsubstitutions.md)
  Decode all generic substitutions that were recorded for this invocation.
- [func decodeNextArgument<Argument>() throws -> Argument](localtestinginvocationdecoder/decodenextargument.md)
  Attempt to decode the next argument from the underlying buffers into pre-allocated storage pointed at by ‘pointer’.
- [func decodeReturnType() throws -> (any Any.Type)?](localtestinginvocationdecoder/decodereturntype.md)
  Attempt to decode the known return type of the distributed invocation.
### Type Aliases
- [LocalTestingInvocationDecoder.SerializationRequirement](localtestinginvocationdecoder/serializationrequirement.md)
  The serialization requirement that the types passed to `decodeNextArgument` are required to conform to. The type returned by `decodeReturnType` is also expected to conform to this associated type requirement.

## Relationships

### Conforms To
- [DistributedTargetInvocationDecoder](distributedtargetinvocationdecoder.md)

## See Also

- [class LocalTestingDistributedActorSystem](localtestingdistributedactorsystem.md)
  A `DistributedActorSystem` designed for local only testing.
- [struct LocalTestingActorID](localtestingactorid.md)
- [typealias LocalTestingActorAddress](localtestingactoraddress.md)
- [struct LocalTestingInvocationEncoder](localtestinginvocationencoder.md)
- [struct LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationdecoder)*