# resourceBusy

**Framework**: System  
**Kind**: property

Resource busy.

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
static var resourceBusy: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

You attempted to use a system resource which was in use at the time, in a manner that would have conflicted with the request.

The corresponding C error is `EBUSY`.

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
- [static var resourceTemporarilyUnavailable: Errno](errno/resourcetemporarilyunavailable.md)
  Resource temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/resourcebusy)*