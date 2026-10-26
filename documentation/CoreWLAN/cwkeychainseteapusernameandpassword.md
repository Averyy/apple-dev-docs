# CWKeychainSetEAPUsernameAndPassword

**Framework**: Core WLAN  
**Kind**: func  
**Role**: Function

Sets the keychain item containing the 802.1X username and password for the specified SSID.

**Availability**:
- macOS 10.7+ - Deprecated in 10.9

## Declaration

```c
OSStatus CWKeychainSetEAPUsernameAndPassword(CFDataRef ssidData, CFStringRef username, CFStringRef password);
```

#### Return Value

An OSStatus error code which will indicate whether or not a failure occurred during execution. *errSecSuccess* indicates no error occurred.

## Parameters

- `username`: The 802.1X username.
- `password`: The 802.1X password.

## See Also

### Utility Methods
- [CWKeychainCopyEAPIdentity](./cwkeychaincopyeapidentity.md)
  Finds and returns the identity stored for corresponding network with the specified SSID.
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
- [CWKeychainSetPassword](./cwkeychainsetpassword.md)
  Sets the network keychain password for the specified SSID.
- [func CWMergeNetworks(Set<CWNetwork>) -> Set<CWNetwork>](./cwmergenetworks%28_%29.md)
  Merges the specified set of CWNetwork objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwkeychainseteapusernameandpassword)*