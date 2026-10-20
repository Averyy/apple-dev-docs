# mapTemplate(_:shouldUpdateNotificationFor:with:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the system should display the maneuver with updated travel estimates as a notification when the app is in the background.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, shouldUpdateNotificationFor maneuver: CPManeuver, with travelEstimates: CPTravelEstimates) -> Bool
```

```objc
- (BOOL) mapTemplate:(CPMapTemplate *) mapTemplate shouldUpdateNotificationForManeuver:(CPManeuver *) maneuver withTravelEstimates:(CPTravelEstimates *) travelEstimates;
```

#### Return Value

[`true`](../../Swift/true.md) if the system should display the maneuver as a notification; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `mapTemplate`: The current map template.
- `maneuver`: The current maneuver.
- `travelEstimates`: The updated travel estimates.

## See Also

### Displaying Notifications
- [func mapTemplate(CPMapTemplate, shouldShowNotificationFor: CPManeuver) -> Bool](./maptemplate%28_,shouldshownotificationfor%29-4mnm1.md)
  Asks the delegate whether the system should display the maneuver as a notification when the app is in the background.
- [func mapTemplate(CPMapTemplate, shouldShowNotificationFor: CPNavigationAlert) -> Bool](./maptemplate%28_,shouldshownotificationfor%29-5lu8a.md)
  Asks the delegate whether the system should display the navigation alert as a notification when the app is in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:shouldupdatenotificationfor:with:))*