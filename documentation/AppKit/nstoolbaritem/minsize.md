# minSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The toolbar item’s minimum size.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: This property is no longer recommended. Instead, let the system automatically measure the size of the view using constraints.

## Declaration

```swift
var minSize: NSSize { get set }
```

```objc
@property NSSize minSize;
```

#### Discussion

See [Setting a Toolbar Item’s Size](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Tasks/SettingTBItemSize.html#//apple_ref/doc/uid/20000754) for a discussion on item sizes.

## See Also

### Deprecated
- [var allowsDuplicatesInToolbar: Bool](./allowsduplicatesintoolbar.md)
  A Boolean value that indicates whether the toolbar item can appear more than once in a toolbar.
- [var maxSize: NSSize](./maxsize.md)
  The toolbar item’s maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/minsize)*