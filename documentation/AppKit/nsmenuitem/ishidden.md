# isHidden

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the menu item is hidden.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (getter=isHidden) BOOL hidden;
```

#### Discussion

Hidden menu items (or items with a hidden superitem) do not appear in a menu and do not participate in command key matching.

## See Also

### Managing hidden status
- [var isHiddenOrHasHiddenAncestor: Bool](./ishiddenorhashiddenancestor.md)
  A Boolean value that indicates whether the menu item or any of its superitems is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/ishidden)*