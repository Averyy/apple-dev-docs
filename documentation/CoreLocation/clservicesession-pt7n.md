# CLServiceSession

**Framework**: Core Location  
**Kind**: class

An object that provides diagnostics about an app’s authorization to use location services.

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
- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md)
- [Suspending authorization requests](suspending-authorization-requests.md)

#### Discussion

A `CLServiceSession` object represents your app’s current goal for location authorization (for example [`CLServiceSession.AuthorizationRequirement.always`](CLServiceSession-pt7n/AuthorizationRequirement/always.md)), if any. Use a `CLServiceSession` object to declaratively tell Core Location what your app needs for authorization related to a specific workflow that your app provides.

The `CLServiceSession` object requests a person’s authorization to meet those requirements if possible, including automatically re-asking as needed after temporary authorization lapses due to time your app spends in the background.

You can create and hold different session objects to request different kinds of authorization for each workflow; each of these represents an *Explicit Service Session* relevant to that workflow. Each object provides diagnostics that your app can observe to understand how its authorization state may differ from the goal it expressed.

Don’t instantiate `CLServiceSession` objects directly; instead, create an instance that specifies a particular authorization mode, or authorization mode and accuracy requirements by using [`init(authorization:)`](CLServiceSession-pt7n/init(authorization:).md) or [`init(authorization:fullAccuracyPurposeKey:)`](CLServiceSession-pt7n/init(authorization:fullAccuracyPurposeKey:).md), respectively.

## Topics

### Creating a session
- [init(authorization: CLServiceSession.AuthorizationRequirement)](clservicesession-pt7n/init(authorization:).md)
  Creates a services session by using the authorization mode you specify.
- [init(authorization: CLServiceSession.AuthorizationRequirement, fullAccuracyPurposeKey: String)](clservicesession-pt7n/init(authorization:fullaccuracypurposekey:).md)
  Creates a services session by using the authorization mode and purpose key you specify.
- [CLServiceSession.AuthorizationRequirement](clservicesession-pt7n/authorizationrequirement.md)
  Values that describe when the service session needs to request authorization.
### Ending the session
- [func invalidate()](clservicesession-pt7n/invalidate.md)
  Invalidates the services session.
### Getting diagnostic information
- [var diagnostics: CLServiceSession.Diagnostics](clservicesession-pt7n/diagnostics-swift.property.md)
  A property that describes the current state of the services session.
- [CLServiceSession.Diagnostics](clservicesession-pt7n/diagnostics-swift.class.md)
  An object you use to access location service session diagnostic events.
### Structures
- [CLServiceSession.Diagnostic](clservicesession-pt7n/diagnostic.md)
  Values that describe the state of a core location services session.

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
  Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.
- [class CLLocation](cllocation.md)
  The latitude, longitude, and course information reported by the system.
- [struct CLLocationCoordinate2D](cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [class CLFloor](clfloor.md)
  The floor of a building on which the user’s device is located.
- [class CLVisit](clvisit.md)
  Information about the user’s location during a specific period of time.
- [class CLLocationSourceInformation](cllocationsourceinformation.md)
  Information about the source that provides a location.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clservicesession-pt7n)*