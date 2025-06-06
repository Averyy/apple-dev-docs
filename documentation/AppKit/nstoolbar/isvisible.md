# isVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar is visible.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var isVisible: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the toolbar is visible; otherwise, it’s [`false`](https://developer.apple.com/documentation/swift/false). Change the value to hide or show the toolbar.

## See Also

- [var displayMode: NSToolbar.DisplayMode](nstoolbar/displaymode-swift.property.md)
  A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.
- [NSToolbar.DisplayMode](nstoolbar/displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var showsBaselineSeparator: Bool](nstoolbar/showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var allowsUserCustomization: Bool](nstoolbar/allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.
- [var allowsExtensionItems: Bool](nstoolbar/allowsextensionitems.md)
  A Boolean value that indicates whether the toolbar can add items for Action extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/isvisible)*