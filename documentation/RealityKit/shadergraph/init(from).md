# init(from:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a graph from data previously produced by [`encode()`](./encode%28%29.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
convenience init(from data: Data) throws
```

#### Discussion

> **Throws**: If the data is malformed or was produced by an incompatible version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/init(from:))*