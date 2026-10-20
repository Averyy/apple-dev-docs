# dictionaryRepresentation

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A dictionary of attributes that an installation service uses to configure a home.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var dictionaryRepresentation: [String : any Sendable] { get }
```

## See Also

### Identifying a provisional home
- [let hubPairingIdentity: HMHomeManager.PairingIdentity](./hubpairingidentity.md)
  Identity information that an installation service uses to set up a provisional home and pair devices.
- [let threadNetworkIdentifier: Data](./threadnetworkidentifier.md)
  The unique identifier for a Thread network that a home hub provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/provisionalconfiguration/dictionaryrepresentation)*