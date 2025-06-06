# addressRequired

**Framework**: System  
**Kind**: property

Destination address required.

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
static var addressRequired: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A required address was omitted from a socket operation.

The corresponding C error is `EDESTADDRREQ`.

## See Also

- [static var addressFamilyNotSupported: Errno](errno/addressfamilynotsupported.md)
  The address family isn’t supported by the protocol family.
- [static var addressInUse: Errno](errno/addressinuse.md)
  Address already in use.
- [static var addressNotAvailable: Errno](errno/addressnotavailable.md)
  Can’t assign the requested address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/addressrequired)*