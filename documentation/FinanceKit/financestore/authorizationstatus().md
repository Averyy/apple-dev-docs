# authorizationStatus()

**Framework**: FinanceKit  
**Kind**: method  
**Role**: Instance Method

Checks the authorization status for the calling application.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func authorizationStatus() async throws -> AuthorizationStatus
```

#### Return Value

An [`AuthorizationStatus`](../authorizationstatus.md) value that indicates the current state of authorization.

## See Also

### Authorization
- [func requestAuthorization() async throws -> AuthorizationStatus](./requestauthorization%28%29.md)
  Prompts a person to give FinanceKit authorization to access financial data.
- [enum AuthorizationStatus](../authorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/authorizationstatus())*