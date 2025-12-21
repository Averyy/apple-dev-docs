# NSSplitViewItemAccessoryViewController

**Framework**: AppKit  
**Kind**: class

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
class NSSplitViewItemAccessoryViewController
```

## Topics

### Configuring the scroll edge effect
- [var preferredScrollEdgeEffectStyle: NSScrollEdgeEffectStyle](nssplitviewitemaccessoryviewcontroller/preferredscrolledgeeffectstyle.md)
  The split view item accessory’s preferred effect for content scrolling behind it.
- [class NSScrollEdgeEffectStyle](nsscrolledgeeffectstyle.md)
  Styles for a scroll view’s edge effect.
### Instance Properties
- [var automaticallyAppliesContentInsets: Bool](nssplitviewitemaccessoryviewcontroller/automaticallyappliescontentinsets.md)
  Whether or not standard content insets should be applied to the view. Defaults to YES.
- [var isHidden: Bool](nssplitviewitemaccessoryviewcontroller/ishidden.md)
  When set, this property will collapse the accessory view to 0 height (animatable) but not remove it from the window. Set through the animator object to animate it.
### Instance Methods
- [func viewDidAppear()](nssplitviewitemaccessoryviewcontroller/viewdidappear.md)
- [func viewDidDisappear()](nssplitviewitemaccessoryviewcontroller/viewdiddisappear.md)
- [func viewWillAppear()](nssplitviewitemaccessoryviewcontroller/viewwillappear.md)
- [func viewWillDisappear()](nssplitviewitemaccessoryviewcontroller/viewwilldisappear.md)

## Relationships

### Inherits From
- [NSViewController](nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](nssegueperforming.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var topAlignedAccessoryViewControllers: [NSSplitViewItemAccessoryViewController]](nssplitviewitem/topalignedaccessoryviewcontrollers.md)
  The following methods allow you to add accessory views to the top/bottom of this splitViewItem. See `NSSplitViewItemAccessoryViewController` for more details.
- [var bottomAlignedAccessoryViewControllers: [NSSplitViewItemAccessoryViewController]](nssplitviewitem/bottomalignedaccessoryviewcontrollers.md)
- [func addTopAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController)](nssplitviewitem/addtopalignedaccessoryviewcontroller(_:).md)
- [func insertTopAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController, at: Int)](nssplitviewitem/inserttopalignedaccessoryviewcontroller(_:at:).md)
- [func removeTopAlignedAccessoryViewController(at: Int)](nssplitviewitem/removetopalignedaccessoryviewcontroller(at:).md)
  NOTE: you can use this method, or `-removeFromParentViewController:`, whichever is easier.
- [func addBottomAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController)](nssplitviewitem/addbottomalignedaccessoryviewcontroller(_:).md)
- [func insertBottomAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController, at: Int)](nssplitviewitem/insertbottomalignedaccessoryviewcontroller(_:at:).md)
- [func removeBottomAlignedAccessoryViewController(at: Int)](nssplitviewitem/removebottomalignedaccessoryviewcontroller(at:).md)
  NOTE: you can use this method, or `-removeFromParentViewController:`, whichever is easier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitemaccessoryviewcontroller)*