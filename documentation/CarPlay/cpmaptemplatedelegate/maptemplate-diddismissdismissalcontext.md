# mapTemplate(_:didDismiss:dismissalContext:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the system dismissed the navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didDismiss navigationAlert: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)
```

## Parameters

- `mapTemplate`: The current map template.
- `navigationAlert`: The dismissed navigation alert.
- `dismissalContext`: The reason for dismissing the navigation alert.

## See Also

- [func mapTemplate(CPMapTemplate, willShow: CPNavigationAlert)](cpmaptemplatedelegate/maptemplate(_:willshow:).md)
  Tells the delegate that the system will show the navigation alert.
- [func mapTemplate(CPMapTemplate, didShow: CPNavigationAlert)](cpmaptemplatedelegate/maptemplate(_:didshow:).md)
  Tells the delegate that the system showed the navigation alert.
- [func mapTemplate(CPMapTemplate, willDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](cpmaptemplatedelegate/maptemplate(_:willdismiss:dismissalcontext:).md)
  Tells the delegate that the system is preparing to dismiss the navigation alert.
- [CPNavigationAlert.DismissalContext](cpnavigationalert/dismissalcontext.md)
  A set of reasons for dismissing a navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:diddismiss:dismissalcontext:))*