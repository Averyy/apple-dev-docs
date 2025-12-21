# isNavigationBarHidden

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the navigation bar is hidden.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isNavigationBarHidden: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the navigation bar is hidden. The default value is [`false`](https://developer.apple.com/documentation/Swift/false). Setting this property changes the visibility of the navigation bar without animating the changes. If you want to animate the change, use the [`setNavigationBarHidden(_:animated:)`](uinavigationcontroller/setnavigationbarhidden(_:animated:).md)method instead.

## See Also

- [var hidesBarsOnTap: Bool](uinavigationcontroller/hidesbarsontap.md)
  A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [var hidesBarsOnSwipe: Bool](uinavigationcontroller/hidesbarsonswipe.md)
  A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [var hidesBarsWhenVerticallyCompact: Bool](uinavigationcontroller/hidesbarswhenverticallycompact.md)
  A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [var hidesBarsWhenKeyboardAppears: Bool](uinavigationcontroller/hidesbarswhenkeyboardappears.md)
  A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [var barHideOnTapGestureRecognizer: UITapGestureRecognizer](uinavigationcontroller/barhideontapgesturerecognizer.md)
  The gesture recognizer used to hide and show the navigation and toolbar.
- [var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer](uinavigationcontroller/barhideonswipegesturerecognizer.md)
  The gesture recognizer used to hide the navigation bar and toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/isnavigationbarhidden)*