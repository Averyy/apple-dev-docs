# addItem(_:)

**Framework**: UIKit  
**Kind**: method

Associates the specified dynamic item with the gravity behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addItem(_ item: any UIDynamicItem)
```

#### Discussion

Use this method to add new dynamic items to the gravity behavior after initialization. All the dynamic items added to a gravity behavior are subject to the same gravity vector.

If the gravity behavior has an associated dynamic animator, this method notifies the dynamic animator of the presence of the new item so that it can initiate any needed animations.

## Parameters

- `item`: The dynamic item to add to the item array. If the specified item is already associated with the gravity behavior, this method does nothing.

## See Also

- [var items: [any UIDynamicItem]](uigravitybehavior/items.md)
  The set of dynamic items associated with the gravity behavior.
- [func removeItem(any UIDynamicItem)](uigravitybehavior/removeitem(_:).md)
  Removes the specified dynamic item from the gravity behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigravitybehavior/additem(_:))*