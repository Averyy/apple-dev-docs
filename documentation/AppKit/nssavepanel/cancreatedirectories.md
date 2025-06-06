# canCreateDirectories

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the panel displays UI for creating directories.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var canCreateDirectories: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the panel includes UI to create new directories. When the value is [`false`](https://developer.apple.com/documentation/swift/false), the panel does not expose that UI.

## See Also

- [var canSelectHiddenExtension: Bool](nssavepanel/canselecthiddenextension.md)
  A Boolean value that indicates whether the panel displays UI for hiding or showing filename extensions.
- [var showsHiddenFiles: Bool](nssavepanel/showshiddenfiles.md)
  A Boolean value that indicates whether the panel displays files that are normally hidden from the user.
- [var isExtensionHidden: Bool](nssavepanel/isextensionhidden.md)
  A Boolean value that indicates whether to display filename extensions.
- [var isExpanded: Bool](nssavepanel/isexpanded.md)
  A Boolean value that indicates whether whether the panel is expanded.
- [Button tags](button-tags.md)
  Button tags that refer to items on the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/cancreatedirectories)*