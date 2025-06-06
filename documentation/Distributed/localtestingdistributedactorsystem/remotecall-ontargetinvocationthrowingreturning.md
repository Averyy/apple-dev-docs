# remoteCall(on:target:invocation:throwing:returning:)

**Framework**: Distributed  
**Kind**: method

Invoked by the Swift runtime when making a remote call.

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
final func remoteCall<Act, Err, Res>(on actor: Act, target: RemoteCallTarget, invocation: inout LocalTestingDistributedActorSystem.InvocationEncoder, throwing errorType: Err.Type, returning returnType: Res.Type) async throws -> Res where Act : DistributedActor, Err : Error, Res : Decodable, Res : Encodable, Act.ID == LocalTestingActorID
```

#### Discussion

The `arguments` are the arguments container that was previously created by `makeInvocationEncoder` and has been populated with all arguments.

This method should perform the actual remote function call, and await for its response.

#### Serialization Requirement

Implementations of this method must ensure that the `Argument` type parameter conforms to the types’ `SerializationRequirement`.

#### Errors

This method is allowed to throw because of underlying transport or serialization errors, as well as by re-throwing the error received from the remote callee (if able to).


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem/remotecall(on:target:invocation:throwing:returning:))*