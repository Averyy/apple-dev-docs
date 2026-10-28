# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified code and user activity object.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
init(code: INStartVideoCallIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INStartVideoCallIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Return Value

An initialized response object or `nil` if the object could not be created.

## Parameters

- `code`: The response code indicating your success or failure in confirming or handling the intent. For a list of possible values, see [`INStartVideoCallIntentResponseCode`](../instartvideocallintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information specific to your app. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent you’re handling, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintentresponse/init(code:useractivity:))*