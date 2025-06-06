# delegate

**Framework**: AppKit  
**Kind**: property

The delegate of the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var delegate: (any NSMenuDelegate)? { get set }
```

#### Discussion

This property indicates the delegate of the menu.

You can use the delegate to populate a menu just before it is drawn and to check for key equivalents without creating a menu item.

## See Also

- [protocol NSMenuDelegate](nsmenudelegate.md)
  The optional methods implemented by delegates of [`NSMenu`](nsmenu.md) objects to manage menu display and handle some events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/delegate)*