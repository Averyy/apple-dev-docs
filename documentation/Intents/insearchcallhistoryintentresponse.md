# INSearchCallHistoryIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a search call history intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSearchCallHistoryIntentResponse
```

```objc
@interface INSearchCallHistoryIntentResponse : INIntentResponse
```

## Overview

Use an [`INSearchCallHistoryIntentResponse`](./insearchcallhistoryintentresponse.md) object to specify the results of searching the user’s call history. After performing a search using the criteria specified in the [`INSearchCallHistoryIntent`](./insearchcallhistoryintent.md) object, create an instance of this class with the results of that search.

Your app is responsible for displaying the results of your search, so you must communicate the results to it. One way to communicate those results is through the [`NSUserActivity`](../Foundation/nsuseractivity.md) object that you create with your response. After creating that object, place the results in its [`userInfo`](../Foundation/nsuseractivity/userinfo.md) dictionary.

You create an [`INSearchCallHistoryIntentResponse`](./insearchcallhistoryintentresponse.md) object in the [`confirm(intent:completion:)`](./insearchcallhistoryintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insearchcallhistoryintenthandling/handle%28intent,completion%29.md) methods of your search call history handler object. For more information about implementing your handler object, see [`INSearchCallHistoryIntentHandling`](./insearchcallhistoryintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSearchCallHistoryIntentResponseCode, userActivity: NSUserActivity?)](./insearchcallhistoryintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSearchCallHistoryIntentResponseCode](./insearchcallhistoryintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSearchCallHistoryIntentResponseCode](./insearchcallhistoryintentresponsecode.md)
  Constants indicating the status of the response.
### Providing the Search Results
- [var callRecords: [INCallRecord]?](./insearchcallhistoryintentresponse/callrecords.md)
  An array of call records representing the results of the search.

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

### Call History Search
- [protocol INSearchCallHistoryIntentHandling](./insearchcallhistoryintenthandling.md)
  The handler interface for searching the user’s call history.
- [class INSearchCallHistoryIntent](./insearchcallhistoryintent.md)
  A request to list the calls matching the specified criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintentresponse)*