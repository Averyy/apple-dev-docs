# noFunction

**Framework**: System  
**Kind**: property

Function not implemented.

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
static var noFunction: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

You attempted a system call that isn’t available on this system.

The corresponding C error is `ENOSYS`.

## See Also

- [static var alreadyInProcess: Errno](errno/alreadyinprocess.md)
  Operation already in progress.
- [static var badAddress: Errno](errno/badaddress.md)
  Bad address.
- [static var interrupted: Errno](errno/interrupted.md)
  Interrupted function call.
- [static var invalidArgument: Errno](errno/invalidargument.md)
  Invalid argument.
- [static var nowInProgress: Errno](errno/nowinprogress.md)
  Operation now in progress.
- [static var resourceBusy: Errno](errno/resourcebusy.md)
  Resource busy.
- [static var resourceTemporarilyUnavailable: Errno](errno/resourcetemporarilyunavailable.md)
  Resource temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nofunction)*