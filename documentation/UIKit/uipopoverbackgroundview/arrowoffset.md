# arrowOffset

**Framework**: UIKit  
**Kind**: property

The distance (measured in points) from the center of the view to the center line of the arrow.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var arrowOffset: CGFloat { get set }
```

#### Discussion

The default implementation of this method raises an exception. You must override it and implement the appropriate setter and getter methods yourself. Your methods must not call `super`.

Use this value during layout to get the position of the arrow. In your setter method, you should similarly initiate an update to your view’s layout so that you can reposition your stretchable images accordingly.

Offsets are always specified relative to the center of your view object. Adding the offset value to the center value of the given axis yields the required location for the arrow. Thus, for an arrow pointing up or down, a negative offset moves the arrow toward the left edge of the view. For an arrow pointing left or right, a negative offset moves the arrow toward the top of the view.

## See Also

- [var arrowDirection: UIPopoverArrowDirection](uipopoverbackgroundview/arrowdirection.md)
  The direction in which the popover arrow is pointing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/arrowoffset)*