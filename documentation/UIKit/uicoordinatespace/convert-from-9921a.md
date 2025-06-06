# convert(_:from:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Converts a rectangle from the specified coordinate space to the coordinate space of the current object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func convert(_ rect: CGRect, from coordinateSpace: any UICoordinateSpace) -> CGRect
```

#### Return Value

A rectangle specified in the coordinate space of the current object.

## Parameters

- `rect`: A rectangle in the specified coordinate space.
- `coordinateSpace`: The coordinate space in which   is specified.

## See Also

- [func convert(CGPoint, to: any UICoordinateSpace) -> CGPoint](uicoordinatespace/convert(_:to:)-2ub7a.md)
  Converts a point from the coordinate space of the current object to the specified coordinate space.
- [func convert(CGPoint, from: any UICoordinateSpace) -> CGPoint](uicoordinatespace/convert(_:from:)-3w27q.md)
  Converts a point from the specified coordinate space to the coordinate space of the current object.
- [func convert(CGRect, to: any UICoordinateSpace) -> CGRect](uicoordinatespace/convert(_:to:)-3imkt.md)
  Converts a rectangle from the coordinate space of the current object to the specified coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicoordinatespace/convert(_:from:)-9921a)*