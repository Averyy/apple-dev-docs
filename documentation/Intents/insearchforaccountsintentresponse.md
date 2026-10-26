# INSearchForAccountsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to search for account information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INSearchForAccountsIntentResponse
```

```objc
@interface INSearchForAccountsIntentResponse : INIntentResponse
```

#### Overview

Use an [`INSearchForAccountsIntentResponse`](./insearchforaccountsintentresponse.md) object to return the account information found during a search operation. After performing a search using the criteria specified in an [`INSearchForAccountsIntent`](./insearchforaccountsintent.md) object, create an instance of this class and fill it with the results of that search. Siri communicates the information from your response to the user at appropriate times.

You create an [`INSearchForAccountsIntentResponse`](./insearchforaccountsintentresponse.md) object in the [`confirm(intent:completion:)`](./insearchforaccountsintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insearchforaccountsintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INSearchForAccountsIntentHandling`](./insearchforaccountsintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSearchForAccountsIntentResponseCode, userActivity: NSUserActivity?)](./insearchforaccountsintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSearchForAccountsIntentResponseCode](./insearchforaccountsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSearchForAccountsIntentResponseCode](./insearchforaccountsintentresponsecode.md)
  Constants indicating the state of the response.
### Providing the Search Results
- [var accounts: [INPaymentAccount]?](./insearchforaccountsintentresponse/accounts.md)
  The accounts found during the search.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Search for Accounts
- [protocol INSearchForAccountsIntentHandling](./insearchforaccountsintenthandling.md)
  The handler interface for searching for account information.
- [class INSearchForAccountsIntent](./insearchforaccountsintent.md)
  A user request for information about their accounts in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponse)*