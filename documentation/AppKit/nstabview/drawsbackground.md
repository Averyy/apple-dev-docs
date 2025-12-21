# drawsBackground

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the tab view draws a background color when its type is `NSNoTabsNoBorder`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the tab view draws a background color when the its type is `NSNoTabsNoBorder`, otherwise it does not. If the tab view has a bezeled border or a line border, the appropriate background for that border is used. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var tabViewType: NSTabView.TabType](nstabview/tabviewtype.md)
  The tab type to display the tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/drawsbackground)*