# init(identifier:displayName:)

**Framework**: File Provider  
**Kind**: init

Creates a new file provider domain with the specified identifier and display name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(identifier: NSFileProviderDomainIdentifier, displayName: String)
```

## Parameters

- `identifier`: A string that identifies the domain. The file provider extension can select any string to uniquely identify the domain, as long as it doesn’t contain the colon (:) or slash (/) symbols.
- `displayName`: The name for the domain that the system shows to the user.

## See Also

- [init(identifier: NSFileProviderDomainIdentifier, displayName: String, pathRelativeToDocumentStorage: String)](nsfileproviderdomain/init(identifier:displayname:pathrelativetodocumentstorage:).md)
  Returns a newly instantiated domain.
- [struct NSFileProviderDomainIdentifier](nsfileproviderdomainidentifier.md)
  A unique identifier for a file provider’s domain.
- [init(displayName: String, userInfo: [AnyHashable : Any], volumeURL: URL?)](nsfileproviderdomain/init(displayname:userinfo:volumeurl:).md)
  Creates a new file provider domain with the specified URL and display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/init(identifier:displayname:))*