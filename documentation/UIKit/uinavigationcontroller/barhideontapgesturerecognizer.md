# barHideOnTapGestureRecognizer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The gesture recognizer used to hide and show the navigation and toolbar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
unowned(unsafe) var barHideOnTapGestureRecognizer: UITapGestureRecognizer { get }
```

```objc
@property (nonatomic, assign, readonly) UITapGestureRecognizer * barHideOnTapGestureRecognizer;
```

#### Discussion

This property contains the gesture recognizer used to hide or show the bars. The gesture recognizer is inactive unless the [`hidesBarsOnTap`](./hidesbarsontap.md) property is [`true`](../../Swift/true.md). You can make changes to the gesture recognizer as needed but must not change its delegate and you must not remove the default target object and action that come configured with it. Do not try to replace this gesture recognizer by overriding the property.

If you tie this gesture recognizer to one of your own, make sure both recognize their gestures simultaneously to ensure that each has a chance to handle the event.

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
- [var isNavigationBarHidden: Bool](./isnavigationbarhidden.md)
  A Boolean value that indicates whether the navigation bar is hidden.
- [var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer](./barhideonswipegesturerecognizer.md)
  The gesture recognizer used to hide the navigation bar and toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/barhideontapgesturerecognizer)*