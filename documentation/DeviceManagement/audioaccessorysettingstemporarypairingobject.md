# AudioAccessorySettingsTemporaryPairingObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes audio accessory temporary pairing behavior. The device enables temporary pairing when this key is present and the `Disabled` key isn’t `false`. The device doesn’t synchronize pairing information with iCloud when temporary pairing is active.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
object AudioAccessorySettingsTemporaryPairingObject
```

## Topics

### Objects
- [object AudioAccessorySettingsTemporaryPairing_ConfigurationObject](audioaccessorysettingstemporarypairing_configurationobject.md)
  A dictionary providing configuration for temporary pairing. Required if `Disabled` isn’t present or is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/audioaccessorysettingstemporarypairingobject)*