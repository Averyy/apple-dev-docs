# WebDomain

**Framework**: Managed Settings  
**Kind**: struct

An object that represents a website.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct WebDomain
```

## Topics

### Creating a web domain
- [init(domain: String)](webdomain/init(domain:).md)
  Creates an object that represents the specified web domain.
- [init(token: WebDomainToken)](webdomain/init(token:).md)
  Creates an object that represents the provided domain.
### Identifying a web domain
- [let domain: String?](webdomain/domain.md)
  A string that identifies a specific web domain.
- [let token: WebDomainToken?](webdomain/token.md)
  An opaque representation of a specific web domain.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [typealias WebDomainToken](webdomaintoken.md)
  A representation of a web domain that preserves the user’s privacy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webdomain)*