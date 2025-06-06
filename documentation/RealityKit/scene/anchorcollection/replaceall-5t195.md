# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces the existing anchor collection with a provided sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func replaceAll<S>(_ entities: S) where S : Sequence, S.Element : HasAnchoring
```

## Parameters

- `entities`: A sequence of anchors to replace the existing   collection.

## See Also

- [func replaceAll([any HasAnchoring])](scene/anchorcollection/replaceall(_:)-tris.md)
  Replaces the existing anchor collection with a provided collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/replaceall(_:)-5t195)*