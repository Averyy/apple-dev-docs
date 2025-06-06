# ACAccountCredentialRenewResult

**Framework**: Accounts  
**Kind**: enum

Status codes of credential renewal requests.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
enum ACAccountCredentialRenewResult
```

## Topics

### Constants
- [ACAccountCredentialRenewResult.renewed](acaccountcredentialrenewresult/renewed.md)
  The account’s credentials have been renewed and are now associated with the account.
- [ACAccountCredentialRenewResult.rejected](acaccountcredentialrenewresult/rejected.md)
  Renewal failed because the user revoked your access to their account.
- [ACAccountCredentialRenewResult.failed](acaccountcredentialrenewresult/failed.md)
  A non-user-initiated cancel of the prompt.
### Initializers
- [init?(rawValue: Int)](acaccountcredentialrenewresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func renewCredentials(for: ACAccount!, completion: ACAccountStoreCredentialRenewalHandler!)](acaccountstore/renewcredentials(for:completion:).md)
  Renews account credentials when the credentials are no longer valid.
- [typealias ACAccountStoreCredentialRenewalHandler](acaccountstorecredentialrenewalhandler.md)
  Specifies a handler to call when credentials are renewed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult)*