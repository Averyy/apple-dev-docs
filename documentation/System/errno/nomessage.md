# noMessage

**Framework**: System  
**Kind**: property  
**Role**: Type Property

No message of desired type.

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
static var noMessage: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

An IPC message queue doesn’t contain a message of the desired type, or a message catalog doesn’t contain the requested message.

The corresponding C error is `ENOMSG`.

## See Also

### General Errors
- [static var badMessage: Errno](./badmessage.md)
  Bad message.
- [static var canceled: Errno](./canceled.md)
  Operation canceled.
- [static var illegalByteSequence: Errno](./illegalbytesequence.md)
  Illegal byte sequence.
- [static var noData: Errno](./nodata.md)
  No message available.
- [static var noSuchPolicy: Errno](./nosuchpolicy.md)
  No such policy registered.
- [static var notPermitted: Errno](./notpermitted.md)
  Operation not permitted.
- [static var notRecoverable: Errno](./notrecoverable.md)
  State not recoverable.
- [static var outputQueueFull: Errno](./outputqueuefull.md)
  Interface output queue is full.
- [static var tooManyReferences: Errno](./toomanyreferences.md)
  Too many references: can’t splice.
- [static var tooManyUsers: Errno](./toomanyusers.md)
  Too many users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nomessage)*