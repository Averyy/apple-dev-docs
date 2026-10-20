# NSFileProviderDomainIdentifier

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

A unique identifier for a file provider’s domain.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderDomainIdentifier
```

```c
typedef NSString * NSFileProviderDomainIdentifier;
```

## Topics

### Initializers
- [init(String)](./nsfileproviderdomainidentifier/init%28_%29.md)
  Returns a newly initialized domain identifier.
- [init(rawValue: String)](./nsfileproviderdomainidentifier/init%28rawvalue%29.md)
  Returns a newly initialized domain identifier.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating domains
- [init(identifier: NSFileProviderDomainIdentifier, displayName: String, pathRelativeToDocumentStorage: String)](./nsfileproviderdomain/init%28identifier,displayname,pathrelativetodocumentstorage%29.md)
  Returns a newly instantiated domain.
- [init(identifier: NSFileProviderDomainIdentifier, displayName: String)](./nsfileproviderdomain/init%28identifier,displayname%29.md)
  Creates a new file provider domain with the specified identifier and display name.
- [init(displayName: String, userInfo: [AnyHashable : Any], volumeURL: URL?)](./nsfileproviderdomain/init%28displayname,userinfo,volumeurl%29.md)
  Creates a new file provider domain with the specified URL and display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomainidentifier)*