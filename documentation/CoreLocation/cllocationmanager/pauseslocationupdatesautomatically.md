# pausesLocationUpdatesAutomatically

**Framework**: Core Location  
**Kind**: property

A Boolean value that indicates whether the location-manager object may pause location updates.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var pausesLocationUpdatesAutomatically: Bool { get set }
```

## Mentions

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)

#### Discussion

Allowing the location manager to pause updates can improve battery life on the target device without sacrificing location data. Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) causes the location manager to pause updates (and powers down the appropriate hardware) at times when the location data is unlikely to change. For example, if the user stops for food while using a navigation app, the location manager might pause updates for a period of time. You can help the determination of when to pause location updates by assigning a value to the [`activityType`](cllocationmanager/activitytype.md) property.

After a pause occurs, it’s your responsibility to restart location services again when you determine that they’re needed. Core Location calls the [`locationManagerDidPauseLocationUpdates(_:)`](cllocationmanagerdelegate/locationmanagerdidpauselocationupdates(_:).md) method of your location manager’s delegate to let you know that a pause has occurred. In that method configure a local notification that has a [`UNLocationNotificationTrigger`](https://developer.apple.com/documentation/UserNotifications/UNLocationNotificationTrigger) to notify when the user exits the current region. The message for the local notification should prompt the user to launch your app again so that it can resume updates.

> ❗ **Important**:  For apps that have in-use authorization, a pause to location updates ends access to location changes until the app launches again and is able to restart those updates. To prevent location updates from stopping entirely, consider disabling this property and changing location accuracy to [`kCLLocationAccuracyThreeKilometers`](kcllocationaccuracythreekilometers.md) when your app moves to the background. This allows your app to continue receiving location updates in a power-friendly manner.

On supported platforms the default value of this property is [`true`](https://developer.apple.com/documentation/swift/true); otherwise the default value is [`false`](https://developer.apple.com/documentation/swift/false) and is immutable.

## See Also

- [func startUpdatingLocation()](cllocationmanager/startupdatinglocation.md)
  Starts the generation of updates that report the user’s current location.
- [func stopUpdatingLocation()](cllocationmanager/stopupdatinglocation.md)
  Stops the generation of location updates.
- [func requestLocation()](cllocationmanager/requestlocation.md)
  Requests the one-time delivery of the user’s current location.
- [var allowsBackgroundLocationUpdates: Bool](cllocationmanager/allowsbackgroundlocationupdates.md)
  A Boolean value that indicates whether the app receives location updates when running in the background.
- [var showsBackgroundLocationIndicator: Bool](cllocationmanager/showsbackgroundlocationindicator.md)
  A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.
- [var activityType: CLActivityType](cllocationmanager/activitytype.md)
  The type of activity the app expects the user to typically perform while in the app’s location session.
- [enum CLActivityType](clactivitytype.md)
  Constants that indicate the type of activity associated with location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/pauseslocationupdatesautomatically)*