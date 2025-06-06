# items

**Framework**: UIKit  
**Kind**: property

Returns the set of dynamic items you’ve added to the push behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var items: [any UIDynamicItem] { get }
```

## See Also

- [var active: Bool](uipushbehavior/active.md)
  The state of the push behavior’s force: either active or inactive.
- [func addItem(any UIDynamicItem)](uipushbehavior/additem(_:).md)
  Adds a dynamic item to the behavior’s dynamic item array.
- [init(items: [any UIDynamicItem], mode: UIPushBehavior.Mode)](uipushbehavior/init(items:mode:).md)
  Initializes a push behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](uipushbehavior/removeitem(_:).md)
  Removes a specific dynamic item from the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/items)*