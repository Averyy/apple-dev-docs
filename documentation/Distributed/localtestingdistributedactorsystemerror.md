# LocalTestingDistributedActorSystemError

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
struct LocalTestingDistributedActorSystemError
```

## Topics

### Initializers
- [init(message: String)](localtestingdistributedactorsystemerror/init(message:).md)
### Instance Properties
- [let message: String](localtestingdistributedactorsystemerror/message.md)

## Relationships

### Conforms To
- [DistributedActorSystemError](distributedactorsystemerror.md)
- [Error](../swift/error.md)
- [Sendable](../swift/sendable.md)

## See Also

- [struct DistributedActorCodingError](distributedactorcodingerror.md)
  Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [protocol DistributedActorSystemError](distributedactorsystemerror.md)
  Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [struct ExecuteDistributedTargetError](executedistributedtargeterror.md)
  Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystemerror)*