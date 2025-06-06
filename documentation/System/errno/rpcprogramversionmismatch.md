# rpcProgramVersionMismatch

**Framework**: System  
**Kind**: property

The version of the remote procedure call (RPC) program is incorrect.

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
static var rpcProgramVersionMismatch: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The requested version of the program isn’t available on the remote host.

The corresponding C error is `EPROGMISMATCH`.

## See Also

- [static var rpcProcedureUnavailable: Errno](errno/rpcprocedureunavailable.md)
  Bad procedure for program.
- [static var rpcProgramUnavailable: Errno](errno/rpcprogramunavailable.md)
  The remote procedure call (RPC) program isn’t available.
- [static var rpcUnsuccessful: Errno](errno/rpcunsuccessful.md)
  The structure of the remote procedure call (RPC) is bad.
- [static var rpcVersionMismatch: Errno](errno/rpcversionmismatch.md)
  The version of the remote procedure call (RPC) is incorrect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/rpcprogramversionmismatch)*