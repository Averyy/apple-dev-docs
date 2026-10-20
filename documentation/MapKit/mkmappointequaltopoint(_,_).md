# MKMapPointEqualToPoint(_:_:)

**Framework**: MapKit  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether two map points are equal.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func MKMapPointEqualToPoint(_ point1: MKMapPoint, _ point2: MKMapPoint) -> Bool
```

```c
static BOOL MKMapPointEqualToPoint(MKMapPoint point1, MKMapPoint point2);
```

#### Return Value

[`true`](../Swift/true.md) if the `x` and `y` values in both points are exactly the same, or [`false`](../Swift/false.md) if one or both values are different.

## Parameters

- `point1`: The first map point.
- `point2`: The second point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmappointequaltopoint(_:_:))*