# removeItem(_:)

**Framework**: UIKit  
**Kind**: method

Removes the specified dynamic item from the gravity behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeItem(_ item: any UIDynamicItem)
```

#### Discussion

If the gravity behavior has an associated dynamic animator, this method notifies the dynamic animator of the removal of the item so that it can stop any associated animations.

## Parameters

- `item`: The dynamic item that you want to remove. If the specified item is not associated with the behavior, this method does nothing.

## See Also

- [var items: [any UIDynamicItem]](uigravitybehavior/items.md)
  The set of dynamic items associated with the gravity behavior.
- [func addItem(any UIDynamicItem)](uigravitybehavior/additem(_:).md)
  Associates the specified dynamic item with the gravity behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigravitybehavior/removeitem(_:))*