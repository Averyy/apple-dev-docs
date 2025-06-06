# init(displayName:userInfo:volumeURL:)

**Framework**: File Provider  
**Kind**: init

Creates a new file provider domain with the specified URL and display name.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(displayName: String, userInfo: [AnyHashable : Any] = [:], volumeURL: URL?)
```

## See Also

- [init(identifier: NSFileProviderDomainIdentifier, displayName: String, pathRelativeToDocumentStorage: String)](nsfileproviderdomain/init(identifier:displayname:pathrelativetodocumentstorage:).md)
  Returns a newly instantiated domain.
- [init(identifier: NSFileProviderDomainIdentifier, displayName: String)](nsfileproviderdomain/init(identifier:displayname:).md)
  Creates a new file provider domain with the specified identifier and display name.
- [struct NSFileProviderDomainIdentifier](nsfileproviderdomainidentifier.md)
  A unique identifier for a file provider’s domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/init(displayname:userinfo:volumeurl:))*