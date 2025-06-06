# removeAll(keepCapacity:)

**Framework**: RealityKit  
**Kind**: method

Removes all anchors from the collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func removeAll(keepCapacity: Bool = false)
```

## Parameters

- `keepCapacity`: Pass true to keep the existing capacity of the array   after removing its elements. The default value is false.

## See Also

- [func remove(any HasAnchoring)](scene/anchorcollection/remove(_:).md)
  Removes the anchor at the specified position.
- [func remove(at: Int)](scene/anchorcollection/remove(at:).md)
  Removes and returns the anchor at the specified position.
- [func removeAll()](scene/anchorcollection/removeall.md)
  Removes all anchors from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/removeall(keepcapacity:))*