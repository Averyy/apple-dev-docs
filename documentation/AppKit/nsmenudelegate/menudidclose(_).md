# menuDidClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked after a menu closed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func menuDidClose(_ menu: NSMenu)
```

```objc
- (void) menuDidClose:(NSMenu *) menu;
```

#### Discussion

Don’t modify the structure of the menu or the menu items during this method.

## Parameters

- `menu`: The menu that closed.

## See Also

### Handling Open and Close Events
- [func menuWillOpen(NSMenu)](./menuwillopen%28_%29.md)
  Invoked when a menu is about to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menudidclose(_:))*