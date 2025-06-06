# protocolNotSupported

**Framework**: System  
**Kind**: property

Protocol not supported.

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
static var protocolNotSupported: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The protocol hasn’t been configured into the system, or no implementation for it exists.

The corresponding C error is `EPROTONOSUPPORT`.

## See Also

- [static var protocolError: Errno](errno/protocolerror.md)
  Protocol error.
- [static var protocolFamilyNotSupported: Errno](errno/protocolfamilynotsupported.md)
  Protocol family not supported.
- [static var protocolNotAvailable: Errno](errno/protocolnotavailable.md)
  Protocol not available.
- [static var protocolWrongTypeForSocket: Errno](errno/protocolwrongtypeforsocket.md)
  Protocol wrong for socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/protocolnotsupported)*