# argListTooLong

**Framework**: System  
**Kind**: property

The argument list is too long.

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
static var argListTooLong: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The number of bytes used for the argument and environment list of the new process exceeded the limit `NCARGS`, as defined in `<sys/param.h>`.

The corresponding C error is `E2BIG`.

## See Also

- [static var identifierRemoved: Errno](errno/identifierremoved.md)
  Identifier removed.
- [static var noChildProcess: Errno](errno/nochildprocess.md)
  No child processes.
- [static var noSuchProcess: Errno](errno/nosuchprocess.md)
  No such process.
- [static var previousOwnerDied: Errno](errno/previousownerdied.md)
  Previous pthread mutex owner died.
- [static var tooManyProcesses: Errno](errno/toomanyprocesses.md)
  Too many processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/arglisttoolong)*