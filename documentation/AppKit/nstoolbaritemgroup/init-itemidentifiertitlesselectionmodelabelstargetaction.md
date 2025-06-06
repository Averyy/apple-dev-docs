# init(itemIdentifier:titles:selectionMode:labels:target:action:)

**Framework**: AppKit  
**Kind**: init

Creates a grouped toolbar item with labels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
convenience init(itemIdentifier: NSToolbarItem.Identifier, titles: [String], selectionMode: NSToolbarItemGroup.SelectionMode, labels: [String]?, target: Any?, action: Selector?)
```

## Parameters

- `itemIdentifier`: The identifier for the grouped toolbar item.
- `titles`: An array of titles to present as subitems in the grouped toolbar item.
- `selectionMode`: A Boolean value that indicates how the grouped toolbar item presents selections.
- `labels`: Labels that correspond to the specified titles.
- `target`: If target is  , the toolbar attempts to invoke the specified action on the first responder and, failing that, passes the action up the responder chain.
- `action`: The selector that the toolbar invokes on the target.

## See Also

- [convenience init(itemIdentifier: NSToolbarItem.Identifier, images: [UIImage], selectionMode: NSToolbarItemGroup.SelectionMode, labels: [String]?, target: Any?, action: Selector?)](nstoolbaritemgroup/init(itemidentifier:images:selectionmode:labels:target:action:).md)
  Creates a grouped toolbar item with images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/init(itemidentifier:titles:selectionmode:labels:target:action:))*