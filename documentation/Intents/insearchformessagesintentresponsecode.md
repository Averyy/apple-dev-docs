# INSearchForMessagesIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the response state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INSearchForMessagesIntentResponseCode
```

```c
enum INSearchForMessagesIntentResponseCode : NSInteger;
```

## Topics

### Response State
- [INSearchForMessagesIntentResponseCode.unspecified](./insearchformessagesintentresponsecode/unspecified.md)
  The response code is unknown.
- [INSearchForMessagesIntentResponseCode.ready](./insearchformessagesintentresponsecode/ready.md)
  A response code indicating app readiness.
- [INSearchForMessagesIntentResponseCode.inProgress](./insearchformessagesintentresponsecode/inprogress.md)
  You are performing the search but do not yet have the results.
- [INSearchForMessagesIntentResponseCode.success](./insearchformessagesintentresponsecode/success.md)
  You successfully handled the intent.
- [INSearchForMessagesIntentResponseCode.failure](./insearchformessagesintentresponsecode/failure.md)
  You are unable to perform the search.
- [INSearchForMessagesIntentResponseCode.failureRequiringAppLaunch](./insearchformessagesintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to search their messages.
- [INSearchForMessagesIntentResponseCode.failureMessageServiceNotAvailable](./insearchformessagesintentresponsecode/failuremessageservicenotavailable.md)
  You were unable to perform the search because your message service is currently unavailable.
- [INSearchForMessagesIntentResponseCode.failureMessageTooManyResults](./insearchformessagesintentresponsecode/failuremessagetoomanyresults.md)
  Too many messages matched the specified search criteria.
### Enumeration Cases
- [INSearchForMessagesIntentResponseCode.failureRequiringInAppAuthentication](./insearchformessagesintentresponsecode/failurerequiringinappauthentication.md)
### Initializers
- [init?(rawValue: Int)](./insearchformessagesintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INSearchForMessagesIntentResponseCode](./insearchformessagesintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponsecode)*