# NSFileProviderDomainIdentifier

**Framework**: File Provider  
**Kind**: struct

A unique identifier for a file provider’s domain.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderDomainIdentifier
```

## Topics

### Initializers
- [init(String)](nsfileproviderdomainidentifier/init(_:).md)
  Returns a newly initialized domain identifier.
- [init(rawValue: String)](nsfileproviderdomainidentifier/init(rawvalue:).md)
  Returns a newly initialized domain identifier.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(identifier: NSFileProviderDomainIdentifier, displayName: String, pathRelativeToDocumentStorage: String)](nsfileproviderdomain/init(identifier:displayname:pathrelativetodocumentstorage:).md)
  Returns a newly instantiated domain.
- [init(identifier: NSFileProviderDomainIdentifier, displayName: String)](nsfileproviderdomain/init(identifier:displayname:).md)
  Creates a new file provider domain with the specified identifier and display name.
- [init(displayName: String, userInfo: [AnyHashable : Any], volumeURL: URL?)](nsfileproviderdomain/init(displayname:userinfo:volumeurl:).md)
  Creates a new file provider domain with the specified URL and display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomainidentifier)*