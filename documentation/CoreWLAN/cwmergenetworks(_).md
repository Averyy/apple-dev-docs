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

#### Discussion

Duplicate networks are defined as networks with the same SSID, security type, and BSS type. When duplicates are found, the network with the best RSSI value will remain.

## Parameters

- `networks`: The set of networks to merge.

## See Also

### Utility Methods
- [func CWKeychainCopyEAPIdentityList(UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus](./cwkeychaincopyeapidentitylist%28_%29.md)
  Finds and returns the available identities stored in the keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwmergenetworks(_:))*