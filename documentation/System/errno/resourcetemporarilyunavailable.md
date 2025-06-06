# resourceTemporarilyUnavailable

**Framework**: System  
**Kind**: property

Resource temporarily unavailable.

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
static var resourceTemporarilyUnavailable: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

This is a temporary condition; later calls to the same routine may complete normally. Make the same function call again later.

The corresponding C error is `EAGAIN`.

## See Also

- [static var alreadyInProcess: Errno](errno/alreadyinprocess.md)
  Operation already in progress.
- [static var badAddress: Errno](errno/badaddress.md)
  Bad address.
- [static var interrupted: Errno](errno/interrupted.md)
  Interrupted function call.
- [static var invalidArgument: Errno](errno/invalidargument.md)
  Invalid argument.
- [static var noFunction: Errno](errno/nofunction.md)
  Function not implemented.
- [static var nowInProgress: Errno](errno/nowinprogress.md)
  Operation now in progress.
- [static var resourceBusy: Errno](errno/resourcebusy.md)
  Resource busy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/resourcetemporarilyunavailable)*