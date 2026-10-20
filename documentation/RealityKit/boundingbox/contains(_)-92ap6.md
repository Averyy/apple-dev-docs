# contains(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Checks whether the bounding box contains the specified point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func contains(_ point: SIMD3<Float>) -> Bool
```

**Other overloads**:

```swift
func contains(_ boundingBox: BoundingBox) -> Bool
```

#### Return Value

A Boolean that’s `true` if the box contains the specified point.

## See Also

### Checking for overlap
- [func contains(BoundingBox) -> Bool](./contains%28_%29-5ux4h.md)
  Checks whether the bounding box contains the specified bounds.
- [func intersects(BoundingBox) -> Bool](./intersects%28_%29.md)
  Checks whether the bounding box intersects the specified bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/contains(_:)-92ap6)*