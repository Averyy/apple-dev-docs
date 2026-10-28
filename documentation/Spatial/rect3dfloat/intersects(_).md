# intersects(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func intersects(_ other: Rect3DFloat) -> Bool
```

```c
static bool SPRect3DFloatIntersectsRect(SPRect3DFloat rect, SPRect3DFloat other);
```

## Return Value

A Boolean value that indicates whether two rectangles intersect.

## Discussion

Returns a Boolean value that indicates whether two rectangles intersect.

## Parameters

- `other`: The second rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/intersects(_:))*