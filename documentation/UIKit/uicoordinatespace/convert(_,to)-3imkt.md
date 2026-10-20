# convert(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Converts a rectangle from the coordinate space of the current object to the specified coordinate space.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func convert(_ rect: CGRect, to coordinateSpace: any UICoordinateSpace) -> CGRect
```

```objc
- (CGRect) convertRect:(CGRect) rect toCoordinateSpace:(id<UICoordinateSpace>) coordinateSpace;
```

#### Return Value

A rectangle specified in the target coordinate space.

## Parameters

- `rect`: A rectangle specified in the coordinate system of the current object.
- `coordinateSpace`: The coordinate space into which `rect` is to be converted.

## See Also

### Converting between coordinate spaces
- [func convert(CGPoint, to: any UICoordinateSpace) -> CGPoint](./convert%28_,to%29-2ub7a.md)
  Converts a point from the coordinate space of the current object to the specified coordinate space.
- [func convert(CGPoint, from: any UICoordinateSpace) -> CGPoint](./convert%28_,from%29-3w27q.md)
  Converts a point from the specified coordinate space to the coordinate space of the current object.
- [func convert(CGRect, from: any UICoordinateSpace) -> CGRect](./convert%28_,from%29-9921a.md)
  Converts a rectangle from the specified coordinate space to the coordinate space of the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicoordinatespace/convert(_:to:)-3imkt)*