# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified code and user activity.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(code: INGetCarPowerLevelStatusIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INGetCarPowerLevelStatusIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

## Return Value

A newly initialized response object.

## Parameters

- `code`: The response code indicating success or failure when confirming or handling the intent. For a list of possible values, see [`INGetCarPowerLevelStatusIntentResponseCode`](../ingetcarpowerlevelstatusintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information that is specific to your app.

  If you specify `nil`, the system automatically does the following:``

  - Creates a user activity for you.
  - Sets the activity’s type to the class name of the intent being handled.
  - Sets the activity’s [`interaction`](../../Foundation/nsuseractivity/interaction.md) property to an [`INInteraction`](../ininteraction.md) object that contains the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/init(code:useractivity:))*