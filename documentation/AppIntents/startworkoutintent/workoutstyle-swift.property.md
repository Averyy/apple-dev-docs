# workoutStyle

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The workout style for the intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
var workoutStyle: Self.WorkoutStyle { get set }
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](../actionbuttonarticle.md)

#### Discussion

Your implementation’s `workoutStyle` property must be a type you define that adopts either the [`AppEnum`](../appenum.md) or [`AppEntity`](../appentity.md) protocol. Declare this property using the [`AppIntent.Parameter`](../appintent/parameter.md) property wrapper.

```swift
// Define a parameter that specifies the type of workout that this
// intent starts.
@Parameter(title: "Start Workout Entity")
var workoutStyle: WorkoutEnum
```

For a complete description of implementing a [`StartWorkoutIntent`](../startworkoutintent.md), see [Responding to the Action button on Apple Watch Ultra](../actionbuttonarticle.md)

## See Also

### Defining supported workouts
- [associatedtype WorkoutStyle : AppValue](./workoutstyle-swift.associatedtype.md)
  The type to use for defining the intent’s workout style.
- [static var suggestedWorkouts: [Self]](./suggestedworkouts.md)
  A list of the supported workout styles.
- [static func invalidateSuggestedWorkouts()](./invalidatesuggestedworkouts%28%29.md)
  Tells the system when the list of suggested workouts changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/startworkoutintent/workoutstyle-swift.property)*