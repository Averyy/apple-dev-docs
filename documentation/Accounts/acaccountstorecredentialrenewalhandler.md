# ACAccountStoreCredentialRenewalHandler

**Framework**: Accounts  
**Kind**: typealias  
**Role**: Type Alias

Specifies a handler to call when credentials are renewed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
typealias ACAccountStoreCredentialRenewalHandler = (ACAccountCredentialRenewResult, (any Error)?) -> Void
```

```c
typedef void (^)(enum ACAccountCredentialRenewResult, NSError *) ACAccountStoreCredentialRenewalHandler;
```

#### Discussion

The renewal handler parameters are:

- **`renewResult`**: The result of the renewal request.
- **`error`**: An error, if one occurred.

## See Also

### Renewing Account Credentials
- [func renewCredentials(for: ACAccount!, completion: ((ACAccountCredentialRenewResult, (any Error)?) -> Void)!)](./acaccountstore/renewcredentials%28for,completion%29.md)
  Renews account credentials when the credentials are no longer valid.
- [enum ACAccountCredentialRenewResult](./acaccountcredentialrenewresult.md)
  Status codes of credential renewal requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstorecredentialrenewalhandler)*