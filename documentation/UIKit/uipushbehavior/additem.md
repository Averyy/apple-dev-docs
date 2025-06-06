# addItem(_:)

**Framework**: UIKit  
**Kind**: method

Adds a dynamic item to the behavior’s dynamic item array.

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

All the dynamic items added to a push behavior are subject to the same force vector.

## Parameters

- `item`: The dynamic item to add to the item array.

## See Also

- [var active: Bool](uipushbehavior/active.md)
  The state of the push behavior’s force: either active or inactive.
- [init(items: [any UIDynamicItem], mode: UIPushBehavior.Mode)](uipushbehavior/init(items:mode:).md)
  Initializes a push behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](uipushbehavior/removeitem(_:).md)
  Removes a specific dynamic item from the behavior.
- [var items: [any UIDynamicItem]](uipushbehavior/items.md)
  Returns the set of dynamic items you’ve added to the push behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/additem(_:))*