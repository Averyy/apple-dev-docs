# CWMergeNetworks(_:)

**Framework**: Core WLAN  
**Kind**: func  
**Role**: Function

Merges the specified set of CWNetwork objects.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CWMergeNetworks(_ networks: Set<CWNetwork>) -> Set<CWNetwork>
```

```c
NSSet<CWNetwork *> *CWMergeNetworks(NSSet<CWNetwork *> *networks);
```

## Discussion

Duplicate networks are defined as networks with the same SSID, security type, and BSS type. When duplicates are found, the network with the best RSSI value will remain.

## Parameters

- `networks`: The set of networks to merge.

## See Also

### Utility Methods
- [func CWKeychainCopyEAPIdentityList(UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus](./cwkeychaincopyeapidentitylist%28_%29.md)
  Finds and returns the available identities stored in the keychain.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwmergenetworks(_:))*