# invalidateSuggestedWorkouts()

**Framework**: App Intents  
**Kind**: method

Tells the system when the list of suggested workouts changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func invalidateSuggestedWorkouts()
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)

#### Discussion

Call this method when you change the value of the [`suggestedWorkouts`](startworkoutintent/suggestedworkouts.md) property.

## See Also

- [associatedtype WorkoutStyle : AppValue](startworkoutintent/workoutstyle-swift.associatedtype.md)
  The type to use for defining the intent’s workout style.
- [var workoutStyle: Self.WorkoutStyle](startworkoutintent/workoutstyle-swift.property.md)
  The workout style for the intent.
- [static var suggestedWorkouts: [Self]](startworkoutintent/suggestedworkouts.md)
  A list of the supported workout styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/startworkoutintent/invalidatesuggestedworkouts())*