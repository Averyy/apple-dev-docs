# executeDistributedTarget(on:target:invocationDecoder:handler:)

**Framework**: Distributed  
**Kind**: method

Prepare and execute a call to the distributed function identified by the passed arguments, on the passed `actor`, and collect its results using the `ResultHandler`.

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
func executeDistributedTarget<Act>(on actor: Act, target: RemoteCallTarget, invocationDecoder: inout Self.InvocationDecoder, handler: Self.ResultHandler) async throws where Act : DistributedActor
```

#### Discussion

This method encapsulates multiple steps that are invoked in executing a distributed function, into one very efficient implementation. The steps involved are:

- looking up the distributed function based on its name
- decoding, in an efficient manner, all arguments from the `Args` container into a well-typed representation
- using that representation to perform the call on the target method

The reason for this API using a `ResultHandler` rather than returning values directly, is that thanks to this approach it can avoid any existential boxing, and can serve the most latency sensitive-use-cases.

> **Note**: If the target location, invocation argument decoding, or some other mismatch between them happens. In general, this method is allowed to throw in any situation that might otherwise result in an illegal or unexpected invocation being performed. ```swift
    Throws ``ExecuteDistributedTargetMissingAccessorError`` if the `target`
    does not resolve to a valid distributed function accessor, i.e. the
    call identifier is incorrect, corrupted, or simply not present in this process.
```

## Parameters

- `actor`: Actor on which the remote call should invoke the target
- `target`: The target (method) identifier that should be invoked
- `invocationDecoder`: Used to obtain all arguments to be used to perform   the target invocation
- `handler`: Used to provide a type-safe way for library code to handle   the values returned by the target invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:))*