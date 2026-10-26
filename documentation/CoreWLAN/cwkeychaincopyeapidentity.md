# CWKeychainCopyEAPIdentity

**Framework**: Core WLAN  
**Kind**: func  
**Role**: Function

Finds and returns the identity stored for corresponding network with the specified SSID.

**Availability**:
- macOS 10.7+ - Deprecated in 10.9

## Declaration

```c
OSStatus CWKeychainCopyEAPIdentity(CFDataRef ssidData, SecIdentityRef*identity);
```

#### Return Value

An OSStatus error code which will indicate whether or not a failure occurred during execution. *errSecSuccess* indicates no error occurred.

#### Discussion

If there is no matching keychain entry for the specified SSID, this method will return *NO*.

## Parameters

- `identity`: A SecIdentityRef object passed by reference, which contains the certificate to use for the specified SSID.

## See Also

### Utility Methods
- [func CWKeychainCopyEAPIdentityList(UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus](./cwkeychaincopyeapidentitylist%28_%29.md)
  Finds and returns the available identities stored in the keychain.
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
- [func CWMergeNetworks(Set<CWNetwork>) -> Set<CWNetwork>](./cwmergenetworks%28_%29.md)
  Merges the specified set of CWNetwork objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwkeychaincopyeapidentity)*