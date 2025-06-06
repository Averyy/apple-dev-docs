# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

The buffer for a given semantic. There can only be one buffer for any given ID.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
subscript<S>(semantic: S) -> MeshBuffer<S.Element>? where S : MeshBufferSemantic { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdescriptor/subscript(_:))*