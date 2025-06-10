# remove(at:)

**Framework**: RealityKit  
**Kind**: method

Removes and returns the anchor at the specified position.

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
@preconcurrency func remove(at index: Int)
```

## Parameters

- `index`: The position of the anchor to remove.   Use a valid index of the collection.

## See Also

- [func remove(any HasAnchoring)](scene/anchorcollection/remove(_:).md)
  Removes the anchor at the specified position.
- [func removeAll()](scene/anchorcollection/removeall.md)
  Removes all anchors from the collection.
- [func removeAll(keepCapacity: Bool)](scene/anchorcollection/removeall(keepcapacity:).md)
  Removes all anchors from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/remove(at:))*