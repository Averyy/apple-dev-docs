# isOverviewVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating if the tab overview is currently displayed.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var isOverviewVisible: Bool { get set }
```

```objc
@property (getter=isOverviewVisible) BOOL overviewVisible;
```

## Discussion

The tab overview provides a visual overview of the windows that make up a tabbing group. This property indicates whether the tab overview is currently displayed. Setting the property either shows or hides the overview.

You can monitor this property for changes using key-value observing.

## See Also

### Related Documentation
- [func toggleTabOverview(Any?)](../nswindow/toggletaboverview%28_%29.md)
  Shows or hides the tab overview.
### Configuring the Tab User Interface
- [var isTabBarVisible: Bool](./istabbarvisible.md)
  A Boolean value indicating whether the tabbed window group currently displays a tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/isoverviewvisible)*