# Static parameter types

**Framework**: App Intents

Types that represent an enumerable list of static parameter values.

#### Overview

App enums represent a fixed set of possible values that you use as intent parameters that appear in interfaces like the Shortcuts app or Siri responses. In contrast to app entities that provide you with a way to describe dynamic content to the system, app enums describe static, predefined values you know at compile time, such as a set of categories. For example, the [`Accelerating app interactions with App Intents`](acceleratingappinteractionswithappintents.md) sample app uses an app enum to describe different types of activities it supports. The following code snippet uses an extension to add conformance with the [`AppEnum`](appenum.md) protocol to the `ActivityStyle` enumeration and provides localized display representations:

```swift
enum ActivityStyle: String, Codable, Sendable {
    case biking
    case equestrian
    case hiking
    case jogging
    case crossCountrySkiing
    case snowshoeing
    
    /// The string name for an SF Symbols symbol representing the value.
    var symbol: String {
        switch self {
        case .biking:
            return "figure.outdoor.cycle"
        case .equestrian:
            return "figure.equestrian.sports"
        case .hiking:
            return "figure.hiking"
        case .jogging:
            return "figure.run"
        case .crossCountrySkiing:
            return "figure.skiing.crosscountry"
        case .snowshoeing:
            return "snowflake"
        }
    }

    /// The HealthKit workout type that corresponds to the activity type.
    var workoutStyle: HKWorkoutActivityType {
        switch self {
        case .biking:
            return .cycling
        case .equestrian:
            return .equestrianSports
        case .hiking:
            return .hiking
        case .jogging:
            return .running
        case .crossCountrySkiing:
            return .crossCountrySkiing
        case .snowshoeing:
            return .snowSports
        }
    }
}

/// Conforming `ActivityStyle` to `AppEnum` makes it available for use as a parameter in an `AppIntent`.
extension ActivityStyle: AppEnum {
    
    /**
     A localized name representing this entity as a concept people are familiar with in the app, including localized variations based on the plural
     rules the app defines in `AppIntents.stringsdict`, which the app references through the `table` parameter. The system may show
     this value to people when they configure an intent.
     */
    static var typeDisplayRepresentation: TypeDisplayRepresentation {
        TypeDisplayRepresentation(
            name: LocalizedStringResource("Activity", table: "AppIntents"),
            numericFormat: LocalizedStringResource("\(placeholder: .int) activities", table: "AppIntents")
        )
    }
    
    /// Localized names for each case that the enumeration defines. The system shows these values to people when they configure or use an intent.
    static let caseDisplayRepresentations: [ActivityStyle: DisplayRepresentation] = [
        .biking: DisplayRepresentation(title: "Biking",
                                       subtitle: "Mountain bike ride",
                                       image: .init(systemName: "figure.outdoor.cycle")),
        
        .equestrian: DisplayRepresentation(title: "Equestrian",
                                           subtitle: "Equestrian sports",
                                           image: .init(systemName: "figure.equestrian.sports")),
        
        .hiking: DisplayRepresentation(title: "Hiking",
                                       subtitle: "A lengthy outdoor walk",
                                       image: .init(systemName: "figure.hiking")),
        
        .jogging: DisplayRepresentation(title: "Jogging",
                                        subtitle: "A gentle run",
                                        image: .init(systemName: "figure.run")),
        
        .crossCountrySkiing: DisplayRepresentation(title: "Skiing",
                                                   subtitle: "Cross-country skiing",
                                                   image: .init(systemName: "figure.skiing.crosscountry")),
        
        .snowshoeing: DisplayRepresentation(title: "Snowshoeing",
                                            subtitle: "Walking in the snow",
                                            image: .init(systemName: "snowflake"))
    ]
}
```

## Topics

### App enum
- [protocol AppEnum](appenum.md)
  An interface to express that a custom type has a predefined, static set of valid values to display.
- [protocol URLRepresentableEnum](urlrepresentableenum.md)
  An app enum with a URL representation.

## See Also

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Parameter resolution](parameter-resolution.md)
  Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.
- [Common data types](common-data-types.md)
  Specify common types that your app supports, including currencies, files, and contacts.
- [App entities](app-entities.md)
  Make core types or concepts discoverable to the system by declaring them as app entities.
- [Entity queries](entity-queries.md)
  Help the system find the entities your app defines and use them to resolve parameters.
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-enums)*