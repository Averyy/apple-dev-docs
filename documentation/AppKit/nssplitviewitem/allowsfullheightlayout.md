# allowsFullHeightLayout

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether full-height sidebars appear in the window after you set a style mask.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var allowsFullHeightLayout: Bool { get set }
```

#### Discussion

This property only applies to [`NSSplitViewItem.Behavior.sidebar`](nssplitviewitem/behavior-swift.enum/sidebar.md) and [`NSSplitViewItem.Behavior.inspector`](nssplitviewitem/behavior-swift.enum/inspector.md). The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](nssplitviewitem/titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/allowsfullheightlayout)*