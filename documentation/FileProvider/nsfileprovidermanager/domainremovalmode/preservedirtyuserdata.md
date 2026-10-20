# NSFileProviderManager.DomainRemovalMode.preserveDirtyUserData

**Framework**: File Provider  
**Kind**: case  
**Role**: Case

Deletes the domain but keeps any items with unsynced, local changes.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case preserveDirtyUserData
```

```c
NSFileProviderDomainRemovalModePreserveDirtyUserData
```

## See Also

### Options
- [NSFileProviderManager.DomainRemovalMode.removeAll](./removeall.md)
  Deletes all items in the domain.
- [NSFileProviderManager.DomainRemovalMode.preserveDownloadedUserData](./preservedownloadeduserdata.md)
  Deletes the domain, but keeps the downloaded user data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/domainremovalmode/preservedirtyuserdata)*