# mapTemplate(_:didShow:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system showed the navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didShow navigationAlert: CPNavigationAlert)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didShowNavigationAlert:(CPNavigationAlert *) navigationAlert;
```

## Parameters

- `mapTemplate`: The current map template.
- `navigationAlert`: The navigation alert presented by the system.

## See Also

### Handling Navigation Alerts
- [func mapTemplate(CPMapTemplate, willShow: CPNavigationAlert)](./maptemplate%28_,willshow%29.md)
  Tells the delegate that the system will show the navigation alert.
- [func mapTemplate(CPMapTemplate, willDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](./maptemplate%28_,willdismiss,dismissalcontext%29.md)
  Tells the delegate that the system is preparing to dismiss the navigation alert.
- [func mapTemplate(CPMapTemplate, didDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](./maptemplate%28_,diddismiss,dismissalcontext%29.md)
  Tells the delegate that the system dismissed the navigation alert.
- [CPNavigationAlert.DismissalContext](../cpnavigationalert/dismissalcontext.md)
  A set of reasons for dismissing a navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didshow:))*