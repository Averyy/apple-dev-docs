# previouslyFocusedItem

**Framework**: UIKit  
**Kind**: property

The item that was focused before the update.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var previouslyFocusedItem: (any UIFocusItem)? { get }
```

#### Discussion

This property is set to `nil` when there was no previously focused item.

## See Also

- [var nextFocusedItem: (any UIFocusItem)?](uifocusupdatecontext/nextfocuseditem.md)
  The item to be focused after the update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/previouslyfocuseditem)*