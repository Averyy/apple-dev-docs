# renewCredentials(for:completion:)

**Framework**: Accounts  
**Kind**: method

Renews account credentials when the credentials are no longer valid.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func renewCredentials(for account: ACAccount!) async throws -> ACAccountCredentialRenewResult
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func renewCredentials(for account: ACAccount!) async throws -> ACAccountCredentialRenewResult
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

For Twitter and Sina Weibo accounts, this method prompts the user to go to Settings to re-enter their password.

For Facebook accounts, if the access token has become invalid due to a regular expiration, this method obtains a new one.

If the user has deauthorized your app, this renewal request returns `ACAccountCredentialRenewResultRejected`.

## Parameters

- `account`: The account to renew credentials.
- `completionHandler`: The handler to call when the renewal has completed.

## See Also

- [typealias ACAccountStoreCredentialRenewalHandler](acaccountstorecredentialrenewalhandler.md)
  Specifies a handler to call when credentials are renewed.
- [enum ACAccountCredentialRenewResult](acaccountcredentialrenewresult.md)
  Status codes of credential renewal requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/renewcredentials(for:completion:))*