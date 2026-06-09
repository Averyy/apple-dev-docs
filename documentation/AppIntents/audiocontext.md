# AudioContext

**Framework**: App Intents  
**Kind**: struct

Specifies the type of audio activity to associate with a suggested entity, allowing the system to surface relevant suggestions at the right moment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AudioContext
```

## Topics

### Structures
- [AudioContext.WorkoutIntensityLevel](audiocontext/workoutintensitylevel.md)
  The intensity level of a workout session.
### Type Properties
- [static var nowPlaying: AudioContext](audiocontext/nowplaying.md)
  The Now Playing control or complication.
- [static var workout: AudioContext](audiocontext/workout.md)
  A workout session of any type.
### Type Methods
- [static func workout(activityType: HKWorkoutActivityType) -> AudioContext](audiocontext/workout(activitytype:).md)
  A workout session of the given activity type.
- [static func workout(intensityLevel: AudioContext.WorkoutIntensityLevel) -> AudioContext](audiocontext/workout(intensitylevel:).md)
  A workout session of the given intensity level.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct RelevantEntities](relevantentities.md)
  A type you use to donate your app’s songs, albums, artists, and other media items to play during workouts.
- [struct AppEntityContext](appentitycontext.md)
  The context used to scope suggested entity donations to a specific domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/audiocontext)*