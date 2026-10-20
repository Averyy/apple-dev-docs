# addItem(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a dynamic item to the dynamic item behavior’s item array.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func addItem(_ item: any UIDynamicItem)
```

```objc
- (void) addItem:(id<UIDynamicItem>) item;
```

#### Discussion

You can add a dynamic item to one or more dynamic item behaviors. For example, you could add a dynamic item to one dynamic item behavior to configure the item’s elasticity and to a second dynamic item behavior to configure its density. This is especially useful when you are defining custom, combined behaviors for your dynamic items.

## Parameters

- `item`: The dynamic item to add to the item array.

## See Also

### Initializing and managing a dynamic item behavior
- [init(items: [any UIDynamicItem])](./init%28items%29.md)
  Initializes a dynamic item behavior with an array of dynamic items.
- [func removeItem(any UIDynamicItem)](./removeitem%28_%29.md)
  Removes a specific dynamic item from the dynamic item behavior.
- [var items: [any UIDynamicItem]](./items.md)
  Returns the set of dynamic items you’ve added to the dynamic item behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/additem(_:))*