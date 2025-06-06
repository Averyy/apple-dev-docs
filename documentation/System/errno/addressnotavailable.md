# addressNotAvailable

**Framework**: System  
**Kind**: property

Can’t assign the requested address.

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
static var addressNotAvailable: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

This error normally results from an attempt to create a socket with an address that isn’t on this machine.

The corresponding C error is `EADDRNOTAVAIL`.

## See Also

- [static var addressFamilyNotSupported: Errno](errno/addressfamilynotsupported.md)
  The address family isn’t supported by the protocol family.
- [static var addressInUse: Errno](errno/addressinuse.md)
  Address already in use.
- [static var addressRequired: Errno](errno/addressrequired.md)
  Destination address required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/addressnotavailable)*