# CWKeychainCopyEAPIdentityList(_:)

**Framework**: Core WLAN  
**Kind**: func  
**Role**: Function

Finds and returns the available identities stored in the keychain.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CWKeychainCopyEAPIdentityList(_ list: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus
```

```c
OSStatus CWKeychainCopyEAPIdentityList(CFArrayRef*list);
```

#### Return Value

An OSStatus error code which will indicate whether or not a failure occurred during execution. *errSecSuccess* indicates no error occurred.

#### Discussion

If there are no available identities, this method will return *nil*.

## See Also

### Utility Methods
- [func CWMergeNetworks(Set<CWNetwork>) -> Set<CWNetwork>](./cwmergenetworks%28_%29.md)
  Merges the specified set of CWNetwork objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwkeychaincopyeapidentitylist(_:))*