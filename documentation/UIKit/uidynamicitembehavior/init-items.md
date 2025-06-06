# init(items:)

**Framework**: UIKit  
**Kind**: init

Initializes a dynamic item behavior with an array of dynamic items.

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

The initialized dynamic item behavior, or `nil` if there was a problem initializing the object.

## Parameters

- `items`: The dynamic items that you want to be subject to the dynamic item behavior.

## See Also

- [func addItem(any UIDynamicItem)](uidynamicitembehavior/additem(_:).md)
  Adds a dynamic item to the dynamic item behavior’s item array.
- [func removeItem(any UIDynamicItem)](uidynamicitembehavior/removeitem(_:).md)
  Removes a specific dynamic item from the dynamic item behavior.
- [var items: [any UIDynamicItem]](uidynamicitembehavior/items.md)
  Returns the set of dynamic items you’ve added to the dynamic item behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/init(items:))*