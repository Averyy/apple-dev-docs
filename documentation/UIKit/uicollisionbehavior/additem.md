# addItem(_:)

**Framework**: UIKit  
**Kind**: method

Adds a dynamic item to the collision behavior’s item array.

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

You can add a dynamic item to one or more collision behaviors. For example, you can use two collision behaviors to specify that item  can collide with item  and that item  can collide with item , but that items  and  ignore items  and .

There is no hard limit to the number of dynamic items you can add to a collision behavior. However, adding a large number of items might result in a performance impact. Be sure to test your behaviors on the device configurations you are targeting.

## Parameters

- `item`: The dynamic item to add to the item array.

## See Also

- [init(items: [any UIDynamicItem])](uicollisionbehavior/init(items:).md)
  Initializes a collision behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](uicollisionbehavior/removeitem(_:).md)
  Removes a specific dynamic item from the collision behavior.
- [var items: [any UIDynamicItem]](uicollisionbehavior/items.md)
  Returns the set of dynamic items you’ve added to the collision behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/additem(_:))*