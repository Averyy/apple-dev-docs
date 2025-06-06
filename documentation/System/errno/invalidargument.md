# invalidArgument

**Framework**: System  
**Kind**: property

Invalid argument.

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
static var invalidArgument: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

One or more of the specified arguments wasn’t valid; for example, specifying an undefined signal to a signal or kill function.

The corresponding C error is `EINVAL`.

## See Also

- [static var alreadyInProcess: Errno](errno/alreadyinprocess.md)
  Operation already in progress.
- [static var badAddress: Errno](errno/badaddress.md)
  Bad address.
- [static var interrupted: Errno](errno/interrupted.md)
  Interrupted function call.
- [static var noFunction: Errno](errno/nofunction.md)
  Function not implemented.
- [static var nowInProgress: Errno](errno/nowinprogress.md)
  Operation now in progress.
- [static var resourceBusy: Errno](errno/resourcebusy.md)
  Resource busy.
- [static var resourceTemporarilyUnavailable: Errno](errno/resourcetemporarilyunavailable.md)
  Resource temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/invalidargument)*