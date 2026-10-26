# INListRideOptionsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intent for getting the types of rides available from a ride-booking service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INListRideOptionsIntent
```

```objc
@interface INListRideOptionsIntent : INIntent
```

## Mentions

- [Generating a List of Ride Options](../SiriKit/generating-a-list-of-ride-options.md)

#### Overview

Maps creates an [`INListRideOptionsIntent`](./inlistrideoptionsintent.md) object when it needs to display the types of vehicles that your service offers. Use the information in this intent to identify the possible vehicles that you can provide to the user right now. The intent contains information about the user’s pickup and drop-off locations, which you can use to determine ride availability, pricing, and estimated pickup times. This intent object represents a request for information and is not a commitment from the user to book any of the specified rides.

To handle this intent, the handler object in your Intents extension must adopt the [`INListRideOptionsIntentHandling`](./inlistrideoptionsintenthandling.md) protocol. Your handler should resolve and confirm the request parameters and create an [`INListRideOptionsIntentResponse`](./inlistrideoptionsintentresponse.md) object with the list of options.

> **Note**:  When implementing ride-booking support, provide a GeoJSON file with the regions for which you are able to provide rides and upload that file as your app’s Routing App Coverage File in App Store Connect. When it needs to suggest apps capable of providing a ride, Maps uses your coverage information to determine whether it should suggest your app. If you do not provide a coverage file and your app is not installed on the user’s device, Maps does not suggest your app. For information about how to create and upload a Routing App Coverage File, see [iTunes Connect Developer Help](https://help.apple.com/itunes-connect/developer/#/dev4ba662442).

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Maps |
| Always requires unlocked device | Yes |

## Topics

### Creating the Intent Object
- [init(pickupLocation: CLPlacemark?, dropOffLocation: CLPlacemark?)](./inlistrideoptionsintent/init%28pickuplocation,dropofflocation%29.md)
  Initializes the intent object with the specified pickup and drop-off locations.
### Getting the Pickup and Drop Off Locations
- [var pickupLocation: CLPlacemark?](./inlistrideoptionsintent/pickuplocation.md)
  The user’s starting location.
- [var dropOffLocation: CLPlacemark?](./inlistrideoptionsintent/dropofflocation.md)
  The user’s destination.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### List Ride Options
- [Generating a List of Ride Options](../SiriKit/generating-a-list-of-ride-options.md)
  Generate ride options for Maps to display to the user.
- [protocol INListRideOptionsIntentHandling](./inlistrideoptionsintenthandling.md)
  The handler interface for fetching the list of rides currently available from your ride-booking service.
- [class INListRideOptionsIntentResponse](./inlistrideoptionsintentresponse.md)
  Your app’s response to a list ride options intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintent)*