# isDefault

**Framework**: CFNetwork  
**Kind**: property  
**Role**: Type Property

Specifies whether the resulting domain is the default registration or browse domain.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var isDefault: CFNetServiceBrowserFlags { get }
```

```c
kCFNetServiceFlagIsDefault
```

#### Discussion

If set, the resulting domain is the default registration or browse domain, depending on the context. For this version of the CFNetServices API, the default registration domain is the local domain.

> **Note**:  In previous versions of this API, this constant was `kCFNetServiceFlagIsRegistrationDomain`, which is retained for backward compatibility.

## See Also

### Type Properties
- [static var isDomain: CFNetServiceBrowserFlags](./isdomain.md)
  Specifies whether the result pertains to a search for domains or services.
- [static var isRegistrationDomain: CFNetServiceBrowserFlags](./isregistrationdomain.md)
- [static var moreComing: CFNetServiceBrowserFlags](./morecoming.md)
  A hint that the system will call the client’s callback function again soon.
- [static var remove: CFNetServiceBrowserFlags](./remove.md)
  Specifies whether the client should remove the result instead of adding it.
- [static var isRegistrationDomain: CFNetServiceBrowserFlags](./isregistrationdomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/isdefault)*