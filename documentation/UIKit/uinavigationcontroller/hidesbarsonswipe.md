# hidesBarsOnSwipe

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hidesBarsOnSwipe: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL hidesBarsOnSwipe;
```

#### Discussion

When this property is set to [`true`](../../Swift/true.md), an upward swipe hides the navigation bar and toolbar. A downward swipe shows both bars again. If the toolbar does not have any items, it remains visible even after a swipe. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Hiding the navigation bar
- [var hidesBarsOnTap: Bool](./hidesbarsontap.md)
  A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [var hidesBarsWhenVerticallyCompact: Bool](./hidesbarswhenverticallycompact.md)
  A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [var hidesBarsWhenKeyboardAppears: Bool](./hidesbarswhenkeyboardappears.md)
  A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [var isNavigationBarHidden: Bool](./isnavigationbarhidden.md)
  A Boolean value that indicates whether the navigation bar is hidden.
- [var barHideOnTapGestureRecognizer: UITapGestureRecognizer](./barhideontapgesturerecognizer.md)
  The gesture recognizer used to hide and show the navigation and toolbar.
- [var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer](./barhideonswipegesturerecognizer.md)
  The gesture recognizer used to hide the navigation bar and toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/hidesbarsonswipe)*