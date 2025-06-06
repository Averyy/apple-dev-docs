# init(itemIdentifier:barButtonItem:)

**Framework**: AppKit  
**Kind**: init

Creates a toolbar item with property values from the specified bar button item.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
convenience init(itemIdentifier: NSToolbarItem.Identifier, barButtonItem: UIBarButtonItem)
```

#### Return Value

A new toolbar item.

#### Discussion

Use this method to create and initialize a toolbar item with property values from a [`UIBarButtonItem`](https://developer.apple.com/documentation/UIKit/UIBarButtonItem), such as [`title`](nstoolbaritem/title.md), [`image`](nstoolbaritem/image.md), [`action`](nstoolbaritem/action.md), and [`target`](nstoolbaritem/target.md).

> **Note**:  In macOS 12 and earlier, this method doesn’t support creating a toolbar item from a bar button item that contains a custom view.

 In macOS 12 and earlier, this method doesn’t support creating a toolbar item from a bar button item that contains a custom view.

## Parameters

- `itemIdentifier`: The identifier for the toolbar item. You use this value to identify the item within your app, so you don’t need to localize it. For example, your toolbar delegate uses this value to identify the specific toolbar item.
- `barButtonItem`: The bar button item to use to create the toolbar item.

## See Also

- [init(itemIdentifier: NSToolbarItem.Identifier)](nstoolbaritem/init(itemidentifier:).md)
  Creates a toolbar item with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/init(itemidentifier:barbuttonitem:))*