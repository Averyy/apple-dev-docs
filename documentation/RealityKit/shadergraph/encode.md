# encode()

**Framework**: RealityKit  
**Kind**: method

Encodes the graph into a binary representation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func encode() throws -> Data
```

#### Discussion

The resulting data can be stored to disk or passed across a process boundary, and later restored with [`init(from:)`](shadergraph/init(from:).md).

> **Note**: If the graph cannot be serialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/encode())*