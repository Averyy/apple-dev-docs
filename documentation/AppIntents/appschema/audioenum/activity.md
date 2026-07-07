# activity

**Framework**: App Intents  
**Kind**: property

An enum schema for an activity parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var activity: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `audio` domain and a parameter type matches the `activity` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .audio.activity)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `activity` schema:

```swift
@AppEnum(schema: .audio.activity)
enum AudioActivity: String {
    case cooking
    case dining
    case studying
    case focusing
    case reading
    case gaming
    case working
    case showering
    case cleaning
    case relaxing
    case sleeping
    case indoorActivity
    case partying
    case commuting
    case driving
    case traveling
    case gardening
    case barbecuing
    case beachDay
    case roadTrip
    case outdoorActivity
    case meditating
    case yoga
    case walking
    case running
    case strength
    case cycling
    case dance
    case hiit
    case rowing
    case workoutLowIntensity
    case workoutMediumIntensity
    case workoutHighIntensity

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .cooking: "Cooking",
        .dining: "Dining",
        .studying: "Studying",
        .focusing: "Focusing",
        .reading: "Reading",
        .gaming: "Gaming",
        .working: "Working",
        .showering: "Showering",
        .cleaning: "Cleaning",
        .relaxing: "Relaxing",
        .sleeping: "Sleeping",
        .indoorActivity: "IndoorActivity",
        .partying: "Partying",
        .commuting: "Commuting",
        .driving: "Driving",
        .traveling: "Traveling",
        .gardening: "Gardening",
        .barbecuing: "Barbecuing",
        .beachDay: "BeachDay",
        .roadTrip: "RoadTrip",
        .outdoorActivity: "OutdoorActivity",
        .meditating: "Meditating",
        .yoga: "Yoga",
        .walking: "Walking",
        .running: "Running",
        .strength: "Strength",
        .cycling: "Cycling",
        .dance: "Dance",
        .hiit: "Hiit",
        .rowing: "Rowing",
        .workoutLowIntensity: "WorkoutLowIntensity",
        .workoutMediumIntensity: "WorkoutMediumIntensity",
        .workoutHighIntensity: "WorkoutHighIntensity"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var affinityState: some AppSchemaEnum](appschema/audioenum/affinitystate.md)
  An enum schema for an affinity state parameter.
- [var appViewIdentifier: some AppSchemaEnum](appschema/audioenum/appviewidentifier.md)
  An enum schema for an app view identifier parameter.
- [var invocationSource: some AppSchemaEnum](appschema/audioenum/invocationsource.md)
  An enum schema for an invocation source parameter.
- [var playbackAttributes: some AppSchemaEnum](appschema/audioenum/playbackattributes.md)
  An enum schema for a playback attributes parameter.
- [var queueInsertionLocation: some AppSchemaEnum](appschema/audioenum/queueinsertionlocation.md)
  An enum schema for a queue insertion location parameter.
- [AppSchema.AudioEnum](appschema/audioenum.md)
  Identifies enum schemas in the audio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audioenum/activity)*