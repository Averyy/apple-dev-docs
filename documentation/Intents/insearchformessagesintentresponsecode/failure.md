# INSearchForMessagesIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You are unable to perform the search.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failure
```

```c
INSearchForMessagesIntentResponseCodeFailure
```

## Discussion

Use this code for both transient and unrecoverable errors that would prevent your app from searching the user’s messages.

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
- [INSearchForMessagesIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to search their messages.
- [INSearchForMessagesIntentResponseCode.failureMessageServiceNotAvailable](./failuremessageservicenotavailable.md)
  You were unable to perform the search because your message service is currently unavailable.
- [INSearchForMessagesIntentResponseCode.failureMessageTooManyResults](./failuremessagetoomanyresults.md)
  Too many messages matched the specified search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponsecode/failure)*