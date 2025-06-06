# ActorSystem

**Framework**: Distributed  
**Kind**: associatedtype  
**Required**: Yes

The type of transport used to communicate with actors of this type.

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
associatedtype ActorSystem : DistributedActorSystem where Self.ID == Self.ActorSystem.ActorID
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactor/actorsystem-swift.associatedtype)*