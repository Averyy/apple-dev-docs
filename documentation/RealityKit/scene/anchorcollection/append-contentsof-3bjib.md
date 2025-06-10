# append(contentsOf:)

**Framework**: RealityKit  
**Kind**: method

Adds anchors from an array to the end of this collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func append(contentsOf array: [any HasAnchoring])
```

## Parameters

- `array`: The array of anchor entities to add.

## See Also

- [func append(any HasAnchoring)](scene/anchorcollection/append(_:).md)
  Adds a new anchor at the end of the collection.
- [func append<S>(contentsOf: S)](scene/anchorcollection/append(contentsof:)-4sf55.md)
  Adds anchors from a sequence to the end of this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/append(contentsof:)-3bjib)*