# mapTemplate(_:shouldShowNotificationFor:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the system should display the navigation alert as a notification when the app is in the background.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, shouldShowNotificationFor navigationAlert: CPNavigationAlert) -> Bool
```

```objc
- (BOOL) mapTemplate:(CPMapTemplate *) mapTemplate shouldShowNotificationForNavigationAlert:(CPNavigationAlert *) navigationAlert;
```

## Return Value

[`true`](../../Swift/true.md) if the system should display the navigation alert as a notification; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `mapTemplate`: The current map template.
- `navigationAlert`: The navigation alert to display as a notification.

## See Also

### Handling navigation alerts
- [func mapTemplate(CPMapTemplate, willShow: CPNavigationAlert)](./maptemplate%28_,willshow%29.md)
  Tells the delegate that the system will show the navigation alert.
- [func mapTemplate(CPMapTemplate, didShow: CPNavigationAlert)](./maptemplate%28_,didshow%29.md)
  Tells the delegate that the system showed the navigation alert.
- [func mapTemplate(CPMapTemplate, willDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](./maptemplate%28_,willdismiss,dismissalcontext%29.md)
  Tells the delegate that the system is preparing to dismiss the navigation alert.
- [func mapTemplate(CPMapTemplate, didDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](./maptemplate%28_,diddismiss,dismissalcontext%29.md)
  Tells the delegate that the system dismissed the navigation alert.
- [CPNavigationAlert.DismissalContext](../cpnavigationalert/dismissalcontext.md)
  A set of reasons for dismissing a navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:shouldshownotificationfor:)-5lu8a)*