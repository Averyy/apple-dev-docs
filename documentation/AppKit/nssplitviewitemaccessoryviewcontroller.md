# NSSplitViewItemAccessoryViewController

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 26.0+

## Declaration

```swift
class NSSplitViewItemAccessoryViewController
```

```objc
@interface NSSplitViewItemAccessoryViewController : NSViewController
```

## Topics

### Configuring the scroll edge effect
- [var preferredScrollEdgeEffectStyle: NSScrollEdgeEffectStyle](./nssplitviewitemaccessoryviewcontroller/preferredscrolledgeeffectstyle.md)
  The split view item accessory’s preferred effect for content scrolling behind it.
- [class NSScrollEdgeEffectStyle](./nsscrolledgeeffectstyle.md)
  Styles for a scroll view’s edge effect.
### Instance Properties
- [var automaticallyAppliesContentInsets: Bool](./nssplitviewitemaccessoryviewcontroller/automaticallyappliescontentinsets.md)
  Whether or not standard content insets should be applied to the view. Defaults to YES.
- [var isHidden: Bool](./nssplitviewitemaccessoryviewcontroller/ishidden.md)
  When set, this property will collapse the accessory view to 0 height (animatable) but not remove it from the window. Set through the animator object to animate it.
### Instance Methods
- [func viewDidAppear()](./nssplitviewitemaccessoryviewcontroller/viewdidappear%28%29.md)
- [func viewDidDisappear()](./nssplitviewitemaccessoryviewcontroller/viewdiddisappear%28%29.md)
- [func viewWillAppear()](./nssplitviewitemaccessoryviewcontroller/viewwillappear%28%29.md)
- [func viewWillDisappear()](./nssplitviewitemaccessoryviewcontroller/viewwilldisappear%28%29.md)

## Relationships

### Inherits From
- [NSViewController](./nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](./nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](./nssegueperforming.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring accessory views
- [var topAlignedAccessoryViewControllers: [NSSplitViewItemAccessoryViewController]](./nssplitviewitem/topalignedaccessoryviewcontrollers.md)
  The following methods allow you to add accessory views to the top/bottom of this splitViewItem. See `NSSplitViewItemAccessoryViewController` for more details.
- [var bottomAlignedAccessoryViewControllers: [NSSplitViewItemAccessoryViewController]](./nssplitviewitem/bottomalignedaccessoryviewcontrollers.md)
- [func addTopAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController)](./nssplitviewitem/addtopalignedaccessoryviewcontroller%28_%29.md)
- [func insertTopAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController, at: Int)](./nssplitviewitem/inserttopalignedaccessoryviewcontroller%28_,at%29.md)
- [func removeTopAlignedAccessoryViewController(at: Int)](./nssplitviewitem/removetopalignedaccessoryviewcontroller%28at%29.md)
  NOTE: you can use this method, or `-removeFromParentViewController:`, whichever is easier.
- [func addBottomAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController)](./nssplitviewitem/addbottomalignedaccessoryviewcontroller%28_%29.md)
- [func insertBottomAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController, at: Int)](./nssplitviewitem/insertbottomalignedaccessoryviewcontroller%28_,at%29.md)
- [func removeBottomAlignedAccessoryViewController(at: Int)](./nssplitviewitem/removebottomalignedaccessoryviewcontroller%28at%29.md)
  NOTE: you can use this method, or `-removeFromParentViewController:`, whichever is easier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitemaccessoryviewcontroller)*