# anchorIdentifier

**Framework**: RealityKit  
**Kind**: property

The identifier of the AR anchor with which the anchor entity is associated, or `nil` if it isn’t currently anchored.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+ - Deprecated

## Declaration

```swift
@MainActor
@preconcurrency var anchorIdentifier: UUID? { get }
```

## See Also

- [var anchoring: AnchoringComponent](anchorentity/anchoring.md)
  The component that describes how the virtual content is anchored to the real world.
- [func reanchor(AnchoringComponent.Target, preservingWorldTransform: Bool)](anchorentity/reanchor(_:preservingworldtransform:).md)
  Changes the entity’s anchoring, preserving either the world transform or the local transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity/anchoridentifier)*