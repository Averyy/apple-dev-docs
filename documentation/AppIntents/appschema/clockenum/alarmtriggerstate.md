# alarmTriggerState

**Framework**: App Intents  
**Kind**: property

An enum schema for an alarm trigger state parameter.

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
var alarmTriggerState: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `clock` domain and a parameter type matches the `alarmTriggerState` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .clock.alarmTriggerState)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `alarmTriggerState` schema:

```swift
@AppEnum(schema: .clock.alarmTriggerState)
enum AlarmTriggerState: String {
    case firing
    case snoozed
    case none

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .firing: "Firing",
        .snoozed: "Snoozed",
        .none: "None"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var timerState: some AppSchemaEnum](appschema/clockenum/timerstate.md)
  An enum schema for a timer state parameter.
- [AppSchema.ClockEnum](appschema/clockenum.md)
  Identifies enum schemas in the clock domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockenum/alarmtriggerstate)*