# previousOwnerDied

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Previous pthread mutex owner died.

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
static var previousOwnerDied: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

The corresponding C error is `EOWNERDEAD`.

## See Also

### Process Errors
- [static var argListTooLong: Errno](./arglisttoolong.md)
  The argument list is too long.
- [static var identifierRemoved: Errno](./identifierremoved.md)
  Identifier removed.
- [static var noChildProcess: Errno](./nochildprocess.md)
  No child processes.
- [static var noSuchProcess: Errno](./nosuchprocess.md)
  No such process.
- [static var tooManyProcesses: Errno](./toomanyprocesses.md)
  Too many processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/previousownerdied)*