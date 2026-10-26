# INGetCarPowerLevelStatusIntentResponseObserver

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The interface for providing updates of a vehicle’s power level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol INGetCarPowerLevelStatusIntentResponseObserver : NSObjectProtocol
```

```objc
@protocol INGetCarPowerLevelStatusIntentResponseObserver <NSObject>
```

#### Overview

This protocol allows adopting objects to provide the system with an updated power level of a vehicle. You do not adopt this protocol in your own objects. Instead, the system provides an object that adopts this protocol, and you call its [`didUpdate(getCarPowerLevelStatus:)`](./ingetcarpowerlevelstatusintentresponseobserver/didupdate%28getcarpowerlevelstatus%29.md) method to provide the vehicle’s current power level.

When the system requests power level updates, it passes an object that conforms to this protocol to the [`startSendingUpdates(for:to:)`](./ingetcarpowerlevelstatusintenthandling/startsendingupdates%28for,to%29.md) method of your power level status handler—your custom object that adopts the [`INGetCarPowerLevelStatusIntentHandling`](./ingetcarpowerlevelstatusintenthandling.md) protocol. Your handler must store a reference to this object and use it to deliver regular updates about the power level.

## Topics

### Updating the Power Level Status
- [func didUpdate(getCarPowerLevelStatus: INGetCarPowerLevelStatusIntentResponse)](./ingetcarpowerlevelstatusintentresponseobserver/didupdate%28getcarpowerlevelstatus%29.md)
  Provides information about the vehicle’s power level.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Get Car Power Level Status
- [protocol INGetCarPowerLevelStatusIntentHandling](./ingetcarpowerlevelstatusintenthandling.md)
  The handler interface for requesting a car’s current power level.
- [class INGetCarPowerLevelStatusIntent](./ingetcarpowerlevelstatusintent.md)
  A request for the current power level of the user’s car.
- [class INGetCarPowerLevelStatusIntentResponse](./ingetcarpowerlevelstatusintentresponse.md)
  Your app’s response to a request for the vehicle power level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponseobserver)*