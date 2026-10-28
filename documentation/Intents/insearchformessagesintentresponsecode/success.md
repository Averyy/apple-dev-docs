# INSearchForMessagesIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully handled the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case success
```

```c
INSearchForMessagesIntentResponseCodeSuccess
```

## Discussion

Use this code when your app completed the search successfully, regardless of the number of found messags. If the search yielded one or more messages, provide the details of those messages in the [`messages`](../insearchformessagesintentresponse/messages.md) property.

## See Also

### Response State
- [INSearchForMessagesIntentResponseCode.unspecified](./unspecified.md)
  The response code is unknown.
- [INSearchForMessagesIntentResponseCode.ready](./ready.md)
  A response code indicating app readiness.
- [INSearchForMessagesIntentResponseCode.inProgress](./inprogress.md)
  You are performing the search but do not yet have the results.
- [INSearchForMessagesIntentResponseCode.failure](./failure.md)
  You are unable to perform the search.
- [INSearchForMessagesIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to search their messages.
- [INSearchForMessagesIntentResponseCode.failureMessageServiceNotAvailable](./failuremessageservicenotavailable.md)
  You were unable to perform the search because your message service is currently unavailable.
- [INSearchForMessagesIntentResponseCode.failureMessageTooManyResults](./failuremessagetoomanyresults.md)
  Too many messages matched the specified search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponsecode/success)*