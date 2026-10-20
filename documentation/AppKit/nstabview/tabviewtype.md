# tabViewType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tab type to display the tabs.

**Availability**:
- macOS

## Declaration

```swift
var tabViewType: NSTabView.TabType { get set }
```

```objc
@property NSTabViewType tabViewType;
```

#### Discussion

The supported values for this property are listed in [`NSTabView.TabType`](./tabtype.md). The default value of this property is [`NSTabView.TabType.topTabsBezelBorder`](./tabtype/toptabsbezelborder.md).

## See Also

### Configuring the Tab Attributes
- [NSTabView.TabType](./tabtype.md)
  These constants specify the tab view’s type as used by the [`tabViewType`](./tabviewtype.md) property.
- [var tabPosition: NSTabView.TabPosition](./tabposition-swift.property.md)
- [NSTabView.TabPosition](./tabposition-swift.enum.md)
- [var tabViewBorderType: NSTabView.TabViewBorderType](./tabviewbordertype-swift.property.md)
- [NSTabView.TabViewBorderType](./tabviewbordertype-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/tabviewtype)*