# LocalTestingDistributedActorSystem.ActorID

**Framework**: Distributed  
**Kind**: typealias

The type ID that will be assigned to any distributed actor managed by this actor system.

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
typealias ActorID = LocalTestingActorID
```

##### A Note on Codable Ids

If this type is `Codable`, then any `distributed actor` using this `ActorID` as its `DistributedActor/ID` will gain a synthesized `Codable` conformance which is implemented by encoding the `ID`. The decoding counter part of the `Codable` conformance is implemented by decoding the `ID` and passing it to the [`resolve(id:using:)`](distributedactor/resolve(id:using:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem/actorid)*