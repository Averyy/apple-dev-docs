# init(itemIdentifier:)

**Framework**: AppKit  
**Kind**: init

Creates a toolbar item with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
init(itemIdentifier: NSToolbarItem.Identifier)
```

#### Return Value

A new toolbar item.

## Parameters

- `itemIdentifier`: The identifier for the toolbar item. You use this value to identify the item within your app, so you don’t need to localize it. For example, your toolbar delegate uses this value to identify the specific toolbar item.

## See Also

- [Toolbar Programming Topics for Cocoa](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Toolbars.html#//apple_ref/doc/uid/10000109i)
- [convenience init(itemIdentifier: NSToolbarItem.Identifier, barButtonItem: UIBarButtonItem)](nstoolbaritem/init(itemidentifier:barbuttonitem:).md)
  Creates a toolbar item with property values from the specified bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/init(itemidentifier:))*