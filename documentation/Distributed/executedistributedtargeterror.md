# ExecuteDistributedTargetError

**Framework**: Distributed  
**Kind**: struct

Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md).

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
struct ExecuteDistributedTargetError
```

#### Overview

Inspect the [`errorCode`](executedistributedtargeterror/errorcode-swift.property.md) for details about the underlying reason this error was thrown.

## Topics

### Initializers
- [init(message: String)](executedistributedtargeterror/init(message:).md)
- [init(message: String, errorCode: ExecuteDistributedTargetError.ErrorCode)](executedistributedtargeterror/init(message:errorcode:).md)
### Instance Properties
- [let errorCode: ExecuteDistributedTargetError.ErrorCode](executedistributedtargeterror/errorcode-swift.property.md)
- [let message: String](executedistributedtargeterror/message.md)
### Enumerations
- [ExecuteDistributedTargetError.ErrorCode](executedistributedtargeterror/errorcode-swift.enum.md)

## Relationships

### Conforms To
- [DistributedActorSystemError](distributedactorsystemerror.md)
- [Error](../swift/error.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct DistributedActorCodingError](distributedactorcodingerror.md)
  Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [protocol DistributedActorSystemError](distributedactorsystemerror.md)
  Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [struct LocalTestingDistributedActorSystemError](localtestingdistributedactorsystemerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/executedistributedtargeterror)*