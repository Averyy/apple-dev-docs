# SerializationRequirement

**Framework**: Distributed  
**Kind**: associatedtype  
**Required**: Yes

The serialization requirement that will be applied to all distributed targets used with this system.

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
associatedtype SerializationRequirement where Self.SerializationRequirement == Self.InvocationDecoder.SerializationRequirement
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorsystem/serializationrequirement)*