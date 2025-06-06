# LocalTestingInvocationDecoder.SerializationRequirement

**Framework**: Distributed  
**Kind**: typealias

The serialization requirement that the types passed to `decodeNextArgument` are required to conform to. The type returned by `decodeReturnType` is also expected to conform to this associated type requirement.

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
typealias SerializationRequirement = Codable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationdecoder/serializationrequirement)*