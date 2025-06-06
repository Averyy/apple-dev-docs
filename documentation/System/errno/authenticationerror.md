# authenticationError

**Framework**: System  
**Kind**: property

Authentication error.

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
static var authenticationError: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The authentication ticket used to mount an NFS file system was invalid.

The corresponding C error is `EAUTH`.

## See Also

- [static var needAuthenticator: Errno](errno/needauthenticator.md)
  Need authenticator.
- [static var staleNFSFileHandle: Errno](errno/stalenfsfilehandle.md)
  Stale NFS file handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/authenticationerror)*