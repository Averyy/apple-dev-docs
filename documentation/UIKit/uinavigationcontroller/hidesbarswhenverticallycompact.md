# hidesBarsWhenVerticallyCompact

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hidesBarsWhenVerticallyCompact: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL hidesBarsWhenVerticallyCompact;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the navigation controller hides its navigation bar and toolbar when it transitions to a vertically compact environment. Upon returning to a vertically regular environment, the navigation controller automatically shows both bars again. In addition, unhandled taps in the content area cause the navigation controller to show both bars again. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Hiding the navigation bar
- [var hidesBarsOnTap: Bool](./hidesbarsontap.md)
  A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [var hidesBarsOnSwipe: Bool](./hidesbarsonswipe.md)
  A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [var hidesBarsWhenKeyboardAppears: Bool](./hidesbarswhenkeyboardappears.md)
  A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [var isNavigationBarHidden: Bool](./isnavigationbarhidden.md)
  A Boolean value that indicates whether the navigation bar is hidden.
- [var barHideOnTapGestureRecognizer: UITapGestureRecognizer](./barhideontapgesturerecognizer.md)
  The gesture recognizer used to hide and show the navigation and toolbar.
- [var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer](./barhideonswipegesturerecognizer.md)
  The gesture recognizer used to hide the navigation bar and toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/hidesbarswhenverticallycompact)*