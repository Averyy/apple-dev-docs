# notPermitted

**Framework**: System  
**Kind**: property

Operation not permitted.

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
static var notPermitted: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

An attempt was made to perform an operation limited to processes with appropriate privileges or to the owner of a file or other resources.

The corresponding C error is `EPERM`.

## See Also

- [static var badMessage: Errno](errno/badmessage.md)
  Bad message.
- [static var canceled: Errno](errno/canceled.md)
  Operation canceled.
- [static var illegalByteSequence: Errno](errno/illegalbytesequence.md)
  Illegal byte sequence.
- [static var noData: Errno](errno/nodata.md)
  No message available.
- [static var noMessage: Errno](errno/nomessage.md)
  No message of desired type.
- [static var noSuchPolicy: Errno](errno/nosuchpolicy.md)
  No such policy registered.
- [static var notRecoverable: Errno](errno/notrecoverable.md)
  State not recoverable.
- [static var outputQueueFull: Errno](errno/outputqueuefull.md)
  Interface output queue is full.
- [static var tooManyReferences: Errno](errno/toomanyreferences.md)
  Too many references: can’t splice.
- [static var tooManyUsers: Errno](errno/toomanyusers.md)
  Too many users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/notpermitted)*