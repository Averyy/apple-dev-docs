# fileNameTooLong

**Framework**: System  
**Kind**: property

The file name is too long.

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
static var fileNameTooLong: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A component of a pathname exceeded 255 (`MAXNAMELEN`) characters, or an entire pathname exceeded 1023 (`MAXPATHLEN-1`) characters.

The corresponding C error is `ENAMETOOLONG`.

## See Also

- [static var tooManyRemoteLevels: Errno](errno/toomanyremotelevels.md)
  Too many levels of remote in path.
- [static var tooManySymbolicLinkLevels: Errno](errno/toomanysymboliclinklevels.md)
  Too many levels of symbolic links.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/filenametoolong)*