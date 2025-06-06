# addOption(withTitle:image:order:handler:)

**Framework**: UIKit  
**Kind**: method

Adds a custom menu item to the list of document pickers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func addOption(withTitle title: String, image: UIImage?, order: UIDocumentMenuOrder, handler: @escaping () -> Void)
```

## Parameters

- `title`: The custom menu item’s title.
- `image`: The custom menu item’s image.
- `order`: The position of this menu item. See   for possible values.
- `handler`: A block that is called when the user selects this custom menu item.

## See Also

- [enum UIDocumentMenuOrder](uidocumentmenuorder.md)
  The insertion point for custom menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/addoption(withtitle:image:order:handler:))*