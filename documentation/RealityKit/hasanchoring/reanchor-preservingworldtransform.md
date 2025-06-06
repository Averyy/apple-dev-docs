# reanchor(_:preservingWorldTransform:)

**Framework**: RealityKit  
**Kind**: method

Changes the entity’s anchoring, preserving either the world transform or the local transform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS ?+ - Deprecated

## Declaration

```swift
@MainActor
@preconcurrency func reanchor(_ target: AnchoringComponent.Target, preservingWorldTransform: Bool = true)
```

## Parameters

- `target`: Describes how the entity should be anchored in AR.
- `preservingWorldTransform`: A Boolean you set to   to preserve the   current world space position, or   to use the position relative to   the previous anchor for the new anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasanchoring/reanchor(_:preservingworldtransform:))*