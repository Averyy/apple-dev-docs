# userInterfaceLayoutDirection

**Framework**: AppKit  
**Kind**: property

The user interface layout direction.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection { get set }
```

#### Discussion

When set to [`NSUserInterfaceLayoutDirection.rightToLeft`](nsuserinterfacelayoutdirection/righttoleft.md), the outline view displays the disclosure triangle to the right of the cell instead of the left. The default value is [`NSUserInterfaceLayoutDirection.leftToRight`](nsuserinterfacelayoutdirection/lefttoright.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/userinterfacelayoutdirection)*