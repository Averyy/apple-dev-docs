# DistributedActorSystemError

**Framework**: Distributed  
**Kind**: protocol  
**Role**: Protocol

Error protocol to which errors thrown by any `DistributedActorSystem` should conform.

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
protocol DistributedActorSystemError : Error
```

## Relationships

### Inherits From
- [Error](../Swift/error.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [DistributedActorCodingError](./distributedactorcodingerror.md)
- [ExecuteDistributedTargetError](./executedistributedtargeterror.md)
- [LocalTestingDistributedActorSystemError](./localtestingdistributedactorsystemerror.md)

## See Also

### Errors
- [struct DistributedActorCodingError](./distributedactorcodingerror.md)
  Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [struct ExecuteDistributedTargetError](./executedistributedtargeterror.md)
  Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](./distributedactorsystem/executedistributedtarget%28on,target,invocationdecoder,handler%29.md).
- [struct LocalTestingDistributedActorSystemError](./localtestingdistributedactorsystemerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorsystemerror)*