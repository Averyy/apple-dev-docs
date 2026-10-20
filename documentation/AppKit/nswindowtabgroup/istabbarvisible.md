# isTabBarVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the tabbed window group currently displays a tab bar.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var isTabBarVisible: Bool { get }
```

```objc
@property (readonly, getter=isTabBarVisible) BOOL tabBarVisible;
```

#### Discussion

Typically, a tabbed window displays a tab bar if there is more than one window in the tabbing group. The tab bar can also be manually toggled using the [`toggleTabBar(_:)`](../nswindow/toggletabbar%28_%29.md) method.

## See Also

### Configuring the Tab User Interface
- [var isOverviewVisible: Bool](./isoverviewvisible.md)
  A Boolean value indicating if the tab overview is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/istabbarvisible)*