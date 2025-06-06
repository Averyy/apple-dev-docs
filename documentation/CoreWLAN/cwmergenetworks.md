# CWMergeNetworks(_:)

**Framework**: Core WLAN  
**Kind**: func

Merges the specified set of CWNetwork objects.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CWMergeNetworks(_ networks: Set<CWNetwork>) -> Set<CWNetwork>
```

#### Discussion

Duplicate networks are defined as networks with the same SSID, security type, and BSS type. When duplicates are found, the network with the best RSSI value will remain.

## Parameters

- `networks`: The set of networks to merge.

## See Also

- [func CWKeychainCopyEAPIdentityList(UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus](cwkeychaincopyeapidentitylist(_:).md)
  Finds and returns the available identities stored in the keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwmergenetworks(_:))*