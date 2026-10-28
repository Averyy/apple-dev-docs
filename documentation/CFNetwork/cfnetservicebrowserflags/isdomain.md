# isDomain

**Framework**: CFNetwork  
**Kind**: property  
**Role**: Type Property

Specifies whether the result pertains to a search for domains or services.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var isDomain: CFNetServiceBrowserFlags { get }
```

```c
kCFNetServiceFlagIsDomain
```

## Discussion

If set, the results pertain to a search for domains. If not set, the results pertain to a search for services.

## See Also

### Type Properties
- [static var isDefault: CFNetServiceBrowserFlags](./isdefault.md)
  Specifies whether the resulting domain is the default registration or browse domain.
- [static var isRegistrationDomain: CFNetServiceBrowserFlags](./isregistrationdomain.md)
- [static var moreComing: CFNetServiceBrowserFlags](./morecoming.md)
  A hint that the system will call the client’s callback function again soon.
- [static var remove: CFNetServiceBrowserFlags](./remove.md)
  Specifies whether the client should remove the result instead of adding it.
- [static var isRegistrationDomain: CFNetServiceBrowserFlags](./isregistrationdomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/isdomain)*