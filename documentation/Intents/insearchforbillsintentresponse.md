# INSearchForBillsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to a search for bills.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSearchForBillsIntentResponse
```

```objc
@interface INSearchForBillsIntentResponse : INIntentResponse
```

## Overview

Use an [`INSearchForBillsIntentResponse`](./insearchforbillsintentresponse.md) object to return the list of bills found during a search operation. After performing a search using the criteria specified in an [`INSearchForBillsIntent`](./insearchforbillsintent.md) object, create an instance of this class and fill it with the results of that search. Siri communicates the information from your response to the user at appropriate times.

You create an [`INSearchForBillsIntentResponse`](./insearchforbillsintentresponse.md) object in the [`confirm(intent:completion:)`](./insearchforbillsintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insearchforbillsintenthandling/handle%28intent,completion%29.md) methods of your search for bills handler object. For more information about implementing your handler object, see [`INSearchForBillsIntentHandling`](./insearchforbillsintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSearchForBillsIntentResponseCode, userActivity: NSUserActivity?)](./insearchforbillsintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSearchForBillsIntentResponseCode](./insearchforbillsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSearchForBillsIntentResponseCode](./insearchforbillsintentresponsecode.md)
  Constants indicating the state of the response.
### Accessing the Search Results
- [var bills: [INBillDetails]?](./insearchforbillsintentresponse/bills.md)
  The bills found during the search.

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

### Bill Search
- [protocol INSearchForBillsIntentHandling](./insearchforbillsintenthandling.md)
  The handler interface for searching for bills associated with the user.
- [class INSearchForBillsIntent](./insearchforbillsintent.md)
  A request for the list of bills matching the specified criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintentresponse)*