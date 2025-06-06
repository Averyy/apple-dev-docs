# init(identifier:displayName:pathRelativeToDocumentStorage:)

**Framework**: File Provider  
**Kind**: init

Returns a newly instantiated domain.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(identifier: NSFileProviderDomainIdentifier, displayName: String, pathRelativeToDocumentStorage: String)
```

## Parameters

- `identifier`: A string that identifies the domain. The file provider extension can select any string to uniquely identify the domain, as long as it doesn’t contain the colon (:) or slash (/) symbols.
- `displayName`: The name for the domain that the system shows to the user.
- `pathRelativeToDocumentStorage`: A path relative to the file provider extension’s   that the system uses to store the domain’s content.

## See Also

- [init(identifier: NSFileProviderDomainIdentifier, displayName: String)](nsfileproviderdomain/init(identifier:displayname:).md)
  Creates a new file provider domain with the specified identifier and display name.
- [struct NSFileProviderDomainIdentifier](nsfileproviderdomainidentifier.md)
  A unique identifier for a file provider’s domain.
- [init(displayName: String, userInfo: [AnyHashable : Any], volumeURL: URL?)](nsfileproviderdomain/init(displayname:userinfo:volumeurl:).md)
  Creates a new file provider domain with the specified URL and display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/init(identifier:displayname:pathrelativetodocumentstorage:))*