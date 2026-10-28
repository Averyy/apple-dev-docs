# init(barButtonSystemItem:target:action:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an item using the specified system item, target, and action.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
convenience init(barButtonSystemItem systemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)
```

```objc
- (instancetype) initWithBarButtonSystemItem:(UIBarButtonSystemItem) systemItem target:(id) target action:(SEL) action;
```

## Return Value

A newly initialized [`UIBarButtonItem`](../uibarbuttonitem.md).

## Parameters

- `systemItem`: The system item to use as the first item on the bar. For possible values, see [`UIBarButtonItem.SystemItem`](./systemitem.md).
- `target`: The object that receives the `action` message.
- `action`: The action to send to `target` when a person selects this item.

## See Also

### Related Documentation
- [convenience init(image: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](./init%28image,style,target,action%29.md)
  Creates an item using the specified image, style, target, and action.
- [convenience init(title: String?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)](./init%28title,style,target,action%29.md)
  Creates an item using the specified title, style, target, and action.
### Creating system items
- [convenience init(systemItem: UIBarButtonItem.SystemItem, primaryAction: UIAction?, menu: UIMenu?)](./init%28systemitem,primaryaction,menu%29.md)
  Creates an item using the specified system item, primary action, and context menu.
- [UIBarButtonItem.SystemItem](./systemitem.md)
  Constants that define system-supplied images for bar button items.
- [- initWithBarButtonSystemItem:primaryAction:menu:](./initwithbarbuttonsystemitem_primaryaction_menu_.md)
  Creates an item using the specified system item, primary action, and context menu.
- [- initWithBarButtonSystemItem:primaryAction:](./initwithbarbuttonsystemitem_primaryaction_.md)
  Creates an item using the specified system item and primary action.
- [- initWithBarButtonSystemItem:menu:](./initwithbarbuttonsystemitem_menu_.md)
  Creates an item using the specified system item and context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(barbuttonsystemitem:target:action:))*