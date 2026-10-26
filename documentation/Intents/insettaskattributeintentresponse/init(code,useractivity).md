# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified code and user activity object.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
init(code: INSetTaskAttributeIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INSetTaskAttributeIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

#### Return Value

An initialized response object or `nil` if the object could not be created.

#### Discussion

After initializing the response object, create an [`INTask`](../intask.md) object with the updated values that you intend to apply to your app’s data structures and assign that object to the [`modifiedTask`](./modifiedtask.md) property.

## Parameters

- `code`: The response code indicating your success or failure in handling the intent. For a list of possible values, see [`INSetTaskAttributeIntentResponse`](../insettaskattributeintentresponse.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add app-specific information. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintentresponse/init(code:useractivity:))*