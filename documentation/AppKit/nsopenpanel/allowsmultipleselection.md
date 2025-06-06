# allowsMultipleSelection

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the user may select multiple files and directories.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsMultipleSelection: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the user may select multiple items from the browser. When the selection contains multiple items, use the [`urls`](nsopenpanel/urls.md) property to retrieve those items instead of the inherited [`url`](nssavepanel/url.md) property.

## See Also

- [var canChooseFiles: Bool](nsopenpanel/canchoosefiles.md)
  A Boolean that indicates whether the user can choose files in the panel.
- [var canChooseDirectories: Bool](nsopenpanel/canchoosedirectories.md)
  A Boolean that indicates whether the user can choose directories in the panel.
- [var resolvesAliases: Bool](nsopenpanel/resolvesaliases.md)
  A Boolean that indicates whether the panel resolves aliases.
- [var isAccessoryViewDisclosed: Bool](nsopenpanel/isaccessoryviewdisclosed.md)
  A Boolean value that indicates whether the panel’s accessory view is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/allowsmultipleselection)*