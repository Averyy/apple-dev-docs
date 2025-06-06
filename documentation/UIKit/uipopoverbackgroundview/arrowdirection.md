# arrowDirection

**Framework**: UIKit  
**Kind**: property

The direction in which the popover arrow is pointing.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var arrowDirection: UIPopoverArrowDirection { get set }
```

#### Discussion

The default implementation of this method raises an exception. You must override it and implement the appropriate setter and getter methods yourself. Your methods must not call `super`.

You should use this value during layout to configure the images to use for your view’s content. In your setter method, you should update to your view’s content and potentially update the layout as well.

Use this value to determine which stretchable images to use for your view. Normally, you would have different sets of images depending on whether the arrow was pointing up, down, left, or right. (You could also use the same image for up and down, or left and right, and use a transform to flip the images so that they point in the appropriate direction.)  The popover controller sets this value prior to displaying the popover initially, and it may change the value after your popover is displayed on screen.

## See Also

- [var arrowOffset: CGFloat](uipopoverbackgroundview/arrowoffset.md)
  The distance (measured in points) from the center of the view to the center line of the arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/arrowdirection)*