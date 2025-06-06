# focusItems(in:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Retrieves all of the focus items within this container that intersect with the provided rectangle.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func focusItems(in rect: CGRect) -> [any UIFocusItem]
```

#### Return Value

An array of focus items that intersect the provided rectangle. The focus items are expressed in the container’s coordinate space.

#### Discussion

The found focus items should report their frames in the [`coordinateSpace`](uifocusitemcontainer/coordinatespace.md).

## Parameters

- `rect`: The rectangle used to look for focus items that intersect the rectangle expressed in the container’s coordinate space.

## See Also

- [var coordinateSpace: any UICoordinateSpace](uifocusitemcontainer/coordinatespace.md)
  The coordinate space of the focus items contained in the focus item container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitemcontainer/focusitems(in:))*