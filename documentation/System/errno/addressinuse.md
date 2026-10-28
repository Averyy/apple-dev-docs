# addressInUse

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Address already in use.

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
static var addressInUse: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

Only one use of each address is normally permitted.

The corresponding C error is `EADDRINUSE`.

## See Also

### Network Address Errors
- [static var addressFamilyNotSupported: Errno](./addressfamilynotsupported.md)
  The address family isn’t supported by the protocol family.
- [static var addressNotAvailable: Errno](./addressnotavailable.md)
  Can’t assign the requested address.
- [static var addressRequired: Errno](./addressrequired.md)
  Destination address required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/addressinuse)*