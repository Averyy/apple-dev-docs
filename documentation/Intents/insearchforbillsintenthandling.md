# INSearchForBillsIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for searching for bills associated with the user.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSearchForBillsIntentHandling : NSObjectProtocol
```

```objc
@protocol INSearchForBillsIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INSearchForBillsIntentHandling`](./insearchforbillsintenthandling.md) protocol to resolve, confirm, and handle requests to search for bills related to the user. Adopt this protocol in an object of your Intents extension that’s capable of searching the user’s bills and returning those bills that match the specified criteria. Users can search for bills based on the payee, the bill type, the due date, and whether the user has paid them or not.

Siri delivers an [`INSearchForBillsIntent`](./insearchforbillsintent.md) object to your handler when the user asks to search for bills using your app. The provided intent object contains the parameters to use during the search. Use the methods of this protocol to resolve the parameters and perform the search.

## Topics

### Resolving the Intent Parameters
- [func resolveBillPayee(for: INSearchForBillsIntent, with: (INBillPayeeResolutionResult) -> Void)](./insearchforbillsintenthandling/resolvebillpayee%28for,with%29.md)
  Resolves the payee to use during your search.
- [func resolveBillType(for: INSearchForBillsIntent, with: (INBillTypeResolutionResult) -> Void)](./insearchforbillsintenthandling/resolvebilltype%28for,with%29.md)
  Resolves the bill type to use during your search.
- [func resolveDueDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./insearchforbillsintenthandling/resolveduedaterange%28for,with%29.md)
  Resolves the due date to use during your search.
- [func resolvePaymentDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./insearchforbillsintenthandling/resolvepaymentdaterange%28for,with%29.md)
  Resolves the payment date to use during your search.
- [func resolveStatus(for: INSearchForBillsIntent, with: (INPaymentStatusResolutionResult) -> Void)](./insearchforbillsintenthandling/resolvestatus%28for,with%29.md)
  Resolves the bill status to use during your search.
### Confirming the Response
- [func confirm(intent: INSearchForBillsIntent, completion: (INSearchForBillsIntentResponse) -> Void)](./insearchforbillsintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can perform the search.
### Handling the Intent
- [func handle(intent: INSearchForBillsIntent, completion: (INSearchForBillsIntentResponse) -> Void)](./insearchforbillsintenthandling/handle%28intent,completion%29.md)
  Handles searching for the specified bills.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INPaymentsDomainHandling](./inpaymentsdomainhandling.md)

## See Also

### Bill Search
- [class INSearchForBillsIntent](./insearchforbillsintent.md)
  A request for the list of bills matching the specified criteria.
- [class INSearchForBillsIntentResponse](./insearchforbillsintentresponse.md)
  Your app’s response to a request to a search for bills.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintenthandling)*