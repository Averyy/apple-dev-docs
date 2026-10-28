# previouslyFocusedView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view that was focused before the focus update.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
weak var previouslyFocusedView: UIView? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) UIView * previouslyFocusedView;
```

## Discussion

If your app targets tvOS 10 and later, use [`previouslyFocusedItem`](./previouslyfocuseditem.md) instead.

This property returns `nil` when no view was previously focused, such as when setting the initial focus.

## See Also

### Locating focus direction
- [var nextFocusedView: UIView?](./nextfocusedview.md)
  The view that takes the focus after the focus update.
- [var focusHeading: UIFocusHeading](./focusheading.md)
  The heading in which the focus update is occurring.
- [struct UIFocusHeading](../uifocusheading.md)
  The general type of an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/previouslyfocusedview)*