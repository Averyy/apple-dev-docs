# INListRideOptionsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a list ride options intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INListRideOptionsIntentResponse
```

```objc
@interface INListRideOptionsIntentResponse : INIntentResponse
```

## Overview

An [`INListRideOptionsIntentResponse`](./inlistrideoptionsintentresponse.md) object contains your app’s response to a request for ride options that your service offers. SiriKit can ask for a list of ride options at any time. When creating your response object, provide the types of vehicles you can offer in the [`rideOptions`](./inlistrideoptionsintentresponse/rideoptions.md) property. Each option provides information about a specific type of vehicle, including information about the pricing and passenger capacity of those vehicles. You can also provide information about accepted forms of payment and when the list of ride options expires.

When creating a response object with a code that involves launching the app, always provide a relevant [`NSUserActivity`](../Foundation/nsuseractivity.md) object. The activity object gets delivered to your parent app so that it has the context that it needs to handle the operation.

You create an [`INListRideOptionsIntentResponse`](./inlistrideoptionsintentresponse.md) object in the [`confirm(intent:completion:)`](./inlistrideoptionsintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inlistrideoptionsintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INListRideOptionsIntentHandling`](./inlistrideoptionsintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INListRideOptionsIntentResponseCode, userActivity: NSUserActivity?)](./inlistrideoptionsintentresponse/init%28code,useractivity%29.md)
  Initialize the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INListRideOptionsIntentResponseCode](./inlistrideoptionsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
### Accessing the Response Parameters
- [var rideOptions: [INRideOption]?](./inlistrideoptionsintentresponse/rideoptions.md)
  An array of ride options representing the services and prices that you are able to offer.
- [var expirationDate: Date?](./inlistrideoptionsintentresponse/expirationdate.md)
  The date after which the specified ride options are no longer valid.
- [var paymentMethods: [INPaymentMethod]?](./inlistrideoptionsintentresponse/paymentmethods.md)
  An array of payment methods supported by your service.
### Constants
- [enum INListRideOptionsIntentResponseCode](./inlistrideoptionsintentresponsecode.md)
  Constants indicating the state of the response.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
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
- [class INListRideOptionsIntent](./inlistrideoptionsintent.md)
  An intent for getting the types of rides available from a ride-booking service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintentresponse)*