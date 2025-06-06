# isOverviewVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating if the tab overview is currently displayed.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var isOverviewVisible: Bool { get set }
```

#### Discussion

The tab overview provides a visual overview of the windows that make up a tabbing group. This property indicates whether the tab overview is currently displayed. Setting the property either shows or hides the overview.

You can monitor this property for changes using key-value observing.

## See Also

- [func toggleTabOverview(Any?)](nswindow/toggletaboverview(_:).md)
  Shows or hides the tab overview.
- [var isTabBarVisible: Bool](nswindowtabgroup/istabbarvisible.md)
  A Boolean value indicating whether the tabbed window group currently displays a tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/isoverviewvisible)*