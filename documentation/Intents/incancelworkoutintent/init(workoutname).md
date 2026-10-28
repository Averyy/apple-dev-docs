# init(workoutName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes an intent object with the specified workout name.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(workoutName: INSpeakableString?)
```

```objc
- (instancetype) initWithWorkoutName:(INSpeakableString *) workoutName;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Typically, you don’t create instances of this class yourself. Siri creates instances when the user asks to cancel a workout. However, you can use this method during testing to create intent objects that validate your intent handling code paths.

## Parameters

- `workoutName`: The name of the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintent/init(workoutname:))*