# remoteCall(on:target:invocation:throwing:returning:)

**Framework**: Distributed  
**Kind**: method  
**Required**: Yes

Invoked by the Swift runtime when making a remote call.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func remoteCall<Act, Err, Res>(on actor: Act, target: RemoteCallTarget, invocation: inout Self.InvocationEncoder, throwing: Err.Type, returning: Res.Type) async throws -> Res where Act : DistributedActor, Err : Error, Self.ActorID == Act.ID
```

#### Discussion

The `arguments` are the arguments container that was previously created by `makeInvocationEncoder` and has been populated with all arguments.

This method should perform the actual remote function call, and await for its response.

#### Serialization Requirement

Implementations of this method must ensure that the `Argument` type parameter conforms to the types’ `SerializationRequirement`.

#### Errors

This method is allowed to throw because of underlying transport or serialization errors, as well as by re-throwing the error received from the remote callee (if able to).


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorsystem/remotecall(on:target:invocation:throwing:returning:))*