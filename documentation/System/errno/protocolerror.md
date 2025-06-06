# protocolError

**Framework**: System  
**Kind**: property

Protocol error.

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
static var protocolError: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

Some protocol error occurred. This error is device-specific, but generally isn’t related to a hardware failure.

The corresponding C error is `EPROTO`.

## See Also

- [static var protocolFamilyNotSupported: Errno](errno/protocolfamilynotsupported.md)
  Protocol family not supported.
- [static var protocolNotAvailable: Errno](errno/protocolnotavailable.md)
  Protocol not available.
- [static var protocolNotSupported: Errno](errno/protocolnotsupported.md)
  Protocol not supported.
- [static var protocolWrongTypeForSocket: Errno](errno/protocolwrongtypeforsocket.md)
  Protocol wrong for socket type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/protocolerror)*