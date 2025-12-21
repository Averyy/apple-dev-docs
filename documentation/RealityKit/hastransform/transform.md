# transform

**Framework**: RealityKit  
**Kind**: property

The transform of an entity relative to its parent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var transform: Transform { get set }
```

#### Discussion

For an [`AnchorEntity`](anchorentity.md) instance, the transform is relative to the AR anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/transform)*