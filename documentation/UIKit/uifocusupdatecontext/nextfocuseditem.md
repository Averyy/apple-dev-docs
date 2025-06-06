# nextFocusedItem

**Framework**: UIKit  
**Kind**: property

The item to be focused after the update.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var nextFocusedItem: (any UIFocusItem)? { get }
```

#### Discussion

This property is set to `nil` if no item is receiving the focus.

## See Also

- [var previouslyFocusedItem: (any UIFocusItem)?](uifocusupdatecontext/previouslyfocuseditem.md)
  The item that was focused before the update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/nextfocuseditem)*