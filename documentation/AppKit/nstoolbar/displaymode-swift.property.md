# displayMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var displayMode: NSToolbar.DisplayMode { get set }
```

```objc
@property NSToolbarDisplayMode displayMode;
```

#### Discussion

The default value of this property is [`NSToolbar.DisplayMode.default`](./displaymode-swift.enum/default.md). For a list of possible values, see [`NSToolbar.DisplayMode`](./displaymode-swift.enum.md).

## See Also

### Configuring the toolbar’s behavior
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the toolbar is visible.
- [NSToolbar.DisplayMode](./displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var allowsUserCustomization: Bool](./allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.
- [var allowsExtensionItems: Bool](./allowsextensionitems.md)
  A Boolean value that indicates whether the toolbar can add items for Action extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/displaymode-swift.property)*