# renewCredentials(for:completion:)

**Framework**: Accounts  
**Kind**: method  
**Role**: Instance Method

Renews account credentials when the credentials are no longer valid.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
func renewCredentials(for account: ACAccount!, completion completionHandler: (@Sendable (ACAccountCredentialRenewResult, (any Error)?) -> Void)!)
```

```swift
func renewCredentials(for account: ACAccount!) async throws -> ACAccountCredentialRenewResult
```

```objc
- (void) renewCredentialsForAccount:(ACAccount *) account completion:(ACAccountStoreCredentialRenewalHandler) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func renewCredentials(for account: ACAccount!) async throws -> ACAccountCredentialRenewResult
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

For Twitter and Sina Weibo accounts, this method prompts the user to go to Settings to re-enter their password.

For Facebook accounts, if the access token has become invalid due to a regular expiration, this method obtains a new one.

If the user has deauthorized your app, this renewal request returns `ACAccountCredentialRenewResultRejected`.

## Parameters

- `account`: The account to renew credentials.
- `completionHandler`: The handler to call when the renewal has completed.

## See Also

### Renewing Account Credentials
- [typealias ACAccountStoreCredentialRenewalHandler](../acaccountstorecredentialrenewalhandler.md)
  Specifies a handler to call when credentials are renewed.
- [enum ACAccountCredentialRenewResult](../acaccountcredentialrenewresult.md)
  Status codes of credential renewal requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/renewcredentials(for:completion:))*