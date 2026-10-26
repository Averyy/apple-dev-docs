# INSearchCallHistoryIntentResponseCode.continueInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your extension is ready to transfer control to the app in order to display the search results.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case continueInApp
```

```c
INSearchCallHistoryIntentResponseCodeContinueInApp
```

#### Discussion

Upon returning this code, Siri launches your app and passes it the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object you provided at initialization time. (If you didn’t provide a user activity object, Siri creates one for you). Siri adds an [`INInteraction`](../ininteraction.md) object with the intent and your response to the user activity object before delivering it. Your app should use the information in the user activity object to display the search results.

## See Also

### Constants
- [INSearchCallHistoryIntentResponseCode.unspecified](./unspecified.md)
  Your app can’t provide a more specific response.
- [INSearchCallHistoryIntentResponseCode.ready](./ready.md)
  Your app is ready to perform the search.
- [INSearchCallHistoryIntentResponseCode.failure](./failure.md)
  You were unable to perform the search.
- [INSearchCallHistoryIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to search their call history.
- [INSearchCallHistoryIntentResponseCode.failureAppConfigurationRequired](./failureappconfigurationrequired.md)
  The user must perform additional configuration steps before searching the call history is possible.
- [INSearchCallHistoryIntentResponseCode.inProgress](./inprogress.md)
  Your app is in the process of handling the intent.
- [INSearchCallHistoryIntentResponseCode.success](./success.md)
  Your app successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintentresponsecode/continueinapp)*