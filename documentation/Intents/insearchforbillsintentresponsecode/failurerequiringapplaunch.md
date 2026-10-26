# INSearchForBillsIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to perform the search.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INSearchForBillsIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you can’t perform the search from your Intents extension but can perform it from your app. Don’t use this code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INSearchForBillsIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSearchForBillsIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INSearchForBillsIntentResponseCode.inProgress](./inprogress.md)
  The search is still in progress.
- [INSearchForBillsIntentResponseCode.success](./success.md)
  You successfully retrieved the search results.
- [INSearchForBillsIntentResponseCode.failure](./failure.md)
  You were unable to retrieve the search results.
- [INSearchForBillsIntentResponseCode.failureCredentialsUnverified](./failurecredentialsunverified.md)
  You were unable to perform the search because you couldn’t verify the user’s credentials.
- [INSearchForBillsIntentResponseCode.failureBillNotFound](./failurebillnotfound.md)
  The search yielded no results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintentresponsecode/failurerequiringapplaunch)*