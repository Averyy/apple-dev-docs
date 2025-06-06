# rpcVersionMismatch

**Framework**: System  
**Kind**: property

The version of the remote procedure call (RPC) is incorrect.

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
static var rpcVersionMismatch: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The version of RPC on the remote peer isn’t compatible with the local version.

The corresponding C error is `ERPCMISMATCH`.

## See Also

- [static var rpcProcedureUnavailable: Errno](errno/rpcprocedureunavailable.md)
  Bad procedure for program.
- [static var rpcProgramUnavailable: Errno](errno/rpcprogramunavailable.md)
  The remote procedure call (RPC) program isn’t available.
- [static var rpcProgramVersionMismatch: Errno](errno/rpcprogramversionmismatch.md)
  The version of the remote procedure call (RPC) program is incorrect.
- [static var rpcUnsuccessful: Errno](errno/rpcunsuccessful.md)
  The structure of the remote procedure call (RPC) is bad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/rpcversionmismatch)*