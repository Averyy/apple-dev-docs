# isHidden

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the menu item is hidden.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isHidden: Bool { get set }
```

#### Discussion

Hidden menu items (or items with a hidden superitem) do not appear in a menu and do not participate in command key matching.

## See Also

- [var isHiddenOrHasHiddenAncestor: Bool](nsmenuitem/ishiddenorhashiddenancestor.md)
  A Boolean value that indicates whether the menu item or any of its superitems is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/ishidden)*