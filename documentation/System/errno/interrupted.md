# interrupted

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Interrupted function call.

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
static var interrupted: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

The process caught an asynchronous signal (such as `SIGINT` or `SIGQUIT`) during the execution of an interruptible function. If the signal handler performs a normal return, the caller of the interrupted function call receives this error.

The corresponding C error is `EINTR`.

## See Also

### System Call Errors
- [static var alreadyInProcess: Errno](./alreadyinprocess.md)
  Operation already in progress.
- [static var badAddress: Errno](./badaddress.md)
  Bad address.
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

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/interrupted)*