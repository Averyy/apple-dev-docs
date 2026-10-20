# SecTrustSettingsDomain

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The trust settings domains.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecTrustSettingsDomain
```

```c
enum SecTrustSettingsDomain : uint32_t;
```

## Topics

### Constants
- [SecTrustSettingsDomain.user](./sectrustsettingsdomain/user.md)
  Per-user trust settings.
- [SecTrustSettingsDomain.admin](./sectrustsettingsdomain/admin.md)
  Locally administered, system-wide trust settings.
- [SecTrustSettingsDomain.system](./sectrustsettingsdomain/system.md)
  System trust settings.
### Initializers
- [init?(rawValue: UInt32)](./sectrustsettingsdomain/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingsdomain)*