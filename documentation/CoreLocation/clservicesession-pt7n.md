# CLServiceSession

**Framework**: Core Location  
**Kind**: class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
final class CLServiceSession
```

## Mentions

- [Handling location updates in the background](handling-location-updates-in-the-background.md)
- [Suspending authorization requests](suspending-authorization-requests.md)
- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md)

## Topics

### Classes
- [CLServiceSession.Diagnostics](clservicesession-pt7n/diagnostics-swift.class.md)
### Structures
- [CLServiceSession.Diagnostic](clservicesession-pt7n/diagnostic.md)
### Initializers
- [init(authorization: CLServiceSession.AuthorizationRequirement)](clservicesession-pt7n/init(authorization:).md)
- [init(authorization: CLServiceSession.AuthorizationRequirement, fullAccuracyPurposeKey: String)](clservicesession-pt7n/init(authorization:fullaccuracypurposekey:).md)
### Instance Properties
- [var diagnostics: CLServiceSession.Diagnostics](clservicesession-pt7n/diagnostics-swift.property.md)
### Instance Methods
- [func invalidate()](clservicesession-pt7n/invalidate.md)
### Enumerations
- [CLServiceSession.AuthorizationRequirement](clservicesession-pt7n/authorizationrequirement.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)
  Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md)
  Add and configure an extension to enable your location-sharing app to access a user’s location in response to a request from another user.
- [class CLVisit](clvisit.md)
  Information about the user’s location during a specific period of time.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clservicesession-pt7n)*