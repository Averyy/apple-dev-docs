# init(items:mode:)

**Framework**: UIKit  
**Kind**: init

Initializes a push behavior with an array of dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(items: [any UIDynamicItem], mode: UIPushBehavior.Mode)
```

#### Return Value

The initialized push behavior, or `nil` if there was a problem initializing the object.

## Parameters

- `items`: The dynamic items that you want to be subject to the push behavior.
- `mode`: The mode for the new push behavior; one of the values defined in the   enumeration. You must supply a value.

## See Also

- [var active: Bool](uipushbehavior/active.md)
  The state of the push behavior’s force: either active or inactive.
- [func addItem(any UIDynamicItem)](uipushbehavior/additem(_:).md)
  Adds a dynamic item to the behavior’s dynamic item array.
- [func removeItem(any UIDynamicItem)](uipushbehavior/removeitem(_:).md)
  Removes a specific dynamic item from the behavior.
- [var items: [any UIDynamicItem]](uipushbehavior/items.md)
  Returns the set of dynamic items you’ve added to the push behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/init(items:mode:))*