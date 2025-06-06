# protocolFamilyNotSupported

**Framework**: System  
**Kind**: property

Protocol family not supported.

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
static var protocolFamilyNotSupported: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The protocol family hasn’t been configured into the system or no implementation for it exists.

The corresponding C error is `EPFNOSUPPORT`.

## See Also

- [static var protocolError: Errno](errno/protocolerror.md)
  Protocol error.
- [static var protocolNotAvailable: Errno](errno/protocolnotavailable.md)
  Protocol not available.
- [static var protocolNotSupported: Errno](errno/protocolnotsupported.md)
  Protocol not supported.
- [static var protocolWrongTypeForSocket: Errno](errno/protocolwrongtypeforsocket.md)
  Protocol wrong for socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/protocolfamilynotsupported)*