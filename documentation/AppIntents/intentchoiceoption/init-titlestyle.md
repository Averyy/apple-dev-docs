# init(title:style:)

**Framework**: App Intents  
**Kind**: init

Creates a new option for a person to choose to continue an app intent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(title: LocalizedStringResource, style: IntentChoiceOption.Style = .default)
```

## Parameters

- `title`: The localized text to display for this option.
- `style`: The visual style to apply; for example,     or  .   By default, the   for an intent choice option is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentchoiceoption/init(title:style:))*