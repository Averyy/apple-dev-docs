# updateSettings

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for updating settings for an ebook.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var updateSettings: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.books.updateSettings` schema:

```swift
@AppIntent(schema: .books.updateSettings)
struct UpdateBookSettingsIntent: AppIntent {
    @Parameter
    var target: BookSettingsEntity

    @Parameter
    var page: Int?

    @Parameter
    var font: BookFont?

    @Parameter
    var theme: BookTheme?

    @Parameter
    var pageNavigationSetting: BookPageNavigationSetting?

    @Parameter
    var isTextJustified: Bool?

    @Parameter
    var isAllowMultipleColumns: Bool?

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.books` app intent domain, see doc:Making-ebook-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksintent/updatesettings)*