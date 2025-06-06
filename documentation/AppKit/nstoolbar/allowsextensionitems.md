# allowsExtensionItems

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar can add items for Action extensions.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var allowsExtensionItems: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the toolbar can dynamically create toolbar items for Action extensions in the toolbar configuration panel. The toolbar can only add an Action extension if its `Info.plist` file contains the [`NSExtensionServiceAllowsToolbarItem`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionServiceAllowsToolbarItem) key with the value [`true`](https://developer.apple.com/documentation/swift/true). The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isVisible: Bool](nstoolbar/isvisible.md)
  A Boolean value that indicates whether the toolbar is visible.
- [var displayMode: NSToolbar.DisplayMode](nstoolbar/displaymode-swift.property.md)
  A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.
- [NSToolbar.DisplayMode](nstoolbar/displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var showsBaselineSeparator: Bool](nstoolbar/showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var allowsUserCustomization: Bool](nstoolbar/allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/allowsextensionitems)*