# isAccessoryViewDisclosed

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the panel’s accessory view is visible.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var isAccessoryViewDisclosed: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the accessory view is visible, and [`false`](https://developer.apple.com/documentation/Swift/false) when it isn’t. Setting the value of this property programmatically changes the visibility of the accessory panel. If no accessory panel is present, setting this property does nothing.

## See Also

- [var canChooseFiles: Bool](nsopenpanel/canchoosefiles.md)
  A Boolean that indicates whether the user can choose files in the panel.
- [var canChooseDirectories: Bool](nsopenpanel/canchoosedirectories.md)
  A Boolean that indicates whether the user can choose directories in the panel.
- [var resolvesAliases: Bool](nsopenpanel/resolvesaliases.md)
  A Boolean that indicates whether the panel resolves aliases.
- [var allowsMultipleSelection: Bool](nsopenpanel/allowsmultipleselection.md)
  A Boolean that indicates whether the user may select multiple files and directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/isaccessoryviewdisclosed)*