# removeItem(_:)

**Framework**: UIKit  
**Kind**: method

Removes a specific dynamic item from the behavior.

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

## Parameters

- `item`: The dynamic item that you want to remove.

## See Also

- [var active: Bool](uipushbehavior/active.md)
  The state of the push behavior’s force: either active or inactive.
- [func addItem(any UIDynamicItem)](uipushbehavior/additem(_:).md)
  Adds a dynamic item to the behavior’s dynamic item array.
- [init(items: [any UIDynamicItem], mode: UIPushBehavior.Mode)](uipushbehavior/init(items:mode:).md)
  Initializes a push behavior with an array of dynamic items.
- [var items: [any UIDynamicItem]](uipushbehavior/items.md)
  Returns the set of dynamic items you’ve added to the push behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/removeitem(_:))*