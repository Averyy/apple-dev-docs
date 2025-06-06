# isTabBarVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the tabbed window group currently displays a tab bar.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var isTabBarVisible: Bool { get }
```

#### Discussion

Typically, a tabbed window displays a tab bar if there is more than one window in the tabbing group. The tab bar can also be manually toggled using the [`toggleTabBar(_:)`](nswindow/toggletabbar(_:).md) method.

## See Also

- [var isOverviewVisible: Bool](nswindowtabgroup/isoverviewvisible.md)
  A Boolean value indicating if the tab overview is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/istabbarvisible)*