# didUpdate(getCarPowerLevelStatus:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides information about the vehicle’s power level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func didUpdate(getCarPowerLevelStatus response: INGetCarPowerLevelStatusIntentResponse)
```

```objc
- (void) getCarPowerLevelStatusResponseDidUpdate:(INGetCarPowerLevelStatusIntentResponse *) response;
```

## Discussion

You call this method to deliver updated power level information to Maps, which only requests updates during an active navigation session. During that session, Maps regularly asks for the vehicle’s power level status using [`INGetCarPowerLevelStatusIntent`](../ingetcarpowerlevelstatusintent.md). Only call this method when there’s an abrupt change in the vehicle’s battery charge—a 3 percent or greater drop—since handling the last intent.

## Parameters

- `response`: The response object that contains current power level information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponseobserver/didupdate(getcarpowerlevelstatus:))*