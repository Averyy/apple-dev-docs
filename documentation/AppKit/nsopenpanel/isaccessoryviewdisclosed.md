# isAccessoryViewDisclosed

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the panel’s accessory view is visible.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var isAccessoryViewDisclosed: Bool { get set }
```

```objc
@property (getter=isAccessoryViewDisclosed) BOOL accessoryViewDisclosed;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the accessory view is visible, and [`false`](../../Swift/false.md) when it isn’t. Setting the value of this property programmatically changes the visibility of the accessory panel. If no accessory panel is present, setting this property does nothing.

## See Also

### Configuring the Open Panel
- [var canChooseFiles: Bool](./canchoosefiles.md)
  A Boolean that indicates whether the user can choose files in the panel.
- [var canChooseDirectories: Bool](./canchoosedirectories.md)
  A Boolean that indicates whether the user can choose directories in the panel.
- [var resolvesAliases: Bool](./resolvesaliases.md)
  A Boolean that indicates whether the panel resolves aliases.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean that indicates whether the user may select multiple files and directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/isaccessoryviewdisclosed)*