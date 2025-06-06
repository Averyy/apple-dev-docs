# noChildProcess

**Framework**: System  
**Kind**: property

No child processes.

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
static var noChildProcess: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A `wait(2)` or `waitpid(2)` function was executed by a process that dosn’t have any existing child processes or whose child processes are all already being waited for.

The corresponding C error is `ECHILD`.

## See Also

- [static var argListTooLong: Errno](errno/arglisttoolong.md)
  The argument list is too long.
- [static var identifierRemoved: Errno](errno/identifierremoved.md)
  Identifier removed.
- [static var noSuchProcess: Errno](errno/nosuchprocess.md)
  No such process.
- [static var previousOwnerDied: Errno](errno/previousownerdied.md)
  Previous pthread mutex owner died.
- [static var tooManyProcesses: Errno](errno/toomanyprocesses.md)
  Too many processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nochildprocess)*