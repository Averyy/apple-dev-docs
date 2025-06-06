# init(items:)

**Framework**: UIKit  
**Kind**: init

Initializes a collision behavior with an array of dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(items: [any UIDynamicItem])
```

#### Return Value

The initialized collision behavior, or `nil` if there was a problem initializing the object.

## Parameters

- `items`: The dynamic items that you want to participate in the collision behavior.

## See Also

- [func addItem(any UIDynamicItem)](uicollisionbehavior/additem(_:).md)
  Adds a dynamic item to the collision behavior’s item array.
- [func removeItem(any UIDynamicItem)](uicollisionbehavior/removeitem(_:).md)
  Removes a specific dynamic item from the collision behavior.
- [var items: [any UIDynamicItem]](uicollisionbehavior/items.md)
  Returns the set of dynamic items you’ve added to the collision behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/init(items:))*