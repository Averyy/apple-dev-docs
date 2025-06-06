# coordinateSpace

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The coordinate space of the focus items contained in the focus item container.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var coordinateSpace: any UICoordinateSpace { get }
```

#### Discussion

The focus items returned by [`focusItems(in:)`](uifocusitemcontainer/focusitems(in:).md) should report their frames in this coordinate space.

## See Also

- [func focusItems(in: CGRect) -> [any UIFocusItem]](uifocusitemcontainer/focusitems(in:).md)
  Retrieves all of the focus items within this container that intersect with the provided rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitemcontainer/coordinatespace)*