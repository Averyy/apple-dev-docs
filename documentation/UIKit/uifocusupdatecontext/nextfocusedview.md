# nextFocusedView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view that takes the focus after the focus update.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
weak var nextFocusedView: UIView? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) UIView * nextFocusedView;
```

#### Discussion

If your app targets tvOS 10 and later, use [`nextFocusedItem`](./nextfocuseditem.md) instead.

This property returns `nil` if no view will be focused after the update.

## See Also

### Locating focus direction
- [var previouslyFocusedView: UIView?](./previouslyfocusedview.md)
  The view that was focused before the focus update.
- [var focusHeading: UIFocusHeading](./focusheading.md)
  The heading in which the focus update is occurring.
- [struct UIFocusHeading](../uifocusheading.md)
  The general type of an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/nextfocusedview)*