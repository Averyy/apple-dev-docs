# showsHiddenFiles

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the panel displays files that are normally hidden from the user.

**Availability**:
- macOS

## Declaration

```swift
var showsHiddenFiles: Bool { get set }
```

```objc
@property BOOL showsHiddenFiles;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the panel displays hidden files; if [`false`](../../Swift/false.md), it does not. The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the Panel’s Behavior
- [var canCreateDirectories: Bool](./cancreatedirectories.md)
  A Boolean value that indicates whether the panel displays UI for creating directories.
- [var canSelectHiddenExtension: Bool](./canselecthiddenextension.md)
  A Boolean value that indicates whether the panel displays UI for hiding or showing filename extensions.
- [var isExtensionHidden: Bool](./isextensionhidden.md)
  A Boolean value that indicates whether to display filename extensions.
- [var isExpanded: Bool](./isexpanded.md)
  A Boolean value that indicates whether whether the panel is expanded.
- [Button tags](../button-tags.md)
  Button tags that refer to items on the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/showshiddenfiles)*