# WidgetConfigurationIntent

**Framework**: App Intents  
**Kind**: protocol

An interface for configuring a WidgetKit widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol WidgetConfigurationIntent : AppIntent
```

#### Overview

The parameters of the intent define the configuration options for your widget. The system uses the intent’s title and description for the display name and description of the widget if those values aren’t set explicitly on the [`AppIntentConfiguration`](https://developer.apple.com/documentation/WidgetKit/AppIntentConfiguration).

```swift
import AppIntents

struct FavoriteBook: WidgetConfigurationIntent {
    static var title: LocalizedStringResource = "Favorite Book"
    static var description = IntentDescription("Shows a picture of your favorite book!")

    @Parameter(title: "Title", default: "The Swift Programming Language")
    var title: String

    @Parameter(title: "Author", default: "Apple Inc.")
    var author: String
}
```

Use [`parameterSummary`](appintent/parametersummary-4vgic.md) to configure the order of the parameters in the configuration UI, as well as dynamic presentation such as using the value of one parameter to determine whether to show or hide another.

```swift
enum RefreshInterval: String, AppEnum {
    case hourly, daily, weekly

    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Refresh Interval"
    static var caseDisplayRepresentations: [RefreshInterval : DisplayRepresentation] = [
        .hourly: "Every Hour",
        .daily: "Every Day",
        .weekly: "Every Week",
    ]
}

struct FavoriteSoup: WidgetConfigurationIntent {
    static var title: LocalizedStringResource = "Favorite Soup"
    static var description = IntentDescription("Shows a picture of your favorite soup!")

    @Parameter(title: "Soup")
    var name: String?

    @Parameter(title: "Shuffle", default: true)
    var shuffle: Bool

    @Parameter(title: "Refresh", default: .daily)
    var interval: RefreshInterval

    static var parameterSummary: some ParameterSummary {
        When(\.$shuffle, .equalTo, true) {
            Summary {
                \.$name
                \.$shuffle
                \.$interval
            }
        } otherwise: {
            Summary {
                \.$name
                \.$shuffle
            }
        }
    }
}
```

When using this protocol, you don’t need to provide an implementation for [`perform()`](appintent/perform().md). You can, however, still implement `perform()` to use the same implementation for both widget configuration and as an actionable intent. For more information, refer to the [`Emoji Rangers: Supporting Live Activities, interactivity, and animations`](https://developer.apple.com/documentation/WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations) sample code project’s `EmojiRangerSelection` structure and [`AppIntentTimelineProvider`](https://developer.apple.com/documentation/WidgetKit/AppIntentTimelineProvider).

## Topics

### Widget families
- [enum IntentWidgetFamily](intentwidgetfamily.md)
### Associated Types
- [associatedtype NeverResult](widgetconfigurationintent/neverresult.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol ControlConfigurationIntent](controlconfigurationintent.md)
  An interface for configuring a Control Center module.
- [protocol LiveActivityStartingIntent](liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.
- [protocol LiveActivityIntent](liveactivityintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/widgetconfigurationintent)*