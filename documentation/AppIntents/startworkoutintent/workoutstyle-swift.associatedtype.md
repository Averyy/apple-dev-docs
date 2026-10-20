# WorkoutStyle

**Framework**: App Intents  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type to use for defining the intent’s workout style.

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
associatedtype WorkoutStyle : AppValue
```

#### Discussion

Assign a type that adopts either the [`AppEnum`](../appenum.md) or [`AppEntity`](../appentity.md) protocol.

## See Also

### Defining supported workouts
- [var workoutStyle: Self.WorkoutStyle](./workoutstyle-swift.property.md)
  The workout style for the intent.
- [static var suggestedWorkouts: [Self]](./suggestedworkouts.md)
  A list of the supported workout styles.
- [static func invalidateSuggestedWorkouts()](./invalidatesuggestedworkouts%28%29.md)
  Tells the system when the list of suggested workouts changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/startworkoutintent/workoutstyle-swift.associatedtype)*