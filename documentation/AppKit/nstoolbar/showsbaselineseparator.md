# showsBaselineSeparator

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var showsBaselineSeparator: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the toolbar shows the separator between the toolbar and the main window contents. If the value is [`false`](https://developer.apple.com/documentation/swift/false), the toolbar doesn’t show the separator. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isVisible: Bool](nstoolbar/isvisible.md)
  A Boolean value that indicates whether the toolbar is visible.
- [var displayMode: NSToolbar.DisplayMode](nstoolbar/displaymode-swift.property.md)
  A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.
- [NSToolbar.DisplayMode](nstoolbar/displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var allowsUserCustomization: Bool](nstoolbar/allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.
- [var allowsExtensionItems: Bool](nstoolbar/allowsextensionitems.md)
  A Boolean value that indicates whether the toolbar can add items for Action extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/showsbaselineseparator)*