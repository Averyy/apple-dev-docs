# INSearchCallHistoryIntentResponseCode.unspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your app can’t provide a more specific response.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case unspecified
```

```c
INSearchCallHistoryIntentResponseCodeUnspecified
```

## See Also

### Constants
- [INSearchCallHistoryIntentResponseCode.ready](./ready.md)
  Your app is ready to perform the search.
- [INSearchCallHistoryIntentResponseCode.continueInApp](./continueinapp.md)
  Your extension is ready to transfer control to the app in order to display the search results.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintentresponsecode/unspecified)*