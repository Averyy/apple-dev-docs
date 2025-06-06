# CLLocationUpdate

**Framework**: Core Location  
**Kind**: struct

A structure that contains the location information the framework delivers with each update.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct CLLocationUpdate
```

## Mentions

- [Handling location updates in the background](handling-location-updates-in-the-background.md)

#### Overview

You use `CLLocationUpate` events to observe changes in the device’s location, and to determine the activity type.

## Topics

### Determining movement and location
- [var isStationary: Bool](cllocationupdate/isstationary.md)
  A Boolean value that indicates whether the user is stationary.
- [var location: CLLocation?](cllocationupdate/location.md)
  The user’s location, if available.
### Receiving location updates
- [static func liveUpdates(CLLocationUpdate.LiveConfiguration) -> CLLocationUpdate.Updates](cllocationupdate/liveupdates(_:).md)
  Tells Core Location to start delivering the location updates it produces for the configuration you specify.
- [CLLocationUpdate.LiveConfiguration](cllocationupdate/liveconfiguration.md)
  Values for indicating the kind of updates the framework delivers.
- [CLLocationUpdate.Updates](cllocationupdate/updates.md)
  A structure that represents an asynchronous sequence of location updates.
### Instance Properties
- [var accuracyLimited: Bool](cllocationupdate/accuracylimited.md)
- [var authorizationDenied: Bool](cllocationupdate/authorizationdenied.md)
- [var authorizationDeniedGlobally: Bool](cllocationupdate/authorizationdeniedglobally.md)
- [var authorizationRequestInProgress: Bool](cllocationupdate/authorizationrequestinprogress.md)
- [var authorizationRestricted: Bool](cllocationupdate/authorizationrestricted.md)
- [var insufficientlyInUse: Bool](cllocationupdate/insufficientlyinuse.md)
- [var locationUnavailable: Bool](cllocationupdate/locationunavailable.md)
- [var serviceSessionRequired: Bool](cllocationupdate/servicesessionrequired.md)
- [var stationary: Bool](cllocationupdate/stationary.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md)
  Prepare your app to start collecting location data.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](supporting-live-updates-in-swiftui-and-mac-catalyst-apps.md)
  Enable background events by adding lifecycle event support.
- [class CLLocationManager](cllocationmanager.md)
  The object you use to start and stop the delivery of location-related events to your app.
- [class CLBackgroundActivitySession](clbackgroundactivitysession-3mzv3.md)
  An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.
- [Adopting live updates in Core Location](adopting-live-updates-in-core-location.md)
  Simplify location delivery using asynchronous events in Swift.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationupdate)*