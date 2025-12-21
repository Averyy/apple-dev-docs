# canSelectHiddenExtension

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the panel displays UI for hiding or showing filename extensions.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var canSelectHiddenExtension: Bool { get set }
```

#### Discussion

Set the value of this property before displaying the panel. When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), and the Finder preference “Show all extensions” is [`false`](https://developer.apple.com/documentation/Swift/false), the panel displays the Hide Extension menu item. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

Use the [`isExtensionHidden`](nssavepanel/isextensionhidden.md) property to hide or shows extensions.

## See Also

- [var canCreateDirectories: Bool](nssavepanel/cancreatedirectories.md)
  A Boolean value that indicates whether the panel displays UI for creating directories.
- [var showsHiddenFiles: Bool](nssavepanel/showshiddenfiles.md)
  A Boolean value that indicates whether the panel displays files that are normally hidden from the user.
- [var isExtensionHidden: Bool](nssavepanel/isextensionhidden.md)
  A Boolean value that indicates whether to display filename extensions.
- [var isExpanded: Bool](nssavepanel/isexpanded.md)
  A Boolean value that indicates whether whether the panel is expanded.
- [Button tags](button-tags.md)
  Button tags that refer to items on the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/canselecthiddenextension)*