# allowsMultipleSelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user may select multiple files and directories.

**Availability**:
- macOS

## Declaration

```swift
var allowsMultipleSelection: Bool { get set }
```

```objc
@property BOOL allowsMultipleSelection;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the user may select multiple items from the browser. When the selection contains multiple items, use the [`urls`](./urls.md) property to retrieve those items instead of the inherited [`url`](../nssavepanel/url.md) property.

## See Also

### Configuring the Open Panel
- [var canChooseFiles: Bool](./canchoosefiles.md)
  A Boolean that indicates whether the user can choose files in the panel.
- [var canChooseDirectories: Bool](./canchoosedirectories.md)
  A Boolean that indicates whether the user can choose directories in the panel.
- [var resolvesAliases: Bool](./resolvesaliases.md)
  A Boolean that indicates whether the panel resolves aliases.
- [var isAccessoryViewDisclosed: Bool](./isaccessoryviewdisclosed.md)
  A Boolean value that indicates whether the panel’s accessory view is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/allowsmultipleselection)*