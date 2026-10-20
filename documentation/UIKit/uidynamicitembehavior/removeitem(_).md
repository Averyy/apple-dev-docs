# removeItem(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes a specific dynamic item from the dynamic item behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeItem(_ item: any UIDynamicItem)
```

```objc
- (void) removeItem:(id<UIDynamicItem>) item;
```

#### Discussion

## Parameters

- `item`: The dynamic item that you want to remove.

## See Also

### Initializing and managing a dynamic item behavior
- [func addItem(any UIDynamicItem)](./additem%28_%29.md)
  Adds a dynamic item to the dynamic item behavior’s item array.
- [init(items: [any UIDynamicItem])](./init%28items%29.md)
  Initializes a dynamic item behavior with an array of dynamic items.
- [var items: [any UIDynamicItem]](./items.md)
  Returns the set of dynamic items you’ve added to the dynamic item behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/removeitem(_:))*