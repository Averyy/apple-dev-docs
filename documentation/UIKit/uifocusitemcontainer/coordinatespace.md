# coordinateSpace

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
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
var coordinateSpace: any UICoordinateSpace { get }
```

```objc
@property (nonatomic, strong, readonly) id<UICoordinateSpace> coordinateSpace;
```

## Discussion

The focus items returned by [`focusItems(in:)`](./focusitems%28in%29.md) should report their frames in this coordinate space.

## See Also

### Retrieving focus items
- [func focusItems(in: CGRect) -> [any UIFocusItem]](./focusitems%28in%29.md)
  Retrieves all of the focus items within this container that intersect with the provided rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitemcontainer/coordinatespace)*