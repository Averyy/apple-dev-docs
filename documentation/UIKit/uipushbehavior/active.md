# active

**Framework**: UIKit  
**Kind**: property

The state of the push behavior’s force: either active or inactive.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var active: Bool { get set }
```

#### Discussion

After you’ve added a push behavior to a dynamic animator, use this property to activate or deactivate the behavior’s force (rather than removing and then re-adding the behavior to the animator).

## See Also

- [func addItem(any UIDynamicItem)](uipushbehavior/additem(_:).md)
  Adds a dynamic item to the behavior’s dynamic item array.
- [init(items: [any UIDynamicItem], mode: UIPushBehavior.Mode)](uipushbehavior/init(items:mode:).md)
  Initializes a push behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](uipushbehavior/removeitem(_:).md)
  Removes a specific dynamic item from the behavior.
- [var items: [any UIDynamicItem]](uipushbehavior/items.md)
  Returns the set of dynamic items you’ve added to the push behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/active)*