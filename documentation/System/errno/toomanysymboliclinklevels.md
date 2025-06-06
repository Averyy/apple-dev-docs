# tooManySymbolicLinkLevels

**Framework**: System  
**Kind**: property

Too many levels of symbolic links.

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
static var tooManySymbolicLinkLevels: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A pathname lookup involved more than eight symbolic links.

The corresponding C error is `ELOOP`.

## See Also

- [static var fileNameTooLong: Errno](errno/filenametoolong.md)
  The file name is too long.
- [static var tooManyRemoteLevels: Errno](errno/toomanyremotelevels.md)
  Too many levels of remote in path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/toomanysymboliclinklevels)*