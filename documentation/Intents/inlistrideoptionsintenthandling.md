# INListRideOptionsIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for fetching the list of rides currently available from your ride-booking service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INListRideOptionsIntentHandling : NSObjectProtocol
```

```objc
@protocol INListRideOptionsIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INListRideOptionsIntentHandling`](./inlistrideoptionsintenthandling.md) protocol to resolve, confirm, and handle requests for information about the types of rides available from your service right now. Maps asks for this information when the user searches for a ride between the specified pickup and drop-off locations. Adopt this protocol in an object of your Intents extension that is capable of retrieving the ride information from your servers.

Ride options represent the categories of vehicles that your service offers and do not represent specific vehicles in your fleet. Each ride option contains information about the passenger capacity and pricing of the corresponding vehicles. You should also provide an estimated time at which one or more vehicles of that type could pick up the user.

Maps may deliver an [`INListRideOptionsIntent`](./inlistrideoptionsintent.md) object to your handler object at any time. Maps does not require you to resolve or confirm the contents of a list ride options intent before handling it. User interactions drive the selection of data in Maps, ensuring that the data Maps places into an intent object is already valid.

## Topics

### Resolving the Intent Parameters
- [func resolvePickupLocation(for: INListRideOptionsIntent, with: (INPlacemarkResolutionResult) -> Void)](./inlistrideoptionsintenthandling/resolvepickuplocation%28for,with%29.md)
  Resolves the user’s pickup location.
- [func resolveDropOffLocation(for: INListRideOptionsIntent, with: (INPlacemarkResolutionResult) -> Void)](./inlistrideoptionsintenthandling/resolvedropofflocation%28for,with%29.md)
  Resolves the user’s drop-off location.
### Confirming the Response
- [func confirm(intent: INListRideOptionsIntent, completion: (INListRideOptionsIntentResponse) -> Void)](./inlistrideoptionsintenthandling/confirm%28intent,completion%29.md)
  Confirms that you can provide the list of ride options.
### Handling the Intent
- [func handle(intent: INListRideOptionsIntent, completion: (INListRideOptionsIntentResponse) -> Void)](./inlistrideoptionsintenthandling/handle%28intent,completion%29.md)
  Handles providing the list of ride options.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INRidesharingDomainHandling](./inridesharingdomainhandling.md)

## See Also

### List Ride Options
- [Generating a List of Ride Options](../SiriKit/generating-a-list-of-ride-options.md)
  Generate ride options for Maps to display to the user.
- [class INListRideOptionsIntent](./inlistrideoptionsintent.md)
  An intent for getting the types of rides available from a ride-booking service.
- [class INListRideOptionsIntentResponse](./inlistrideoptionsintentresponse.md)
  Your app’s response to a list ride options intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintenthandling)*