# badAddress

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Bad address.

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
static var badAddress: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

An address passed as an argument to a system call was invalid.

The corresponding C error is `EFAULT`.

## See Also

### System Call Errors
- [static var alreadyInProcess: Errno](./alreadyinprocess.md)
  Operation already in progress.
- [static var interrupted: Errno](./interrupted.md)
  Interrupted function call.
- [static var invalidArgument: Errno](./invalidargument.md)
  Invalid argument.
- [static var noFunction: Errno](./nofunction.md)
  Function not implemented.
- [static var nowInProgress: Errno](./nowinprogress.md)
  Operation now in progress.
- [static var resourceBusy: Errno](./resourcebusy.md)
  Resource busy.
- [static var resourceTemporarilyUnavailable: Errno](./resourcetemporarilyunavailable.md)
  Resource temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/badaddress)*