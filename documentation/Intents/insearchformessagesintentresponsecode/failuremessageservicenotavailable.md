# INSearchForMessagesIntentResponseCode.failureMessageServiceNotAvailable

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to perform the search because your message service is currently unavailable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureMessageServiceNotAvailable
```

```c
INSearchForMessagesIntentResponseCodeFailureMessageServiceNotAvailable
```

#### Discussion

You might use this code if searches occur on a remote server and the network is unavailable.

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
- [INSearchForMessagesIntentResponseCode.failureMessageTooManyResults](./failuremessagetoomanyresults.md)
  Too many messages matched the specified search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponsecode/failuremessageservicenotavailable)*