# addressFamilyNotSupported

**Framework**: System  
**Kind**: property

The address family isn’t supported by the protocol family.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var addressFamilyNotSupported: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

An address incompatible with the requested protocol was used. For example, you shouldn’t necessarily expect to be able to use name server addresses with ARPA Internet protocols.

The corresponding C error is `EAFNOSUPPORT`.

## See Also

- [static var addressInUse: Errno](errno/addressinuse.md)
  Address already in use.
- [static var addressNotAvailable: Errno](errno/addressnotavailable.md)
  Can’t assign the requested address.
- [static var addressRequired: Errno](errno/addressrequired.md)
  Destination address required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/addressfamilynotsupported)*