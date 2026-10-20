# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Replaces the existing anchor collection with a provided sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func replaceAll<S>(_ entities: S) where S : Sequence, S.Element : HasAnchoring
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func replaceAll(_ entities: [any HasAnchoring])
```

## Parameters

- `entities`: A sequence of anchors to replace the existing collection.

## See Also

### Replacing anchors
- [func replaceAll([any HasAnchoring])](./replaceall%28_%29-tris.md)
  Replaces the existing anchor collection with a provided collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/replaceall(_:)-5t195)*