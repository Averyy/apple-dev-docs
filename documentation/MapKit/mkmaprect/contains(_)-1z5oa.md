# contains(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether one rectangle contains another.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func contains(_ rect2: MKMapRect) -> Bool
```

```c
extern BOOL MKMapRectContainsRect(MKMapRect rect1, MKMapRect rect2);
```

## Return Value

[`true`](../../Swift/true.md) if `rect2` is `null` or lies entirely inside `rect1`; otherwise, returns [`false`](../../Swift/false.md) if `rect1` is `null` or doesn’t completely enclose `rect2`.

## Parameters

- `rect2`: The rectangle that `rect1` might contain.

## See Also

### Intersecting the rectangle
- [func contains(MKMapPoint) -> Bool](./contains%28_%29-79tjt.md)
  Returns a Boolean value that indicates whether the specified map point lies within the rectangle.
- [func intersects(MKMapRect) -> Bool](./intersects%28_%29.md)
  Returns a Boolean value that indicates whether two rectangles intersect each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/contains(_:)-1z5oa)*