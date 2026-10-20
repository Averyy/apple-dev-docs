# NSTabView.TabType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants specify the tab view’s type as used by the [`tabViewType`](./tabviewtype.md) property.

**Availability**:
- macOS

## Declaration

```swift
enum TabType
```

```c
enum NSTabViewType : NSUInteger;
```

## Topics

### Constants
- [NSTabView.TabType.topTabsBezelBorder](./tabtype/toptabsbezelborder.md)
  The view includes tabs on the top of the view and has a bezeled border (the default).
- [NSTabView.TabType.noTabsBezelBorder](./tabtype/notabsbezelborder.md)
  The view does not include tabs and has a bezeled border.
- [NSTabView.TabType.noTabsLineBorder](./tabtype/notabslineborder.md)
  The view does not include tabs and has a lined border.
- [NSTabView.TabType.noTabsNoBorder](./tabtype/notabsnoborder.md)
  The view does not include tabs and has no border.
- [NSTabView.TabType.bottomTabsBezelBorder](./tabtype/bottomtabsbezelborder.md)
  Tabs are on the bottom of the view with a bezeled border.
- [NSTabView.TabType.leftTabsBezelBorder](./tabtype/lefttabsbezelborder.md)
  Tabs are on the left of the view with a bezeled border.
- [NSTabView.TabType.rightTabsBezelBorder](./tabtype/righttabsbezelborder.md)
  Tabs are on the right of the view with a bezeled border.
### Initializers
- [init?(rawValue: UInt)](./tabtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the Tab Attributes
- [var tabViewType: NSTabView.TabType](./tabviewtype.md)
  The tab type to display the tabs.
- [var tabPosition: NSTabView.TabPosition](./tabposition-swift.property.md)
- [NSTabView.TabPosition](./tabposition-swift.enum.md)
- [var tabViewBorderType: NSTabView.TabViewBorderType](./tabviewbordertype-swift.property.md)
- [NSTabView.TabViewBorderType](./tabviewbordertype-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/tabtype)*