# initWithBarButtonSystemItem:primaryAction:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates an item using the specified system item and primary action.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithBarButtonSystemItem:(UIBarButtonSystemItem) systemItem primaryAction:(UIAction *) primaryAction;
```

#### Return Value

A newly initialized [`UIBarButtonItem`](../uibarbuttonitem.md).

## Parameters

- `systemItem`: The system item to use as the first item on the bar. For possible values, see [`UIBarButtonItem.SystemItem`](./systemitem.md).
- `primaryAction`: A [`UIAction`](../uiaction.md) to associate with the item. The system item doesn’t use the action to configure its title and image.

## See Also

### Creating system items
- [- initWithBarButtonSystemItem:primaryAction:menu:](./initwithbarbuttonsystemitem_primaryaction_menu_.md)
  Creates an item using the specified system item, primary action, and context menu.
- [- initWithBarButtonSystemItem:menu:](./initwithbarbuttonsystemitem_menu_.md)
  Creates an item using the specified system item and context menu.
- [convenience init(barButtonSystemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)](./init%28barbuttonsystemitem,target,action%29.md)
  Creates an item using the specified system item, target, and action.
- [UIBarButtonItem.SystemItem](./systemitem.md)
  Constants that define system-supplied images for bar button items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithbarbuttonsystemitem:primaryaction:)*