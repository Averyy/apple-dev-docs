# tooManyProcesses

**Framework**: System  
**Kind**: property

Too many processes.

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
static var tooManyProcesses: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The corresponding C error is `EPROCLIM`.

## See Also

- [static var argListTooLong: Errno](errno/arglisttoolong.md)
  The argument list is too long.
- [static var identifierRemoved: Errno](errno/identifierremoved.md)
  Identifier removed.
- [static var noChildProcess: Errno](errno/nochildprocess.md)
  No child processes.
- [static var noSuchProcess: Errno](errno/nosuchprocess.md)
  No such process.
- [static var previousOwnerDied: Errno](errno/previousownerdied.md)
  Previous pthread mutex owner died.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/toomanyprocesses)*