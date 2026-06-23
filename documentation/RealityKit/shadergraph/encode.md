# encode()

**Framework**: RealityKit  
**Kind**: method

Encodes the graph into a binary representation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func encode() throws -> Data
```

#### Discussion

The resulting data can be stored to disk or passed across a process boundary, and later restored with [`init(from:)`](shadergraph/init(from:).md).

> **Note**: If the graph cannot be serialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/encode())*