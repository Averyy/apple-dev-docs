# mapTemplate(_:willShow:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system will show the navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, willShow navigationAlert: CPNavigationAlert)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate willShowNavigationAlert:(CPNavigationAlert *) navigationAlert;
```

## Parameters

- `mapTemplate`: The current map template.
- `navigationAlert`: The navigation alert to display.

## See Also

### Handling navigation alerts
- [func mapTemplate(CPMapTemplate, shouldShowNotificationFor: CPNavigationAlert) -> Bool](./maptemplate%28_,shouldshownotificationfor%29-5lu8a.md)
  Asks the delegate whether the system should display the navigation alert as a notification when the app is in the background.
- [func mapTemplate(CPMapTemplate, didShow: CPNavigationAlert)](./maptemplate%28_,didshow%29.md)
  Tells the delegate that the system showed the navigation alert.
- [func mapTemplate(CPMapTemplate, willDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](./maptemplate%28_,willdismiss,dismissalcontext%29.md)
  Tells the delegate that the system is preparing to dismiss the navigation alert.
- [func mapTemplate(CPMapTemplate, didDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](./maptemplate%28_,diddismiss,dismissalcontext%29.md)
  Tells the delegate that the system dismissed the navigation alert.
- [CPNavigationAlert.DismissalContext](../cpnavigationalert/dismissalcontext.md)
  A set of reasons for dismissing a navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:willshow:))*