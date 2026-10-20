# LocalTestingDistributedActorSystemError

**Framework**: Distributed  
**Kind**: struct  
**Role**: Structure

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
struct LocalTestingDistributedActorSystemError
```

## Topics

### Initializers
- [init(message: String)](./localtestingdistributedactorsystemerror/init%28message%29.md)
### Instance Properties
- [let message: String](./localtestingdistributedactorsystemerror/message.md)

## Relationships

### Conforms To
- [DistributedActorSystemError](./distributedactorsystemerror.md)
- [Error](../Swift/error.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct DistributedActorCodingError](./distributedactorcodingerror.md)
  Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [protocol DistributedActorSystemError](./distributedactorsystemerror.md)
  Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [struct ExecuteDistributedTargetError](./executedistributedtargeterror.md)
  Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](./distributedactorsystem/executedistributedtarget%28on,target,invocationdecoder,handler%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystemerror)*