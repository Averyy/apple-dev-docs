# hitTest(point:in:query:mask:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Searches the scene for entities at the specified point in the view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
func hitTest(point: CGPoint, in space: some CoordinateSpaceProtocol, query: CollisionCastQueryType, mask: CollisionGroup) -> [CollisionCastHit]
```

#### Return Value

An array of hit-test results.

#### Discussion

> ❗ **Important**: RealityKit performs hit tests (ray-casts) against collision shapes. Entities without a proper [`CollisionComponent`](collisioncomponent.md) are ignored by hit tests.

## Parameters

- `point`: A point in the provided coordinate space.
- `space`: The 2D coordinate space in which to interpret the  .
- `query`: The query type.
- `mask`: The collision mask that you can use to prevent hits with certain objects.   The default value is  , which means the ray can hit all objects.   See   for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespaceprojecting/hittest(point:in:query:mask:))*