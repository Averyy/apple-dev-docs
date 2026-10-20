# isRegistrationDomain

**Framework**: CFNetwork  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`isDefault`](./isdefault.md) instead.

## Declaration

```swift
static var isRegistrationDomain: CFNetServiceBrowserFlags { get }
```

```c
kCFNetServiceFlagIsRegistrationDomain
```

## See Also

### Type Properties
- [static var isDefault: CFNetServiceBrowserFlags](./isdefault.md)
  Specifies whether the resulting domain is the default registration or browse domain.
- [static var isDomain: CFNetServiceBrowserFlags](./isdomain.md)
  Specifies whether the result pertains to a search for domains or services.
- [static var moreComing: CFNetServiceBrowserFlags](./morecoming.md)
  A hint that the system will call the client’s callback function again soon.
- [static var remove: CFNetServiceBrowserFlags](./remove.md)
  Specifies whether the client should remove the result instead of adding it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/isregistrationdomain)*