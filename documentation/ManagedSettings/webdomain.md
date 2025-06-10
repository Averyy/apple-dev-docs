# WebDomain

**Framework**: ManagedSettings  
**Kind**: struct

An object that represents a website.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
struct WebDomain
```

## Topics

### Creating a Web Domain
- [init(domain: String)](webdomain/init(domain:).md)
  Creates an object that represents the specified web domain.
- [init(token: WebDomainToken)](webdomain/init(token:).md)
  Creates an object that represents the provided domain.
### Identifying a Web Domain
- [let domain: String?](webdomain/domain.md)
  A string that identifies a specific web domain.
- [let token: WebDomainToken?](webdomain/token.md)
  An opaque representation of a specific web domain.
### Comparing Web Domains
- [static func == (WebDomain, WebDomain) -> Bool](webdomain/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](webdomain/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
- [func hash(into: inout Hasher)](webdomain/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](webdomain/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](webdomain/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [typealias WebDomainToken](webdomaintoken.md)
  A representation of a web domain that preserves the user’s privacy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webdomain)*