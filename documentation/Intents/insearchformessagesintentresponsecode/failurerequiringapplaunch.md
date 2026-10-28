# INSearchForMessagesIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to search their messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INSearchForMessagesIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you cannot handle the request through Siri for a reason not covered by any other response code. For example, you might use this code if the user has not set up an account with your app. Do not use it for general errors or to force the user to launch your app.

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
- [INSearchForMessagesIntentResponseCode.failureMessageServiceNotAvailable](./failuremessageservicenotavailable.md)
  You were unable to perform the search because your message service is currently unavailable.
- [INSearchForMessagesIntentResponseCode.failureMessageTooManyResults](./failuremessagetoomanyresults.md)
  Too many messages matched the specified search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponsecode/failurerequiringapplaunch)*