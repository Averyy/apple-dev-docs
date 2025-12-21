# remove(_:)

**Framework**: RealityKit  
**Kind**: method

Removes the anchor at the specified position.

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
@preconcurrency func remove(_ entity: any HasAnchoring)
```

## Parameters

- `entity`: The anchor to remove from the collection.

## See Also

- [func remove(at: Int)](scene/anchorcollection/remove(at:).md)
  Removes and returns the anchor at the specified position.
- [func removeAll()](scene/anchorcollection/removeall.md)
  Removes all anchors from the collection.
- [func removeAll(keepCapacity: Bool)](scene/anchorcollection/removeall(keepcapacity:).md)
  Removes all anchors from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/remove(_:))*