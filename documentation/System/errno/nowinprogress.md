# nowInProgress

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Operation now in progress.

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
static var nowInProgress: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

You attempted an operation that takes a long time to complete, such as `connect(2)` or `connectx(2)`, on a nonblocking object. See also `fcntl(2)`.

The corresponding C error is `EINPROGRESS`.

## See Also

### System Call Errors
- [static var alreadyInProcess: Errno](./alreadyinprocess.md)
  Operation already in progress.
- [static var badAddress: Errno](./badaddress.md)
  Bad address.
- [static var interrupted: Errno](./interrupted.md)
  Interrupted function call.
- [static var invalidArgument: Errno](./invalidargument.md)
  Invalid argument.
- [static var noFunction: Errno](./nofunction.md)
  Function not implemented.
- [static var resourceBusy: Errno](./resourcebusy.md)
  Resource busy.
- [static var resourceTemporarilyUnavailable: Errno](./resourcetemporarilyunavailable.md)
  Resource temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nowinprogress)*