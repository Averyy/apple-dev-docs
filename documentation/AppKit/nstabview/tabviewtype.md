# tabViewType

**Framework**: AppKit  
**Kind**: property

The tab type to display the tabs.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var tabViewType: NSTabView.TabType { get set }
```

#### Discussion

The supported values for this property are listed in [`NSTabView.TabType`](nstabview/tabtype.md). The default value of this property is [`NSTabView.TabType.topTabsBezelBorder`](nstabview/tabtype/toptabsbezelborder.md).

## See Also

- [NSTabView.TabType](nstabview/tabtype.md)
  These constants specify the tab view’s type as used by the [`tabViewType`](nstabview/tabviewtype.md) property.
- [var tabPosition: NSTabView.TabPosition](nstabview/tabposition-swift.property.md)
- [NSTabView.TabPosition](nstabview/tabposition-swift.enum.md)
- [var tabViewBorderType: NSTabView.TabViewBorderType](nstabview/tabviewbordertype-swift.property.md)
- [NSTabView.TabViewBorderType](nstabview/tabviewbordertype-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/tabviewtype)*