# previouslyFocusedView

**Framework**: UIKit  
**Kind**: property

The view that was focused before the focus update.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var previouslyFocusedView: UIView? { get }
```

#### Discussion

If your app targets tvOS 10 and later, use [`previouslyFocusedItem`](uifocusupdatecontext/previouslyfocuseditem.md) instead.

This property returns `nil` when no view was previously focused, such as when setting the initial focus.

## See Also

- [var nextFocusedView: UIView?](uifocusupdatecontext/nextfocusedview.md)
  The view that takes the focus after the focus update.
- [var focusHeading: UIFocusHeading](uifocusupdatecontext/focusheading.md)
  The heading in which the focus update is occurring.
- [struct UIFocusHeading](uifocusheading.md)
  The general type of an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/previouslyfocusedview)*