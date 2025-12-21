# allowsUserCustomization

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether users can modify the contents of the toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var allowsUserCustomization: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the toolbar enables the Customize Toolbar… menu item. If the value is [`false`](https://developer.apple.com/documentation/Swift/false), the toolbar disables this menu item. The Customize Toolbar… menu item lets people change the items on the toolbar, rearrange their positions, and change the toolbar’s display mode. This attribute does not affect someone’s ability to show or hide the toolbar. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

You can change the value of this property at any time to change your toolbar’s customization behavior. For example, you might prevent toolbar customizations while your app processes some other event. If you set this property to [`true`](https://developer.apple.com/documentation/Swift/true), set the [`autosavesConfiguration`](nstoolbar/autosavesconfiguration.md) property to true to persist any customizations.

## See Also

- [var isVisible: Bool](nstoolbar/isvisible.md)
  A Boolean value that indicates whether the toolbar is visible.
- [var displayMode: NSToolbar.DisplayMode](nstoolbar/displaymode-swift.property.md)
  A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.
- [NSToolbar.DisplayMode](nstoolbar/displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var showsBaselineSeparator: Bool](nstoolbar/showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var allowsExtensionItems: Bool](nstoolbar/allowsextensionitems.md)
  A Boolean value that indicates whether the toolbar can add items for Action extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/allowsusercustomization)*