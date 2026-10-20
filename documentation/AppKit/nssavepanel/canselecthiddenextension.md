# canSelectHiddenExtension

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the panel displays UI for hiding or showing filename extensions.

**Availability**:
- macOS

## Declaration

```swift
var canSelectHiddenExtension: Bool { get set }
```

```objc
@property BOOL canSelectHiddenExtension;
```

#### Discussion

Set the value of this property before displaying the panel. When the value of this property is [`true`](../../Swift/true.md), and the Finder preference “Show all extensions” is [`false`](../../Swift/false.md), the panel displays the Hide Extension menu item. The default value of this property is [`false`](../../Swift/false.md).

Use the [`isExtensionHidden`](./isextensionhidden.md) property to hide or shows extensions.

## See Also

### Configuring the Panel’s Behavior
- [var canCreateDirectories: Bool](./cancreatedirectories.md)
  A Boolean value that indicates whether the panel displays UI for creating directories.
- [var showsHiddenFiles: Bool](./showshiddenfiles.md)
  A Boolean value that indicates whether the panel displays files that are normally hidden from the user.
- [var isExtensionHidden: Bool](./isextensionhidden.md)
  A Boolean value that indicates whether to display filename extensions.
- [var isExpanded: Bool](./isexpanded.md)
  A Boolean value that indicates whether whether the panel is expanded.
- [Button tags](../button-tags.md)
  Button tags that refer to items on the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/canselecthiddenextension)*