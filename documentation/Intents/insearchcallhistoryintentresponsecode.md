# INSearchCallHistoryIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of the response.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INSearchCallHistoryIntentResponseCode
```

```c
enum INSearchCallHistoryIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSearchCallHistoryIntentResponseCode.unspecified](./insearchcallhistoryintentresponsecode/unspecified.md)
  Your app can’t provide a more specific response.
- [INSearchCallHistoryIntentResponseCode.ready](./insearchcallhistoryintentresponsecode/ready.md)
  Your app is ready to perform the search.
- [INSearchCallHistoryIntentResponseCode.continueInApp](./insearchcallhistoryintentresponsecode/continueinapp.md)
  Your extension is ready to transfer control to the app in order to display the search results.
- [INSearchCallHistoryIntentResponseCode.failure](./insearchcallhistoryintentresponsecode/failure.md)
  You were unable to perform the search.
- [INSearchCallHistoryIntentResponseCode.failureRequiringAppLaunch](./insearchcallhistoryintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to search their call history.
- [INSearchCallHistoryIntentResponseCode.failureAppConfigurationRequired](./insearchcallhistoryintentresponsecode/failureappconfigurationrequired.md)
  The user must perform additional configuration steps before searching the call history is possible.
- [INSearchCallHistoryIntentResponseCode.inProgress](./insearchcallhistoryintentresponsecode/inprogress.md)
  Your app is in the process of handling the intent.
- [INSearchCallHistoryIntentResponseCode.success](./insearchcallhistoryintentresponsecode/success.md)
  Your app successfully handled the intent.
### Initializers
- [init?(rawValue: Int)](./insearchcallhistoryintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSearchCallHistoryIntentResponseCode](./insearchcallhistoryintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintentresponsecode)*