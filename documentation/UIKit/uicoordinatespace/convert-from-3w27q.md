# convert(_:from:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Converts a point from the specified coordinate space to the coordinate space of the current object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func convert(_ point: CGPoint, from coordinateSpace: any UICoordinateSpace) -> CGPoint
```

#### Return Value

A point specified in the coordinate space of the current object.

## Parameters

- `point`: A point in the specified coordinate space.
- `coordinateSpace`: The coordinate space in which   is specified.

## See Also

- [func convert(CGPoint, to: any UICoordinateSpace) -> CGPoint](uicoordinatespace/convert(_:to:)-2ub7a.md)
  Converts a point from the coordinate space of the current object to the specified coordinate space.
- [func convert(CGRect, to: any UICoordinateSpace) -> CGRect](uicoordinatespace/convert(_:to:)-3imkt.md)
  Converts a rectangle from the coordinate space of the current object to the specified coordinate space.
- [func convert(CGRect, from: any UICoordinateSpace) -> CGRect](uicoordinatespace/convert(_:from:)-9921a.md)
  Converts a rectangle from the specified coordinate space to the coordinate space of the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicoordinatespace/convert(_:from:)-3w27q)*