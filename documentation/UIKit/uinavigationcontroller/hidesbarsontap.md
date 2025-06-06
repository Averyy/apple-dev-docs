# hidesBarsOnTap

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hidesBarsOnTap: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the navigation controller toggles the hiding and showing of its navigation bar and toolbar in response to an otherwise unhandled tap in the content area. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var hidesBarsOnSwipe: Bool](uinavigationcontroller/hidesbarsonswipe.md)
  A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [var hidesBarsWhenVerticallyCompact: Bool](uinavigationcontroller/hidesbarswhenverticallycompact.md)
  A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [var hidesBarsWhenKeyboardAppears: Bool](uinavigationcontroller/hidesbarswhenkeyboardappears.md)
  A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [var isNavigationBarHidden: Bool](uinavigationcontroller/isnavigationbarhidden.md)
  A Boolean value that indicates whether the navigation bar is hidden.
- [var barHideOnTapGestureRecognizer: UITapGestureRecognizer](uinavigationcontroller/barhideontapgesturerecognizer.md)
  The gesture recognizer used to hide and show the navigation and toolbar.
- [var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer](uinavigationcontroller/barhideonswipegesturerecognizer.md)
  The gesture recognizer used to hide the navigation bar and toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/hidesbarsontap)*