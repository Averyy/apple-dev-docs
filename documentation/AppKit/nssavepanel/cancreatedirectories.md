# canCreateDirectories

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the panel displays UI for creating directories.

**Availability**:
- macOS

## Declaration

```swift
var canCreateDirectories: Bool { get set }
```

```objc
@property BOOL canCreateDirectories;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the panel includes UI to create new directories. When the value is [`false`](../../Swift/false.md), the panel does not expose that UI.

## See Also

### Configuring the Panel’s Behavior
- [var canSelectHiddenExtension: Bool](./canselecthiddenextension.md)
  A Boolean value that indicates whether the panel displays UI for hiding or showing filename extensions.
- [var showsHiddenFiles: Bool](./showshiddenfiles.md)
  A Boolean value that indicates whether the panel displays files that are normally hidden from the user.
- [var isExtensionHidden: Bool](./isextensionhidden.md)
  A Boolean value that indicates whether to display filename extensions.
- [var isExpanded: Bool](./isexpanded.md)
  A Boolean value that indicates whether whether the panel is expanded.
- [Button tags](../button-tags.md)
  Button tags that refer to items on the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/cancreatedirectories)*