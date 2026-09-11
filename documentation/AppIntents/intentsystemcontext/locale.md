# locale

**Framework**: App Intents  
**Kind**: property

The locale in which the system performs the app intent.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var locale: Locale { get }
```

#### Discussion

The locale for a person’s request can differ from the app’s current locale in a few cases:

- A person makes a request in a language that’s different from the system’s locale.
- A person creates a custom shortcut in the Shortcuts app that uses a locale different from their system locale.

Where possible, use `LocalizedStringResource` APIs to localize app intents and let the system choose the right locale as needed. If localized string resources aren’t an option — for example, when you generate content on a server or on device using generative models and can’t easily localize results in the app — use the [`locale`](intentsystemcontext/locale.md) property as context to provide intent results that match the person’s locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentsystemcontext/locale)*