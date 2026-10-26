# kSCPropNetAirPortAuthPasswordEncryption

**Framework**: System Configuration  
**Kind**: var  
**Role**: Global Variable

The AirPort key `AuthPasswordEncryption`, whose value is of type `CFString`.

**Availability**:
- macOS 10.1+ - Deprecated in 10.9

## Declaration

```c
extern CFStringRef const kSCPropNetAirPortAuthPasswordEncryption;
```

#### Discussion

This key can be passed the following constants:

- `kSCValNetAirPortAuthPasswordEncryptionKeychain`, which has the value `Keychain`

## See Also

### Constants
- [kSCPropNetAirPortAllowNetCreation](./kscpropnetairportallownetcreation-c.var.md)
  The AirPort key `AllowNetCreation`, whose value is of type `CFNumber` and is equal to `0` or `1`.
- [kSCPropNetAirPortAuthPassword](./kscpropnetairportauthpassword-c.var.md)
  The AirPort key `AuthPassword`, whose value is of type `CFData`.
- [kSCPropNetAirPortJoinMode](./kscpropnetairportjoinmode-c.var.md)
  The AirPort key `JoinMode`, whose value is of type `CFString`.
- [kSCPropNetAirPortPowerEnabled](./kscpropnetairportpowerenabled-c.var.md)
  The AirPort key `PowerEnabled`, whose value is of type `CFNumber` and is equal to `0` or `1`.
- [kSCPropNetAirPortPreferredNetwork](./kscpropnetairportpreferrednetwork-c.var.md)
  The AirPort key `PreferredNetwork`, whose value is of type `CFString`.
- [kSCPropNetAirPortSavePasswords](./kscpropnetairportsavepasswords-c.var.md)
  The AirPort key `SavePasswords`, whose value is of type `CFNumber` and is equal to `0` or `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetairportauthpasswordencryption-c.var)*