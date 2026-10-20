# canChooseDirectories

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user can choose directories in the panel.

**Availability**:
- macOS

## Declaration

```swift
var canChooseDirectories: Bool { get set }
```

```objc
@property BOOL canChooseDirectories;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), users can choose directories in the panel.

## See Also

### Configuring the Open Panel
- [var canChooseFiles: Bool](./canchoosefiles.md)
  A Boolean that indicates whether the user can choose files in the panel.
- [var resolvesAliases: Bool](./resolvesaliases.md)
  A Boolean that indicates whether the panel resolves aliases.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean that indicates whether the user may select multiple files and directories.
- [var isAccessoryViewDisclosed: Bool](./isaccessoryviewdisclosed.md)
  A Boolean value that indicates whether the panel’s accessory view is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/canchoosedirectories)*