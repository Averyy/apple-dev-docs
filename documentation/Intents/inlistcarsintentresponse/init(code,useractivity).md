# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a response object with the specified code and user activity.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(code: INListCarsIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INListCarsIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Parameters

- `code`: The response code that indicates success or failure when confirming or handling the intent. For a list of possible values, see [`INListCarsIntentResponseCode`](../inlistcarsintentresponsecode.md).
- `userActivity`: A user activity that the system passes to your app if it launches as a result of this response. Use an activity if you need to provide additional information specific to your app.

  If you specify `nil`, the system automatically:

  - Creates a user activity for you.
  - Sets the activity’s type to the class name of the intent it’s handling.
  - Sets the activity’s [`interaction`](../../Foundation/nsuseractivity/interaction.md) property to an instance of [`INInteraction`](../ininteraction.md) that contains the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintentresponse/init(code:useractivity:))*