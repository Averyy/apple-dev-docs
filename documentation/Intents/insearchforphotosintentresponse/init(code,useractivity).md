# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified code and user activity object.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(code: INSearchForPhotosIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INSearchForPhotosIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

#### Discussion

After initializing the object, assign a value to the [`searchResultsCount`](./searchresultscount-3i5mz.md) property indicating the number of photos that match the search parameters.

## Parameters

- `code`: The response code indicating your success or failure in confirming or handling the intent. For a list of possible values, see [`INSearchForPhotosIntentResponseCode`](../insearchforphotosintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information specific to your app. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintentresponse/init(code:useractivity:))*