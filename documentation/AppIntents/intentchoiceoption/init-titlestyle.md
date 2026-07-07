# init(title:style:)

**Framework**: App Intents  
**Kind**: init

Creates a new option for a person to choose to continue an app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(title: LocalizedStringResource, style: IntentChoiceOption.Style = .default)
```

## Parameters

- `title`: The localized text to display for this option.
- `style`: The visual style to apply; for example,  `AppIntents/IntentChoiceOption/destructive` or [`cancel`](intentchoiceoption/cancel.md). By default, the `style` for an intent choice option is `AppIntents/IntentChoiceOption/default`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentchoiceoption/init(title:style:))*