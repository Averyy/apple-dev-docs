# init(itemIdentifier:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a toolbar item with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
init(itemIdentifier: NSToolbarItem.Identifier)
```

```objc
- (instancetype) initWithItemIdentifier:(NSToolbarItemIdentifier) itemIdentifier;
```

## Return Value

A new toolbar item.

## Parameters

- `itemIdentifier`: The identifier for the toolbar item. You use this value to identify the item within your app, so you don’t need to localize it. For example, your toolbar delegate uses this value to identify the specific toolbar item.

## See Also

### Related Documentation
- [Integrating a Toolbar and Touch Bar into Your App](../integrating-a-toolbar-and-touch-bar-into-your-app.md)
  Provide users quick access to your app’s features from a toolbar and corresponding Touch Bar.
### Creating a toolbar item
- [convenience init(itemIdentifier: NSToolbarItem.Identifier, barButtonItem: UIBarButtonItem)](./init%28itemidentifier,barbuttonitem%29.md)
  Creates a toolbar item with property values from the specified bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/init(itemidentifier:))*