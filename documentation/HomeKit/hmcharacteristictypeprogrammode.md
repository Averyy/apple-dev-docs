# HMCharacteristicTypeProgramMode

**Framework**: HomeKit  
**Kind**: var

The current mode of the accessory’s scheduled programs.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 11.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
let HMCharacteristicTypeProgramMode: String
```

#### Discussion

The corresponding value is one of the constants in the [`HMCharacteristicValueProgramMode`](hmcharacteristicvalueprogrammode.md) enumeration.

> **Note**:  This characteristic type doesn’t add, modify, or delete the schedule itself. The user must set or modify the schedule through the accessory’s user interface, or using an app designed to communicate directly with the accessory (for example, using an API provided by the accessory’s manufacturer).

## Topics

### Values
- [enum HMCharacteristicValueProgramMode](hmcharacteristicvalueprogrammode.md)
  Possible values for scheduled programs.

## See Also

- [let HMCharacteristicTypeActive: String](hmcharacteristictypeactive.md)
  The current status of an accessory.
- [let HMCharacteristicTypeStatusTampered: String](hmcharacteristictypestatustampered.md)
  An indicator of whether an accessory has been tampered with.
- [let HMCharacteristicTypeStatusFault: String](hmcharacteristictypestatusfault.md)
  An indicator of whether the accessory has experienced a fault.
- [let HMCharacteristicTypeStatusActive: String](hmcharacteristictypestatusactive.md)
  An indicator of whether the service is working.
- [let HMCharacteristicTypeInUse: String](hmcharacteristictypeinuse.md)
  The current usage state of an accessory.
- [let HMCharacteristicTypeIsConfigured: String](hmcharacteristictypeisconfigured.md)
  The configuration state of an accessory.
- [let HMCharacteristicTypeRemainingDuration: String](hmcharacteristictyperemainingduration.md)
  The number of seconds remaining for the activity being carried out by the accessory.
- [let HMCharacteristicTypeSetDuration: String](hmcharacteristictypesetduration.md)
  The duration of the activity being carried out by the accessory.
- [let HMCharacteristicTypeWiFiSatelliteStatus: String](hmcharacteristictypewifisatellitestatus.md)
  The network status of the WiFi satellite accessory.
- [let HMCharacteristicTypeWANStatusList: String](hmcharacteristictypewanstatuslist.md)
  The WAN status list of an accessory.
- [let HMCharacteristicTypeTargetMediaState: String](hmcharacteristictypetargetmediastate.md)
  The target media state.
- [let HMCharacteristicTypeRouterStatus: String](hmcharacteristictyperouterstatus.md)
  The current status of the router.
- [let HMCharacteristicTypeCurrentMediaState: String](hmcharacteristictypecurrentmediastate.md)
  The current state of the media.
- [let HMCharacteristicTypeCurrentVisibilityState: String](hmcharacteristictypecurrentvisibilitystate.md)
  The current visibility state for a service.
- [let HMCharacteristicTypeTargetVisibilityState: String](hmcharacteristictypetargetvisibilitystate.md)
  The target visibility state for a service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypeprogrammode)*