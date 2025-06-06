# menuWillOpen(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when a menu is about to open.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func menuWillOpen(_ menu: NSMenu)
```

#### Discussion

Don’t modify the structure of the menu or the menu items during this method.

## Parameters

- `menu`: The menu that is about to open.

## See Also

- [func menuDidClose(NSMenu)](nsmenudelegate/menudidclose(_:).md)
  Invoked after a menu closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menuwillopen(_:))*