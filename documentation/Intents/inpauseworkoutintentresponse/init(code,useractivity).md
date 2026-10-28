# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified code and user activity object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(code: INPauseWorkoutIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INPauseWorkoutIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Return Value

An initialized response object or `nil` if the object could not be created.

## Parameters

- `code`: The response code that indicates your success or failure when handling the intent. For a list of possible codes, see [`INPauseWorkoutIntentResponseCode`](../inpauseworkoutintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information specific to your app. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpauseworkoutintentresponse/init(code:useractivity:))*