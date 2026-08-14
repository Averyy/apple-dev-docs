# mapTemplate(_:shouldShowNotificationFor:)

**Framework**: CarPlay  
**Kind**: method

Asks the delegate whether the system should display the navigation alert as a notification when the app is in the background.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, shouldShowNotificationFor navigationAlert: CPNavigationAlert) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the system should display the navigation alert as a notification; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `mapTemplate`: The current map template.
- `navigationAlert`: The navigation alert to display as a notification.

## See Also

- [func mapTemplate(CPMapTemplate, shouldShowNotificationFor: CPManeuver) -> Bool](cpmaptemplatedelegate/maptemplate(_:shouldshownotificationfor:)-4mnm1.md)
  Asks the delegate whether the system should display the maneuver as a notification when the app is in the background.
- [func mapTemplate(CPMapTemplate, shouldUpdateNotificationFor: CPManeuver, with: CPTravelEstimates) -> Bool](cpmaptemplatedelegate/maptemplate(_:shouldupdatenotificationfor:with:).md)
  Asks the delegate whether the system should display the maneuver with updated travel estimates as a notification when the app is in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:shouldshownotificationfor:)-5lu8a)*