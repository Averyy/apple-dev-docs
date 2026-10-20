# allowsFullHeightLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether full-height sidebars appear in the window after you set a style mask.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var allowsFullHeightLayout: Bool { get set }
```

```objc
@property BOOL allowsFullHeightLayout;
```

#### Discussion

This property only applies to [`NSSplitViewItem.Behavior.sidebar`](./behavior-swift.enum/sidebar.md) and [`NSSplitViewItem.Behavior.inspector`](./behavior-swift.enum/inspector.md). The default value is [`true`](../../Swift/true.md).

## See Also

### Customizing appearance
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](./titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](../nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/allowsfullheightlayout)*