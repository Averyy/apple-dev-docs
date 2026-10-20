# needAuthenticator

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Need authenticator.

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
static var needAuthenticator: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

Before mounting the given NFS file system, you must obtain an authentication ticket.

The corresponding C error is `ENEEDAUTH`.

## See Also

### NFS Errors
- [static var authenticationError: Errno](./authenticationerror.md)
  Authentication error.
- [static var staleNFSFileHandle: Errno](./stalenfsfilehandle.md)
  Stale NFS file handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/needauthenticator)*