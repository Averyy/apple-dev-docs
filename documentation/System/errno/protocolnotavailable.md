# protocolNotAvailable

**Framework**: System  
**Kind**: property

Protocol not available.

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
static var protocolNotAvailable: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A bad option or level was specified in a `getsockopt(2)` or `setsockopt(2)` call.

The corresponding C error is `ENOPROTOOPT`.

## See Also

- [static var protocolError: Errno](errno/protocolerror.md)
  Protocol error.
- [static var protocolFamilyNotSupported: Errno](errno/protocolfamilynotsupported.md)
  Protocol family not supported.
- [static var protocolNotSupported: Errno](errno/protocolnotsupported.md)
  Protocol not supported.
- [static var protocolWrongTypeForSocket: Errno](errno/protocolwrongtypeforsocket.md)
  Protocol wrong for socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/protocolnotavailable)*