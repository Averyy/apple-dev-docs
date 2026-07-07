# requestAuthorization()

**Framework**: FinanceKit  
**Kind**: method

Prompts a person to give FinanceKit authorization to access financial data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func requestAuthorization() async throws -> AuthorizationStatus
```

#### Return Value

An [`AuthorizationStatus`](authorizationstatus.md) value that indicates the current state of authorization.

#### Discussion

If there are no accounts are available to display, the framework presents a “No Accounts” screen and returns a status of [`AuthorizationStatus.authorized`](authorizationstatus/authorized.md) or [`AuthorizationStatus.denied`](authorizationstatus/denied.md) depending on the state of a person’s consent.

It’s safe to call this method multiple times; the framework prompts a person only if necessary.

## See Also

- [func authorizationStatus() async throws -> AuthorizationStatus](financestore/authorizationstatus.md)
  Checks the authorization status for the calling application.
- [enum AuthorizationStatus](authorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/requestauthorization())*