# init(_:widgetKind:relevance:)

**Framework**: App Intents  
**Kind**: init

Creates an instance of this type using the specified app intent and relevance information.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
init<IntentType>(_ intent: IntentType, widgetKind: String, relevance: RelevantContext) where IntentType : WidgetConfigurationIntent
```

## Parameters

- `intent`: The app intent you want to suggest. Currently, the intent must be a [`WidgetConfigurationIntent`](widgetconfigurationintent.md) type.
- `widgetKind`: A string you use to describe the intent.
- `relevance`: Contextual clues to help the system decide where to use the widget. For more information, see the documentation for this type in the [`RelevanceKit`](https://developer.apple.com/documentation/RelevanceKit) framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantintent/init(_:widgetkind:relevance:))*