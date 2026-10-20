# addOption(withTitle:image:order:handler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a custom menu item to the list of document pickers.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIDocumentMenuViewController`](../uidocumentmenuviewcontroller.md).

## Declaration

```swift
func addOption(withTitle title: String, image: UIImage?, order: UIDocumentMenuOrder, handler: @escaping () -> Void)
```

```objc
- (void) addOptionWithTitle:(NSString *) title image:(UIImage *) image order:(UIDocumentMenuOrder) order handler:(void (^)()) handler;
```

## Parameters

- `title`: The custom menu item’s title.
- `image`: The custom menu item’s image.
- `order`: The position of this menu item. See [`UIDocumentMenuOrder`](../uidocumentmenuorder.md) for possible values.
- `handler`: A block that is called when the user selects this custom menu item.

## See Also

### Configuring a document menu
- [enum UIDocumentMenuOrder](../uidocumentmenuorder.md)
  The insertion point for custom menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/addoption(withtitle:image:order:handler:))*