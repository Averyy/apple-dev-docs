# nextFocusedView

**Framework**: UIKit  
**Kind**: property

The view that takes the focus after the focus update.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
weak var nextFocusedView: UIView? { get }
```

#### Discussion

If your app targets tvOS 10 and later, use [`nextFocusedItem`](uifocusupdatecontext/nextfocuseditem.md) instead.

This property returns `nil` if no view will be focused after the update.

## See Also

- [var previouslyFocusedView: UIView?](uifocusupdatecontext/previouslyfocusedview.md)
  The view that was focused before the focus update.
- [var focusHeading: UIFocusHeading](uifocusupdatecontext/focusheading.md)
  The heading in which the focus update is occurring.
- [struct UIFocusHeading](uifocusheading.md)
  The general type of an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/nextfocusedview)*