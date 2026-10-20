# titlebarSeparatorStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of separator that the app displays between the title bar and content of a window.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var titlebarSeparatorStyle: NSTitlebarSeparatorStyle { get set }
```

```objc
@property NSTitlebarSeparatorStyle titlebarSeparatorStyle;
```

#### Discussion

To apply this value, you must associate the item’s view with its own title bar section. The default value is [`NSTitlebarSeparatorStyle.automatic`](../nstitlebarseparatorstyle/automatic.md). The containing window’s preference can override this preference.

## See Also

### Customizing appearance
- [var allowsFullHeightLayout: Bool](./allowsfullheightlayout.md)
  A Boolean value that indicates whether full-height sidebars appear in the window after you set a style mask.
- [enum NSTitlebarSeparatorStyle](../nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/titlebarseparatorstyle)*