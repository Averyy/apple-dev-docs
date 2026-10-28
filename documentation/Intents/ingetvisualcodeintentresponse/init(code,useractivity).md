# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified code and user activity object.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(code: INGetVisualCodeIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INGetVisualCodeIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Return Value

An initialized response object or `nil` if the object could not be created.

## Discussion

After initializing the response object, put the image for the visual code in the [`visualCodeImage`](./visualcodeimage.md) property.

## Parameters

- `code`: The response code indicating your success or failure in handling the intent. For a list of possible values, see [`INGetVisualCodeIntentResponseCode`](../ingetvisualcodeintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add app-specific information. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintentresponse/init(code:useractivity:))*