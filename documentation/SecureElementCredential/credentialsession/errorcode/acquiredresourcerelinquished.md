# CredentialSession.ErrorCode.acquiredResourceRelinquished

**Framework**: SecureElementCredential  
**Kind**: case

The system relinquished an underlying shared resource, preventing the operation from completing.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case acquiredResourceRelinquished
```

#### Discussion

When the system throws this error, it also reverts the session state to [`CredentialSession.State.management`](credentialsession/state-swift.enum/management.md).

You can attempt your operation again after receiving this error.

## See Also

- [CredentialSession.ErrorCode.resourceUnavailable](credentialsession/errorcode/resourceunavailable.md)
  The requested resource is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/errorcode/acquiredresourcerelinquished)*