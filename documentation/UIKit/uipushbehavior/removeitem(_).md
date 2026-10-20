# removeItem(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes a specific dynamic item from the behavior.

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

## Parameters

- `item`: The dynamic item that you want to remove.

## See Also

### Initializing and managing a push behavior
- [var active: Bool](./active.md)
  The state of the push behavior’s force: either active or inactive.
- [func addItem(any UIDynamicItem)](./additem%28_%29.md)
  Adds a dynamic item to the behavior’s dynamic item array.
- [init(items: [any UIDynamicItem], mode: UIPushBehavior.Mode)](./init%28items,mode%29.md)
  Initializes a push behavior with an array of dynamic items.
- [var items: [any UIDynamicItem]](./items.md)
  Returns the set of dynamic items you’ve added to the push behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/removeitem(_:))*