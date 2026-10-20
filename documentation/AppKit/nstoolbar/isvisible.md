# isVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the toolbar is visible.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var isVisible: Bool { get set }
```

```objc
@property (getter=isVisible) BOOL visible;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the toolbar is visible; otherwise, it’s [`false`](../../Swift/false.md). Change the value to hide or show the toolbar.

## See Also

### Configuring the toolbar’s behavior
- [var displayMode: NSToolbar.DisplayMode](./displaymode-swift.property.md)
  A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.
- [NSToolbar.DisplayMode](./displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var allowsUserCustomization: Bool](./allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.
- [var allowsExtensionItems: Bool](./allowsextensionitems.md)
  A Boolean value that indicates whether the toolbar can add items for Action extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/isvisible)*