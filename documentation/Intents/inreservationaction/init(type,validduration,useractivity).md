# init(type:validDuration:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new reservation action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(type: INReservationActionType, validDuration: INDateComponentsRange, userActivity: NSUserActivity)
```

```objc
- (instancetype) initWithType:(INReservationActionType) type validDuration:(INDateComponentsRange *) validDuration userActivity:(NSUserActivity *) userActivity;
```

## Parameters

- `type`: The type of action to create.
- `validDuration`: The date and time range the action is valid.
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information that is specific to your app. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservationaction/init(type:validduration:useractivity:))*