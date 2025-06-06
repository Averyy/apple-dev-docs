# validate()

**Framework**: AppKit  
**Kind**: method

Validates the toolbar item’s menu and its ability to perfrom its action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
func validate()
```

#### Discussion

Typically, you don’t call this method directly. When automatic validation is enabled, the toolbar calls this method to validate the item. For standard toolbar items — that is, items without a custom view — the validation process checks whether the item can perform its associated action successfully and enables or disables the item accordingly. The process also validates the associated menu item. When someone switches to another app or window, the automatic validation process disables the item automatically.

If the toolbar item has a custom view, subclass [`NSToolbarItem`](nstoolbaritem.md) and override this method to perform the validation yourself. After you validate your custom toolbar item, update the [`isEnabled`](nstoolbaritem/isenabled.md) property. You don’t need to call `super` in your implementation.

If you disable automatic validation, toolbar items remain enabled and clickable, including when someone switches to another app or window. However, you can still call this method manually to validate the toolbar item.

## See Also

- [var isEnabled: Bool](nstoolbaritem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
- [var autovalidates: Bool](nstoolbaritem/autovalidates.md)
  A Boolean value that indicates whether the toolbar automatically validates the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/validate())*