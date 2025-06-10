# suggestedWorkouts

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A list of the supported workout styles.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static var suggestedWorkouts: [Self] { get }
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)

#### Discussion

If your app is installed on Apple Watch Ultra, the system displays these workouts as options under the First Press settings when someone sets your app as the workout app in Settings > Action Button.

For a complete description of implementing a [`StartWorkoutIntent`](startworkoutintent.md), see [`Responding to the Action button on Apple Watch Ultra`](actionbuttonarticle.md)

## See Also

- [associatedtype WorkoutStyle : AppValue](startworkoutintent/workoutstyle-swift.associatedtype.md)
  The type to use for defining the intent’s workout style.
- [var workoutStyle: Self.WorkoutStyle](startworkoutintent/workoutstyle-swift.property.md)
  The workout style for the intent.
- [static func invalidateSuggestedWorkouts()](startworkoutintent/invalidatesuggestedworkouts.md)
  Tells the system when the list of suggested workouts changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/startworkoutintent/suggestedworkouts)*