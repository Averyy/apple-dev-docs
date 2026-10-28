# DistributedActorCodingError

**Framework**: Distributed  
**Kind**: struct  
**Role**: Structure

Error thrown by distributed actor systems while encountering encoding/decoding issues.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct DistributedActorCodingError
```

## Overview

Also thrown when an attempt to decode [`DistributedActor`](./distributedactor.md) is made, but no [`DistributedActorSystem`](./distributedactorsystem.md) is available in the `Decoder`’s `userInfo[.actorSystemKey]`, as it is required to perform the resolve call.

## Topics

### Initializers
- [init(message: String)](./distributedactorcodingerror/init%28message%29.md)
### Instance Properties
- [let message: String](./distributedactorcodingerror/message.md)
### Type Methods
- [static func missingActorSystemUserInfo<Act>(Act.Type) -> DistributedActorCodingError](./distributedactorcodingerror/missingactorsystemuserinfo%28_%29.md)

## Relationships

### Conforms To
- [DistributedActorSystemError](./distributedactorsystemerror.md)
- [Error](../Swift/error.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [protocol DistributedActorSystemError](./distributedactorsystemerror.md)
  Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [struct ExecuteDistributedTargetError](./executedistributedtargeterror.md)
  Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](./distributedactorsystem/executedistributedtarget%28on,target,invocationdecoder,handler%29.md).
- [struct LocalTestingDistributedActorSystemError](./localtestingdistributedactorsystemerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorcodingerror)*