# CoreWLANUtil.h

**Framework**: Core WLAN  
**Role**: API Collection

### Included Headers

- <Foundation/Foundation.h>

## Topics

### Utility Methods
- [func CWKeychainCopyEAPIdentityList(UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus](./cwkeychaincopyeapidentitylist%28_%29.md)
  Finds and returns the available identities stored in the keychain.
- [func CWMergeNetworks(Set<CWNetwork>) -> Set<CWNetwork>](./cwmergenetworks%28_%29.md)
  Merges the specified set of CWNetwork objects.
- [CWKeychainCopyEAPIdentity](./cwkeychaincopyeapidentity.md)
  Finds and returns the identity stored for corresponding network with the specified SSID.
- [CWKeychainCopyEAPUsernameAndPassword](./cwkeychaincopyeapusernameandpassword.md)
  Finds and returns the username and password stored for corresponding network with the specified SSID.
- [CWKeychainCopyPassword](./cwkeychaincopypassword.md)
  Finds and returns the keychain password stored for the corresponding network with the specified SSID.
- [CWKeychainDeleteEAPUsernameAndPassword](./cwkeychaindeleteeapusernameandpassword.md)
  Deletes the keychain item containing the 802.1X username and password for the specified SSID.
- [CWKeychainDeletePassword](./cwkeychaindeletepassword.md)
  Deletes the network password for the specified SSID from the default keychain.
- [CWKeychainSetEAPIdentity](./cwkeychainseteapidentity.md)
  Associates an exisiting identity item to the specified SSID.
- [CWKeychainSetEAPUsernameAndPassword](./cwkeychainseteapusernameandpassword.md)
  Sets the keychain item containing the 802.1X username and password for the specified SSID.
- [CWKeychainSetPassword](./cwkeychainsetpassword.md)
  Sets the network keychain password for the specified SSID.

## See Also

### Reference
- [CoreWLANConstants.h](./corewlanconstants-h.md)
- [CoreWLANTypes.h](./corewlantypes-h.md)
- [CoreWLAN Enumerations](./corewlan-enumerations.md)
- [CoreWLAN Functions](./corewlan-functions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/corewlanutil-h)*