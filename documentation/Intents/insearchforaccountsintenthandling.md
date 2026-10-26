# INSearchForAccountsIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for searching for account information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
protocol INSearchForAccountsIntentHandling : NSObjectProtocol
```

```objc
@protocol INSearchForAccountsIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INSearchForAccountsIntentHandling`](./insearchforaccountsintenthandling.md) protocol to resolve, confirm, and handle requests to search for the user’s account information. Adopt this protocol in an object of your Intents extension that is capable of searching for accounts and returning account details such as the current balance.

Siri delivers an [`INSearchForAccountsIntent`](./insearchforaccountsintent.md) object to your handler when the user asks to search for accounts using your app. The provided intent object contains the parameters to use during the search. Use the methods of this protocol to resolve the parameters and perform the search.

## Topics

### Resolving the Intent Parameters
- [func resolveAccountNickname(for: INSearchForAccountsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insearchforaccountsintenthandling/resolveaccountnickname%28for,with%29.md)
  Resolves the account nickname to use during a search.
- [func resolveAccountType(for: INSearchForAccountsIntent, with: (INAccountTypeResolutionResult) -> Void)](./insearchforaccountsintenthandling/resolveaccounttype%28for,with%29.md)
  Resolves the account type to look for in a search.
- [func resolveOrganizationName(for: INSearchForAccountsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insearchforaccountsintenthandling/resolveorganizationname%28for,with%29.md)
  Resolves the organization name to use during a search.
- [func resolveRequestedBalanceType(for: INSearchForAccountsIntent, with: (INBalanceTypeResolutionResult) -> Void)](./insearchforaccountsintenthandling/resolverequestedbalancetype%28for,with%29.md)
  Resolves the balance type to look for in a search.
### Confirming the Response
- [func confirm(intent: INSearchForAccountsIntent, completion: (INSearchForAccountsIntentResponse) -> Void)](./insearchforaccountsintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can perform the search.
### Handling the Intent
- [func handle(intent: INSearchForAccountsIntent, completion: (INSearchForAccountsIntentResponse) -> Void)](./insearchforaccountsintenthandling/handle%28intent,completion%29.md)
  Handles searching for the account information.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INPaymentsDomainHandling](./inpaymentsdomainhandling.md)

## See Also

### Search for Accounts
- [class INSearchForAccountsIntent](./insearchforaccountsintent.md)
  A user request for information about their accounts in your app.
- [class INSearchForAccountsIntentResponse](./insearchforaccountsintentresponse.md)
  Your app’s response to a request to search for account information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintenthandling)*