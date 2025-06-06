# staleNFSFileHandle

**Framework**: System  
**Kind**: property

Stale NFS file handle.

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
static var staleNFSFileHandle: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

You attempted access an open file on an NFS filesystem, which is now unavailable as referenced by the given file descriptor. This may indicate that the file was deleted on the NFS server or that some other catastrophic event occurred.

The corresponding C error is `ESTALE`.

## See Also

- [static var authenticationError: Errno](errno/authenticationerror.md)
  Authentication error.
- [static var needAuthenticator: Errno](errno/needauthenticator.md)
  Need authenticator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/stalenfsfilehandle)*