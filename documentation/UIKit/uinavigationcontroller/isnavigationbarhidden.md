# isNavigationBarHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the navigation bar is hidden.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isNavigationBarHidden: Bool { get set }
```

```objc
@property (nonatomic, getter=isNavigationBarHidden) BOOL navigationBarHidden;
```

#### Discussion

If [`true`](../../Swift/true.md), the navigation bar is hidden. The default value is [`false`](../../Swift/false.md). Setting this property changes the visibility of the navigation bar without animating the changes. If you want to animate the change, use the [`setNavigationBarHidden(_:animated:)`](./setnavigationbarhidden%28_,animated%29.md)method instead.

## See Also

### Hiding the navigation bar
- [var hidesBarsOnTap: Bool](./hidesbarsontap.md)
  A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [var hidesBarsOnSwipe: Bool](./hidesbarsonswipe.md)
  A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [var hidesBarsWhenVerticallyCompact: Bool](./hidesbarswhenverticallycompact.md)
  A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [var hidesBarsWhenKeyboardAppears: Bool](./hidesbarswhenkeyboardappears.md)
  A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [var barHideOnTapGestureRecognizer: UITapGestureRecognizer](./barhideontapgesturerecognizer.md)
  The gesture recognizer used to hide and show the navigation and toolbar.
- [var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer](./barhideonswipegesturerecognizer.md)
  The gesture recognizer used to hide the navigation bar and toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/isnavigationbarhidden)*