# resolvesAliases

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the panel resolves aliases.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var resolvesAliases: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), dropping an alias on the panel or asking for filenames or URLs returns the resolved aliases. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true). When this value is [`false`](https://developer.apple.com/documentation/Swift/false), selecting an alias returns the alias instead of the file or directory it represents.

## See Also

- [var canChooseFiles: Bool](nsopenpanel/canchoosefiles.md)
  A Boolean that indicates whether the user can choose files in the panel.
- [var canChooseDirectories: Bool](nsopenpanel/canchoosedirectories.md)
  A Boolean that indicates whether the user can choose directories in the panel.
- [var allowsMultipleSelection: Bool](nsopenpanel/allowsmultipleselection.md)
  A Boolean that indicates whether the user may select multiple files and directories.
- [var isAccessoryViewDisclosed: Bool](nsopenpanel/isaccessoryviewdisclosed.md)
  A Boolean value that indicates whether the panel’s accessory view is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/resolvesaliases)*