# remove

**Framework**: CFNetwork  
**Kind**: property

Specifies whether the client should remove the result instead of adding it.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var remove: CFNetServiceBrowserFlags { get }
```

#### Discussion

If set, the client should remove the result item instead of adding it.

## See Also

- [static var isDefault: CFNetServiceBrowserFlags](cfnetservicebrowserflags/isdefault.md)
  Specifies whether the resulting domain is the default registration or browse domain.
- [static var isDomain: CFNetServiceBrowserFlags](cfnetservicebrowserflags/isdomain.md)
  Specifies whether the result pertains to a search for domains or services.
- [static var isRegistrationDomain: CFNetServiceBrowserFlags](cfnetservicebrowserflags/isregistrationdomain.md)
- [static var moreComing: CFNetServiceBrowserFlags](cfnetservicebrowserflags/morecoming.md)
  A hint that the system will call the client’s callback function again soon.
- [static var isRegistrationDomain: CFNetServiceBrowserFlags](cfnetservicebrowserflags/isregistrationdomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/remove)*