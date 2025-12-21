# canChooseFiles

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the user can choose files in the panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var canChooseFiles: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), users can choose files in the panel.

## See Also

- [var canChooseDirectories: Bool](nsopenpanel/canchoosedirectories.md)
  A Boolean that indicates whether the user can choose directories in the panel.
- [var resolvesAliases: Bool](nsopenpanel/resolvesaliases.md)
  A Boolean that indicates whether the panel resolves aliases.
- [var allowsMultipleSelection: Bool](nsopenpanel/allowsmultipleselection.md)
  A Boolean that indicates whether the user may select multiple files and directories.
- [var isAccessoryViewDisclosed: Bool](nsopenpanel/isaccessoryviewdisclosed.md)
  A Boolean value that indicates whether the panel’s accessory view is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/canchoosefiles)*