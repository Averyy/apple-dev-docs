# updateMotionState(_:forObjectWithToken:)

**Framework**: Nearby Interaction  
**Kind**: method

Notifies the session of an accessory’s motion state change.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func updateMotionState(_ motionState: NIMotionActivityState, forObjectWithToken token: NIDiscoveryToken)
```

#### Discussion

Ranging accuracy improves when the framework knows whether the accessory is moving. Track your accessory’s motion using a method you choose and then describe the motion with the appropriate [`NIMotionActivityState`](nimotionactivitystate.md). Call this method, providing the motion state, when the accessory’s motion state changes:

```swift
func handleMotionStateUpdate(_ state: NIMotionActivityState, session: NISession) {
    guard let config = session.configuration as? NINearbyAccessoryConfiguration else {
        return
    }
    session.updateMotionState(state, forObjectWithToken: config.accessoryDiscoveryToken)
}
```

This method works with [`NINearbyAccessoryConfiguration`](ninearbyaccessoryconfiguration.md) sessions, and applies to Ultra Wideband and Bluetooth Channel Sounding sessions.

## Parameters

- `motionState`: The current motion state of the accessory.
- `token`: The discovery token that identifies the nearby accessory.

## See Also

- [enum NIMotionActivityState](nimotionactivitystate.md)
  Motion states for a nearby accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/updatemotionstate(_:forobjectwithtoken:))*