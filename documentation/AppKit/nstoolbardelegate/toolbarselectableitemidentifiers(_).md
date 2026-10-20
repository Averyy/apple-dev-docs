# toolbarSelectableItemIdentifiers(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to provide the set of selectable items in the toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
@MainActor
optional func toolbarSelectableItemIdentifiers(_ toolbar: NSToolbar) -> [NSToolbarItem.Identifier]
```

```objc
- (NSArray<NSString *> *) toolbarSelectableItemIdentifiers:(NSToolbar *) toolbar;
```

#### Return Value

An array of item identifiers, each of which corresponds to an [`NSToolbarItem`](../nstoolbaritem.md) that should display a selection indicator in the specified toolbar.

#### Discussion

Use this method to return the complete list of toolbar items that support selection. When someone selects one of the returned items, the toolbar automatically displays that item with a visual highlight. The toolbar also places the currently selected item in its [`selectedItemIdentifier`](../nstoolbar/selecteditemidentifier.md) property.

## Parameters

- `toolbar`: The toolbar that contains the items.

## See Also

### Configuring the behavior of items
- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbaralloweditemidentifiers%28_%29.md)
  Asks the delegate to provide the items allowed on the toolbar.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](./toolbardefaultitemidentifiers%28_%29.md)
  Asks the delegate to provide the default items to display on the toolbar.
- [func toolbarImmovableItemIdentifiers(NSToolbar) -> Set<NSToolbarItem.Identifier>](./toolbarimmovableitemidentifiers%28_%29.md)
  Asks the delegate to provide the items that people can’t remove from the toolbar or rearrange during the customization process.
- [func toolbar(NSToolbar, itemIdentifier: NSToolbarItem.Identifier, canBeInsertedAt: Int) -> Bool](./toolbar%28_,itemidentifier,canbeinsertedat%29.md)
  Asks the delegate for a Boolean value that indicates whether the toolbar can place the item at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbardelegate/toolbarselectableitemidentifiers(_:))*