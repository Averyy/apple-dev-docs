# isExpanded

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether whether the panel is expanded.

**Availability**:
- macOS

## Declaration

```swift
var isExpanded: Bool { get }
```

```objc
@property (readonly, getter=isExpanded) BOOL expanded;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the panel is expanded; otherwise, [`false`](../../Swift/false.md).

## See Also

### Configuring the Panel’s Behavior
- [var canCreateDirectories: Bool](./cancreatedirectories.md)
  A Boolean value that indicates whether the panel displays UI for creating directories.
- [var canSelectHiddenExtension: Bool](./canselecthiddenextension.md)
  A Boolean value that indicates whether the panel displays UI for hiding or showing filename extensions.
- [var showsHiddenFiles: Bool](./showshiddenfiles.md)
  A Boolean value that indicates whether the panel displays files that are normally hidden from the user.
- [var isExtensionHidden: Bool](./isextensionhidden.md)
  A Boolean value that indicates whether to display filename extensions.
- [Button tags](../button-tags.md)
  Button tags that refer to items on the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/isexpanded)*