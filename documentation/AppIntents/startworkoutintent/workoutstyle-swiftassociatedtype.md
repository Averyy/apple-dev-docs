# WorkoutStyle

**Framework**: App Intents  
**Kind**: associatedtype  
**Required**: Yes

The type to use for defining the intent’s workout style.

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
associatedtype WorkoutStyle : AppValue
```

#### Discussion

Assign a type that adopts either the [`AppEnum`](appenum.md) or [`AppEntity`](appentity.md) protocol.

## See Also

- [var workoutStyle: Self.WorkoutStyle](startworkoutintent/workoutstyle-swift.property.md)
  The workout style for the intent.
- [static var suggestedWorkouts: [Self]](startworkoutintent/suggestedworkouts.md)
  A list of the supported workout styles.
- [static func invalidateSuggestedWorkouts()](startworkoutintent/invalidatesuggestedworkouts.md)
  Tells the system when the list of suggested workouts changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/startworkoutintent/workoutstyle-swift.associatedtype)*