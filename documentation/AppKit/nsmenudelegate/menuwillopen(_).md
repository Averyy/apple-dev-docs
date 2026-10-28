# menuWillOpen(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when a menu is about to open.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func menuWillOpen(_ menu: NSMenu)
```

```objc
- (void) menuWillOpen:(NSMenu *) menu;
```

## Discussion

Don’t modify the structure of the menu or the menu items during this method.

## Parameters

- `menu`: The menu that is about to open.

## See Also

### Handling Open and Close Events
- [func menuDidClose(NSMenu)](./menudidclose%28_%29.md)
  Invoked after a menu closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menuwillopen(_:))*