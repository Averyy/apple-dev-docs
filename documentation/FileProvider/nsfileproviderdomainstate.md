# NSFileProviderDomainState

**Framework**: File Provider  
**Kind**: protocol

An object that contains global state data about the domain.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderDomainState : NSObjectProtocol
```

## Topics

### Accessing State Data
- [var domainVersion: NSFileProviderDomainVersion](nsfileproviderdomainstate/domainversion.md)
  An opaque object that uniquely identifies the domain’s version.
- [var userInfo: [AnyHashable : Any]](nsfileproviderdomainstate/userinfo.md)
  Global state information about the current domain version.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSFileProviderDomainVersion](nsfileproviderdomainversion.md)
  An opaque object that identifies a specific version of a domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomainstate)*