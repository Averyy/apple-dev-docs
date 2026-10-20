# removeAll(keepCapacity:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Removes all anchors from the collection.

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
@preconcurrency func removeAll(keepCapacity: Bool = false)
```

## Parameters

- `keepCapacity`: Pass true to keep the existing capacity of the array after removing its elements. The default value is false.

## See Also

### Removing anchors
- [func remove(any HasAnchoring)](./remove%28_%29.md)
  Removes the anchor at the specified position.
- [func remove(at: Int)](./remove%28at%29.md)
  Removes and returns the anchor at the specified position.
- [func removeAll()](./removeall%28%29.md)
  Removes all anchors from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/removeall(keepcapacity:))*