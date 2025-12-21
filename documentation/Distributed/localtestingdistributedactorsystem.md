# LocalTestingDistributedActorSystem

**Framework**: Distributed  
**Kind**: class

A `DistributedActorSystem` designed for local only testing.

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
final class LocalTestingDistributedActorSystem
```

#### Overview

It will crash on any attempt of remote communication, but can be useful for learning about `distributed actor` isolation, as well as early prototyping stages of development where a real system is not necessary yet.

## Topics

### Initializers
- [init()](localtestingdistributedactorsystem/init.md)

## Relationships

### Conforms To
- [DistributedActorSystem](distributedactorsystem.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct LocalTestingActorID](localtestingactorid.md)
- [typealias LocalTestingActorAddress](localtestingactoraddress.md)
- [struct LocalTestingInvocationEncoder](localtestinginvocationencoder.md)
- [class LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)
- [struct LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem)*