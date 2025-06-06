# SerializationRequirement

**Framework**: Distributed  
**Kind**: associatedtype  
**Required**: Yes

The serialization requirement to apply to all distributed declarations inside the actor.

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
associatedtype SerializationRequirement where Self.SerializationRequirement == Self.ActorSystem.SerializationRequirement
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactor/serializationrequirement)*