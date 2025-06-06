# CLBackgroundActivitySession

**Framework**: Core Location  
**Kind**: class

An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
final class CLBackgroundActivitySession
```

## Mentions

- [Handling location updates in the background](handling-location-updates-in-the-background.md)
- [Supporting live updates in SwiftUI and Mac Catalyst apps](supporting-live-updates-in-swiftui-and-mac-catalyst-apps.md)

#### Overview

Use `CLBackgroundActivitySession` to start a background activity session that allows a when-in-use authorized app to receive location updates or monitoring events.

## Topics

### Creating a background activity session
- [init()](clbackgroundactivitysession-3mzv3/init.md)
  Creates a new background activity session.
### Ending the session
- [func invalidate()](clbackgroundactivitysession-3mzv3/invalidate.md)
  Invalidates the background activity session.
### Classes
- [CLBackgroundActivitySession.Diagnostics](clbackgroundactivitysession-3mzv3/diagnostics-swift.class.md)
### Structures
- [CLBackgroundActivitySession.Diagnostic](clbackgroundactivitysession-3mzv3/diagnostic.md)
### Instance Properties
- [var diagnostics: CLBackgroundActivitySession.Diagnostics](clbackgroundactivitysession-3mzv3/diagnostics-swift.property.md)

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
- [struct CLLocationUpdate](cllocationupdate.md)
  A structure that contains the location information the framework delivers with each update.
- [Adopting live updates in Core Location](adopting-live-updates-in-core-location.md)
  Simplify location delivery using asynchronous events in Swift.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbackgroundactivitysession-3mzv3)*