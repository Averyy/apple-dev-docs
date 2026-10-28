# init(itemIdentifier:barButtonItem:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a toolbar item with property values from the specified bar button item.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
convenience init(itemIdentifier: NSToolbarItem.Identifier, barButtonItem: UIBarButtonItem)
```

```objc
+ (instancetype) itemWithItemIdentifier:(NSToolbarItemIdentifier) itemIdentifier barButtonItem:(UIBarButtonItem *) barButtonItem;
```

## Return Value

A new toolbar item.

## Discussion

Use this method to create and initialize a toolbar item with property values from a [`UIBarButtonItem`](../../UIKit/uibarbuttonitem.md), such as [`title`](./title.md), [`image`](./image.md), [`action`](./action.md), and [`target`](./target.md).

> **Note**:  In macOS 12 and earlier, this method doesn’t support creating a toolbar item from a bar button item that contains a custom view.

## Parameters

- `itemIdentifier`: The identifier for the toolbar item. You use this value to identify the item within your app, so you don’t need to localize it. For example, your toolbar delegate uses this value to identify the specific toolbar item.
- `barButtonItem`: The bar button item to use to create the toolbar item.

## See Also

### Creating a toolbar item
- [init(itemIdentifier: NSToolbarItem.Identifier)](./init%28itemidentifier%29.md)
  Creates a toolbar item with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/init(itemidentifier:barbuttonitem:))*