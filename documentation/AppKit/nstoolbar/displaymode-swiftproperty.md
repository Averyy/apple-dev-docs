# displayMode

**Framework**: AppKit  
**Kind**: property

A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var displayMode: NSToolbar.DisplayMode { get set }
```

#### Discussion

The default value of this property is [`NSToolbar.DisplayMode.default`](nstoolbar/displaymode-swift.enum/default.md). For a list of possible values, see [`NSToolbar.DisplayMode`](nstoolbar/displaymode-swift.enum.md).

## See Also

- [var isVisible: Bool](nstoolbar/isvisible.md)
  A Boolean value that indicates whether the toolbar is visible.
- [NSToolbar.DisplayMode](nstoolbar/displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var showsBaselineSeparator: Bool](nstoolbar/showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var allowsUserCustomization: Bool](nstoolbar/allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.
- [var allowsExtensionItems: Bool](nstoolbar/allowsextensionitems.md)
  A Boolean value that indicates whether the toolbar can add items for Action extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/displaymode-swift.property)*