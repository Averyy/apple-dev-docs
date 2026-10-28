# INListCarsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intent for retrieving a list of the user’s electric vehicles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INListCarsIntent
```

```objc
@interface INListCarsIntent : INIntent
```

## Overview

Maps creates instances of `INListCarsIntent` when it needs to display a list of the user’s electric vehicles, usually before or during route planning.

To handle this intent, you create an object that conforms to the [`INListCarsIntentHandling`](./inlistcarsintenthandling.md) protocol. The object handles, and optionally confirms, the request by providing an instance of [`INListCarsIntentResponse`](./inlistcarsintentresponse.md). The response contains an array of [`INCar`](./incar.md) objects, one for each of the user’s electric vehicles. Maps requires that each vehicle responds to [`INGetCarPowerLevelStatusIntent`](./ingetcarpowerlevelstatusintent.md) requests so that it can use the information the intent provides—current charge, battery capacity, distance remaining, and so forth—to more accurately plan the route.

## Topics

### Creating an Intent
- [init()](./inlistcarsintent/init%28%29.md)
  Creates an intent that represents a request for a list of the user’s electric vehicles.

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

### List Cars
- [protocol INListCarsIntentHandling](./inlistcarsintenthandling.md)
  The handler interface for requesting a list of the user’s electric vehicles.
- [class INListCarsIntentResponse](./inlistcarsintentresponse.md)
  Your app’s response to a request to list the user’s electric vehicles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintent)*