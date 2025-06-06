# noSuchProcess

**Framework**: System  
**Kind**: property

No such process.

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
static var noSuchProcess: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

There isn’t a process that corresponds to the specified process ID.

The corresponding C error is `ESRCH`.

## See Also

- [static var argListTooLong: Errno](errno/arglisttoolong.md)
  The argument list is too long.
- [static var identifierRemoved: Errno](errno/identifierremoved.md)
  Identifier removed.
- [static var noChildProcess: Errno](errno/nochildprocess.md)
  No child processes.
- [static var previousOwnerDied: Errno](errno/previousownerdied.md)
  Previous pthread mutex owner died.
- [static var tooManyProcesses: Errno](errno/toomanyprocesses.md)
  Too many processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nosuchprocess)*