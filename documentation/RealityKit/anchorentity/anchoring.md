# anchoring

**Framework**: RealityKit  
**Kind**: property

The component that describes how the virtual content is anchored to the real world.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var anchoring: AnchoringComponent { get set }
```

## See Also

- [var anchorIdentifier: UUID?](anchorentity/anchoridentifier.md)
  The identifier of the AR anchor with which the anchor entity is associated, or `nil` if it isn’t currently anchored.
- [func reanchor(AnchoringComponent.Target, preservingWorldTransform: Bool)](anchorentity/reanchor(_:preservingworldtransform:).md)
  Changes the entity’s anchoring, preserving either the world transform or the local transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity/anchoring)*