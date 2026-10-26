# stopSendingUpdates(for:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Stops the delivery of regular power level updates for a particular electric vehicle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func stopSendingUpdates(for intent: INGetCarPowerLevelStatusIntent)
```

```objc
- (void) stopSendingUpdatesForGetCarPowerLevelStatus:(INGetCarPowerLevelStatusIntent *) intent;
```

#### Discussion

The system calls this method when it wants you to stop providing power level updates for a particular electric vehicle. Use this opportunity to perform any necessary cleanup and discard any references to the observer object that [`startSendingUpdates(for:to:)`](./startsendingupdates%28for,to%29.md) provides.

To determine which vehicle the request relates to, you can extract the vehicle’s unique indentifer from the `vocabularyIdentifier` property of the intent’s `carName` speakable string. This is the same value as the `carIdentifier` in the vehicle’s corresponding [`INCar`](../incar.md) object that your [`INListCarsIntentHandling`](../inlistcarsintenthandling.md) handler returns.

> ❗ **Important**:  An arbitrary thread of your Intents extension calls this method.

## Parameters

- `intent`: The intent object that indicates which electric vehicle the power level updates relate to. The [`vocabularyIdentifier`](../inspeakable/vocabularyidentifier.md) property of the [`carName`](../ingetcarpowerlevelstatusintent/carname.md) speakable string stores the unique [`carIdentifier`](../incar/caridentifier.md).

## See Also

### Providing Power Level Status Updates
- [func startSendingUpdates(for: INGetCarPowerLevelStatusIntent, to: any INGetCarPowerLevelStatusIntentResponseObserver)](./startsendingupdates%28for,to%29.md)
  Starts the delivery of regular power level updates for a particular electric vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintenthandling/stopsendingupdates(for:))*