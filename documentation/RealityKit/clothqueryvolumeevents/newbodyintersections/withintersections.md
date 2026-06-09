# withIntersections(_:)

**Framework**: RealityKit  
**Kind**: method

Provides access to the intersections with cloth bodies that took place.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withIntersections<Result>(_ callback: (Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>) -> Result) -> Result
```

#### Return Value

The value returned by `callback`.

#### Discussion

This span is only available during the subscription callback of this event. The provided span is only valid for the lifetime of the callback.

## Parameters

- `callback`: A closure that receives a span over the intersections.

## See Also

- [var intersections: Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>](clothqueryvolumeevents/newbodyintersections/intersections.md)
  The intersections with cloth bodies that took place.
- [ClothQueryVolumeEvents.NewBodyIntersections.Intersection](clothqueryvolumeevents/newbodyintersections/intersection.md)
  An intersection with a cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/withintersections(_:))*