# DistributedActorCodingError

**Framework**: Distributed  
**Kind**: struct

Error thrown by distributed actor systems while encountering encoding/decoding issues.

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
struct DistributedActorCodingError
```

#### Overview

Also thrown when an attempt to decode [`DistributedActor`](distributedactor.md) is made, but no [`DistributedActorSystem`](distributedactorsystem.md) is available in the `Decoder`’s `userInfo[.actorSystemKey]`, as it is required to perform the resolve call.

## Topics

### Initializers
- [init(message: String)](distributedactorcodingerror/init(message:).md)
### Instance Properties
- [let message: String](distributedactorcodingerror/message.md)
### Type Methods
- [static func missingActorSystemUserInfo<Act>(Act.Type) -> DistributedActorCodingError](distributedactorcodingerror/missingactorsystemuserinfo(_:).md)

## Relationships

### Conforms To
- [DistributedActorSystemError](distributedactorsystemerror.md)
- [Error](../swift/error.md)
- [Sendable](../swift/sendable.md)

## See Also

- [protocol DistributedActorSystemError](distributedactorsystemerror.md)
  Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [struct ExecuteDistributedTargetError](executedistributedtargeterror.md)
  Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md).
- [struct LocalTestingDistributedActorSystemError](localtestingdistributedactorsystemerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorcodingerror)*