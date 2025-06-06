# CWKeychainCopyEAPIdentityList(_:)

**Framework**: Core WLAN  
**Kind**: func

Finds and returns the available identities stored in the keychain.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CWKeychainCopyEAPIdentityList(_ list: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus
```

#### Return Value

An OSStatus error code which will indicate whether or not a failure occurred during execution.  indicates no error occurred.

#### Discussion

If there are no available identities, this method will return .

## See Also

- [func CWMergeNetworks(Set<CWNetwork>) -> Set<CWNetwork>](cwmergenetworks(_:).md)
  Merges the specified set of CWNetwork objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwkeychaincopyeapidentitylist(_:))*