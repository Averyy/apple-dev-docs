# AudioAccessorySettingsTemporaryPairingObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes audio accessory temporary pairing behavior. The device enables temporary pairing when this key is present and the `Disabled` key isn’t `false`. The device doesn’t synchronize pairing information with iCloud when temporary pairing is active.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AudioAccessorySettingsTemporaryPairingObject
```

## Topics

### Objects
- [object AudioAccessorySettingsTemporaryPairing_ConfigurationObject](audioaccessorysettingstemporarypairing_configurationobject.md)
  A dictionary providing configuration for temporary pairing. Required if `Disabled` isn’t present or is `false`.

## Properties

- `Configuration` (AudioAccessorySettingsTemporaryPairing_ConfigurationObject): A dictionary providing configuration for temporary pairing. Required if `Disabled` isn’t present or is `false`.
- `Disabled` (boolean): If `true`, temporary pairing of audio accessories is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/audioaccessorysettingstemporarypairingobject)*