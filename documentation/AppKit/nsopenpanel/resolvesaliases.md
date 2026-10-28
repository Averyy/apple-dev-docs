# resolvesAliases

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the panel resolves aliases.

**Availability**:
- macOS

## Declaration

```swift
var resolvesAliases: Bool { get set }
```

```objc
@property BOOL resolvesAliases;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), dropping an alias on the panel or asking for filenames or URLs returns the resolved aliases. The default value of this property is [`true`](../../Swift/true.md). When this value is [`false`](../../Swift/false.md), selecting an alias returns the alias instead of the file or directory it represents.

## See Also

### Configuring the Open Panel
- [var canChooseFiles: Bool](./canchoosefiles.md)
  A Boolean that indicates whether the user can choose files in the panel.
- [var canChooseDirectories: Bool](./canchoosedirectories.md)
  A Boolean that indicates whether the user can choose directories in the panel.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean that indicates whether the user may select multiple files and directories.
- [var isAccessoryViewDisclosed: Bool](./isaccessoryviewdisclosed.md)
  A Boolean value that indicates whether the panel’s accessory view is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/resolvesaliases)*