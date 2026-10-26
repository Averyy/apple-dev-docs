# INSearchForBillsIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INSearchForBillsIntentResponseCode
```

```c
enum INSearchForBillsIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSearchForBillsIntentResponseCode.unspecified](./insearchforbillsintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INSearchForBillsIntentResponseCode.ready](./insearchforbillsintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INSearchForBillsIntentResponseCode.inProgress](./insearchforbillsintentresponsecode/inprogress.md)
  The search is still in progress.
- [INSearchForBillsIntentResponseCode.success](./insearchforbillsintentresponsecode/success.md)
  You successfully retrieved the search results.
- [INSearchForBillsIntentResponseCode.failure](./insearchforbillsintentresponsecode/failure.md)
  You were unable to retrieve the search results.
- [INSearchForBillsIntentResponseCode.failureRequiringAppLaunch](./insearchforbillsintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to perform the search.
- [INSearchForBillsIntentResponseCode.failureCredentialsUnverified](./insearchforbillsintentresponsecode/failurecredentialsunverified.md)
  You were unable to perform the search because you couldn’t verify the user’s credentials.
- [INSearchForBillsIntentResponseCode.failureBillNotFound](./insearchforbillsintentresponsecode/failurebillnotfound.md)
  The search yielded no results.
### Initializers
- [init?(rawValue: Int)](./insearchforbillsintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSearchForBillsIntentResponseCode](./insearchforbillsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintentresponsecode)*