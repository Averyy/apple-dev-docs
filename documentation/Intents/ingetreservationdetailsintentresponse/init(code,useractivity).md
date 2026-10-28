# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates the response object with the specified code and user activity object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(code: INGetReservationDetailsIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INGetReservationDetailsIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Return Value

An initialized response object or `nil` if the object could not be created.

## Parameters

- `code`: The response code indicating your success or failure in confirming or handling the intent. For a list of possible values, see [`INGetReservationDetailsIntentResponseCode`](../ingetreservationdetailsintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information that is specific to your app. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintentresponse/init(code:useractivity:))*