# allowsExtensionItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the toolbar can add items for Action extensions.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var allowsExtensionItems: Bool { get set }
```

```objc
@property BOOL allowsExtensionItems;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the toolbar can dynamically create toolbar items for Action extensions in the toolbar configuration panel. The toolbar can only add an Action extension if its `Info.plist` file contains the [`NSExtensionServiceAllowsToolbarItem`](../../BundleResources/information-property-list/nsextension/nsextensionattributes/nsextensionserviceallowstoolbaritem.md) key with the value [`true`](../../Swift/true.md). The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the toolbar’s behavior
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the toolbar is visible.
- [var displayMode: NSToolbar.DisplayMode](./displaymode-swift.property.md)
  A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.
- [NSToolbar.DisplayMode](./displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var allowsUserCustomization: Bool](./allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/allowsextensionitems)*