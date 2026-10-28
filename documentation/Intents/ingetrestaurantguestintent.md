# INGetRestaurantGuestIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for information about the guest who is making reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INGetRestaurantGuestIntent
```

```objc
@interface INGetRestaurantGuestIntent : INIntent
```

## Overview

An [`INGetRestaurantGuestIntent`](./ingetrestaurantguestintent.md) object is a request for information about the person whose name should appear on reservations. Maps sends this intent to your Intents extension when it wants information about the person making reservations. Your response contains the identity of the person making the reservation. The response can also contain information about whether your service allows the user to modify the identity of the guest. For example, you can specify whether your service allows one user to book reservations on behalf of another user.

To handle this intent, the handler object in your Intents extension must adopt the [`INGetRestaurantGuestIntentHandling`](./ingetrestaurantguestintenthandling.md) protocol. Your handler should create an [`INGetRestaurantGuestIntentResponse`](./ingetrestaurantguestintentresponse.md) object with information about the guest and your app’s preferences for modifying that guest’s identity.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Maps |
| Always requires unlocked device | Yes |

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

### Get Restaurant Guest
- [protocol INGetRestaurantGuestIntentHandling](./ingetrestaurantguestintenthandling.md)
  The handler interface for fetching information about the person making a reservation.
- [class INGetRestaurantGuestIntentResponse](./ingetrestaurantguestintentresponse.md)
  Your app’s response to a get restaurant guest intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetrestaurantguestintent)*