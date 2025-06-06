# init(from:)

**Framework**: Distributed  
**Kind**: init

Initializes an instance of this distributed actor by decoding its [`id`](distributedactor/id.md), and passing it to the [`DistributedActorSystem`](distributedactorsystem.md) obtained from `decoder.userInfo[actorSystemKey]`.

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
nonisolated
init(from decoder: any Decoder) throws
```

#### Requires the Decoder Must Have the Codinguserinfokeyactorsystemkey Set to

the [`ActorSystem`](distributedactor/actorsystem-swift.associatedtype.md) that this actor expects, as it will be used to call [`resolve(id:using:)`](distributedactor/resolve(id:using:).md) on, in order to obtain the instance this initializer should return.

> **Note**: If the actor system value in `decoder.userInfo` is missing or mistyped; the `ID` fails to decode from the passed `decoder`;

## Parameters

- `decoder`: Used to decode the   of this distributed actor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactor/init(from:))*