# protocolWrongTypeForSocket

**Framework**: System  
**Kind**: property

Protocol wrong for socket type.

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
static var protocolWrongTypeForSocket: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A protocol was specified that doesn’t support the semantics of the socket type requested. For example, you can’t use the ARPA Internet UDP protocol with type `SOCK_STREAM`.

The corresponding C error is `EPROTOTYPE`.

## See Also

- [static var protocolError: Errno](errno/protocolerror.md)
  Protocol error.
- [static var protocolFamilyNotSupported: Errno](errno/protocolfamilynotsupported.md)
  Protocol family not supported.
- [static var protocolNotAvailable: Errno](errno/protocolnotavailable.md)
  Protocol not available.
- [static var protocolNotSupported: Errno](errno/protocolnotsupported.md)
  Protocol not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/protocolwrongtypeforsocket)*