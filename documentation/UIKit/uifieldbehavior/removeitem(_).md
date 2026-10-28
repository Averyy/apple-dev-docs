# removeItem(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the field behavior from the specified dynamic item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeItem(_ item: any UIDynamicItem)
```

```objc
- (void) removeItem:(id<UIDynamicItem>) item;
```

## Discussion

Use this method to remove a field from a dynamic item in your interface. This method removes the specified dynamic item from the field behavior’s list of dynamic item.

## Parameters

- `item`: The dynamic item whose behavior you want to modify.

## See Also

### Managing the associated dynamic items
- [func addItem(any UIDynamicItem)](./additem%28_%29.md)
  Associates the field behavior with the specified dynamic item.
- [var items: [any UIDynamicItem]](./items.md)
  The dynamic items associated with the current field behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/removeitem(_:))*