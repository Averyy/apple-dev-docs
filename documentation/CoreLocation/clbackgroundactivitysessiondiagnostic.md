# CLBackgroundActivitySessionDiagnostic

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
@interface CLBackgroundActivitySessionDiagnostic : NSObject
```

## Topics

### Instance Properties
- [authorizationDenied](./clbackgroundactivitysessiondiagnostic/authorizationdenied.md)
- [authorizationDeniedGlobally](./clbackgroundactivitysessiondiagnostic/authorizationdeniedglobally.md)
- [authorizationRequestInProgress](./clbackgroundactivitysessiondiagnostic/authorizationrequestinprogress.md)
- [authorizationRestricted](./clbackgroundactivitysessiondiagnostic/authorizationrestricted.md)
- [insufficientlyInUse](./clbackgroundactivitysessiondiagnostic/insufficientlyinuse.md)
- [serviceSessionRequired](./clbackgroundactivitysessiondiagnostic/servicesessionrequired.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Location updates
- [Getting the current location of a device](./getting-the-current-location-of-a-device.md)
  Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](./handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](./creating-a-location-push-service-extension.md)
  Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.
- [class CLLocation](./cllocation.md)
  The latitude, longitude, and course information reported by the system.
- [struct CLLocationCoordinate2D](./cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [class CLFloor](./clfloor.md)
  The floor of a building on which the user’s device is located.
- [class CLVisit](./clvisit.md)
  Information about the user’s location during a specific period of time.
- [class CLLocationSourceInformation](./cllocationsourceinformation.md)
  Information about the source that provides a location.
- [CLServiceSession](./clservicesession-2ddhd.md)
- [CLServiceSessionDiagnostic](./clservicesessiondiagnostic.md)
- [CLLocationUpdater](./cllocationupdater.md)
  An object that provides device location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbackgroundactivitysessiondiagnostic)*