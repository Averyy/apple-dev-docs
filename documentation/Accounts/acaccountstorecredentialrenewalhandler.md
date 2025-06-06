# ACAccountStoreCredentialRenewalHandler

**Framework**: Accounts  
**Kind**: typealias

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

#### Discussion

The renewal handler parameters are:

## See Also

- [func renewCredentials(for: ACAccount!, completion: ACAccountStoreCredentialRenewalHandler!)](acaccountstore/renewcredentials(for:completion:).md)
  Renews account credentials when the credentials are no longer valid.
- [enum ACAccountCredentialRenewResult](acaccountcredentialrenewresult.md)
  Status codes of credential renewal requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstorecredentialrenewalhandler)*