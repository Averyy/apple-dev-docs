# convert(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Converts a point from the coordinate space of the current object to the specified coordinate space.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func convert(_ point: CGPoint, to coordinateSpace: any UICoordinateSpace) -> CGPoint
```

```objc
- (CGPoint) convertPoint:(CGPoint) point toCoordinateSpace:(id<UICoordinateSpace>) coordinateSpace;
```

## Return Value

A point specified in the target coordinate space.

## Parameters

- `point`: A point specified in the coordinate system of the current object.
- `coordinateSpace`: The coordinate space into which `point` is to be converted.

## See Also

### Converting between coordinate spaces
- [func convert(CGPoint, from: any UICoordinateSpace) -> CGPoint](./convert%28_,from%29-3w27q.md)
  Converts a point from the specified coordinate space to the coordinate space of the current object.
- [func convert(CGRect, to: any UICoordinateSpace) -> CGRect](./convert%28_,to%29-3imkt.md)
  Converts a rectangle from the coordinate space of the current object to the specified coordinate space.
- [func convert(CGRect, from: any UICoordinateSpace) -> CGRect](./convert%28_,from%29-9921a.md)
  Converts a rectangle from the specified coordinate space to the coordinate space of the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicoordinatespace/convert(_:to:)-2ub7a)*