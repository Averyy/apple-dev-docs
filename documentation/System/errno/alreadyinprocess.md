# alreadyInProcess

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Operation already in progress.

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
static var alreadyInProcess: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

You attempted an operation on a nonblocking object that already had an operation in progress.

The corresponding C error is `EALREADY`.

## See Also

### System Call Errors
- [static var badAddress: Errno](./badaddress.md)
  Bad address.
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

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/alreadyinprocess)*