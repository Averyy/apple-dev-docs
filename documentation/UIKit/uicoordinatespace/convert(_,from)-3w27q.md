# convert(_:from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Converts a point from the specified coordinate space to the coordinate space of the current object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func convert(_ point: CGPoint, from coordinateSpace: any UICoordinateSpace) -> CGPoint
```

```objc
- (CGPoint) convertPoint:(CGPoint) point fromCoordinateSpace:(id<UICoordinateSpace>) coordinateSpace;
```

#### Return Value

A point specified in the coordinate space of the current object.

## Parameters

- `point`: A point in the specified coordinate space.
- `coordinateSpace`: The coordinate space in which `point` is specified.

## See Also

### Converting between coordinate spaces
- [func convert(CGPoint, to: any UICoordinateSpace) -> CGPoint](./convert%28_,to%29-2ub7a.md)
  Converts a point from the coordinate space of the current object to the specified coordinate space.
- [func convert(CGRect, to: any UICoordinateSpace) -> CGRect](./convert%28_,to%29-3imkt.md)
  Converts a rectangle from the coordinate space of the current object to the specified coordinate space.
- [func convert(CGRect, from: any UICoordinateSpace) -> CGRect](./convert%28_,from%29-9921a.md)
  Converts a rectangle from the specified coordinate space to the coordinate space of the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicoordinatespace/convert(_:from:)-3w27q)*