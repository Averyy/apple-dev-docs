# init(displayName:userInfo:volumeURL:)

**Framework**: File Provider  
**Kind**: init  
**Role**: Initializer

Creates a new file provider domain with the specified URL and display name.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(displayName: String, userInfo: [AnyHashable : Any] = [:], volumeURL: URL?)
```

```objc
- (instancetype) initWithDisplayName:(NSString *) displayName userInfo:(NSDictionary *) userInfo volumeURL:(NSURL *) volumeURL;
```

## See Also

### Creating domains
- [init(identifier: NSFileProviderDomainIdentifier, displayName: String, pathRelativeToDocumentStorage: String)](./init%28identifier,displayname,pathrelativetodocumentstorage%29.md)
  Returns a newly instantiated domain.
- [init(identifier: NSFileProviderDomainIdentifier, displayName: String)](./init%28identifier,displayname%29.md)
  Creates a new file provider domain with the specified identifier and display name.
- [struct NSFileProviderDomainIdentifier](../nsfileproviderdomainidentifier.md)
  A unique identifier for a file provider’s domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/init(displayname:userinfo:volumeurl:))*