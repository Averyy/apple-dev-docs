# UIViewControllerBasedStatusBarAppearance

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the system bases the appearance of the status bar on the style preferred by the current view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+

#### Discussion

If this key is `YES`, the system uses the current view controller’s preferred status bar style. If this key is `NO`, it uses the status bar style of the [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) object. The default value is `YES`.

## See Also

- [UIStatusBarHidden](information-property-list/uistatusbarhidden.md)
  A Boolean value that indicates whether the system initially hides the status bar when the app launches.
- [UIStatusBarStyle](information-property-list/uistatusbarstyle.md)
  The style of the status bar as the app launches.
- [UIStatusBarTintParameters](information-property-list/uistatusbartintparameters.md)
  The status bar tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiviewcontrollerbasedstatusbarappearance)*