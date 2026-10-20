# contains(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Checks whether the bounding box contains the specified bounds.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func contains(_ boundingBox: BoundingBox) -> Bool
```

**Other overloads**:

```swift
func contains(_ point: SIMD3<Float>) -> Bool
```

#### Return Value

A Boolean that’s `true` if the box contains the specified bounds.

## See Also

### Checking for overlap
- [func contains(SIMD3<Float>) -> Bool](./contains%28_%29-92ap6.md)
  Checks whether the bounding box contains the specified point.
- [func intersects(BoundingBox) -> Bool](./intersects%28_%29.md)
  Checks whether the bounding box intersects the specified bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/contains(_:)-5ux4h)*