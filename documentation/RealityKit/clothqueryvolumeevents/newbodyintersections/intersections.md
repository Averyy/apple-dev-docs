# intersections

**Framework**: RealityKit  
**Kind**: property

The intersections with cloth bodies that took place.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var intersections: Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection> { get }
```

#### Discussion

The lifetime of this span is tied to the owning event, and thus cannot escape it. This data is only available during the subscription callback in which the owning event is provided. If you store the event and attempt to access this data after the subscription callback, then you will get an empty span instead.

## See Also

- [func withIntersections<Result>((Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>) -> Result) -> Result](clothqueryvolumeevents/newbodyintersections/withintersections(_:).md)
  Provides access to the intersections with cloth bodies that took place.
- [ClothQueryVolumeEvents.NewBodyIntersections.Intersection](clothqueryvolumeevents/newbodyintersections/intersection.md)
  An intersection with a cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/intersections)*