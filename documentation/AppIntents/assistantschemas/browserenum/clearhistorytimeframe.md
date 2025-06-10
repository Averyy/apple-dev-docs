# clearHistoryTimeFrame

**Framework**: App Intents  
**Kind**: property

The time frame for clearing the browser history

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var clearHistoryTimeFrame: some AssistantSchemas.Enum { get }
```

## Mentions

- [Making browser actions available to Siri and Apple Intelligence](making-browser-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.browser.clearHistoryTimeFrame` schema:

```swift
@AssistantEnum(schema: .browser.clearHistoryTimeFrame)
enum ClearHistoryTimeFrame: AppEnum {

    case today
    case lastFourHours
    case todayAndYesterday
    case allTime

    static var caseDisplayRepresentations: [ClearHistoryTimeFrame: DisplayRepresentation] = [
        .today: "Today",
        .lastFourHours: "Last 4 hours",
        .todayAndYesterday: "Today and Yesterday",
        .allTime: "Beginning of time",
    ]

    static var typeDisplayName: LocalizedStringResource = "Clear History Timeframe"
}
```

For more information about the `.browser` app intent domain, see [`Making browser actions available to Siri and Apple Intelligence`](making-browser-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserenum/clearhistorytimeframe)*