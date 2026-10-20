# topAlignedAccessoryViewControllers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The following methods allow you to add accessory views to the top/bottom of this splitViewItem. See `NSSplitViewItemAccessoryViewController` for more details.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var topAlignedAccessoryViewControllers: [NSSplitViewItemAccessoryViewController] { get set }
```

```objc
@property (copy) NSArray<NSSplitViewItemAccessoryViewController *> * topAlignedAccessoryViewControllers;
```

## See Also

### Configuring accessory views
- [var bottomAlignedAccessoryViewControllers: [NSSplitViewItemAccessoryViewController]](./bottomalignedaccessoryviewcontrollers.md)
- [func addTopAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController)](./addtopalignedaccessoryviewcontroller%28_%29.md)
- [func insertTopAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController, at: Int)](./inserttopalignedaccessoryviewcontroller%28_,at%29.md)
- [func removeTopAlignedAccessoryViewController(at: Int)](./removetopalignedaccessoryviewcontroller%28at%29.md)
  NOTE: you can use this method, or `-removeFromParentViewController:`, whichever is easier.
- [func addBottomAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController)](./addbottomalignedaccessoryviewcontroller%28_%29.md)
- [func insertBottomAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController, at: Int)](./insertbottomalignedaccessoryviewcontroller%28_,at%29.md)
- [func removeBottomAlignedAccessoryViewController(at: Int)](./removebottomalignedaccessoryviewcontroller%28at%29.md)
  NOTE: you can use this method, or `-removeFromParentViewController:`, whichever is easier.
- [class NSSplitViewItemAccessoryViewController](../nssplitviewitemaccessoryviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/topalignedaccessoryviewcontrollers)*