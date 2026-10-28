# INSearchForMessagesIntentResponseCode.failureMessageTooManyResults

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Too many messages matched the specified search criteria.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureMessageTooManyResults
```

```c
INSearchForMessagesIntentResponseCodeFailureMessageTooManyResults
```

## Discussion

Use this response code when your search returns more results than might make sense to display to the user. For example, you might return this code on watchOS if there are more than 20 messages.

## See Also

### Response State
- [INSearchForMessagesIntentResponseCode.unspecified](./unspecified.md)
  The response code is unknown.
- [INSearchForMessagesIntentResponseCode.ready](./ready.md)
  A response code indicating app readiness.
- [INSearchForMessagesIntentResponseCode.inProgress](./inprogress.md)
  You are performing the search but do not yet have the results.
- [INSearchForMessagesIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSearchForMessagesIntentResponseCode.failure](./failure.md)
  You are unable to perform the search.
- [INSearchForMessagesIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to search their messages.
- [INSearchForMessagesIntentResponseCode.failureMessageServiceNotAvailable](./failuremessageservicenotavailable.md)
  You were unable to perform the search because your message service is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponsecode/failuremessagetoomanyresults)*