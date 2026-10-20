# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the tab view draws a background color when its type is `NSNoTabsNoBorder`.

**Availability**:
- macOS

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property BOOL drawsBackground;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the tab view draws a background color when the its type is `NSNoTabsNoBorder`, otherwise it does not. If the tab view has a bezeled border or a line border, the appropriate background for that border is used. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [var tabViewType: NSTabView.TabType](./tabviewtype.md)
  The tab type to display the tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/drawsbackground)*