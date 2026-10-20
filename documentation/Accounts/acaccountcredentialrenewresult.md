# ACAccountCredentialRenewResult

**Framework**: Accounts  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum ACAccountCredentialRenewResult : NSInteger;
```

## Topics

### Constants
- [ACAccountCredentialRenewResult.renewed](./acaccountcredentialrenewresult/renewed.md)
  The account’s credentials have been renewed and are now associated with the account.
- [ACAccountCredentialRenewResult.rejected](./acaccountcredentialrenewresult/rejected.md)
  Renewal failed because the user revoked your access to their account.
- [ACAccountCredentialRenewResult.failed](./acaccountcredentialrenewresult/failed.md)
  A non-user-initiated cancel of the prompt.
### Initializers
- [init?(rawValue: Int)](./acaccountcredentialrenewresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Renewing Account Credentials
- [func renewCredentials(for: ACAccount!, completion: ((ACAccountCredentialRenewResult, (any Error)?) -> Void)!)](./acaccountstore/renewcredentials%28for,completion%29.md)
  Renews account credentials when the credentials are no longer valid.
- [typealias ACAccountStoreCredentialRenewalHandler](./acaccountstorecredentialrenewalhandler.md)
  Specifies a handler to call when credentials are renewed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult)*