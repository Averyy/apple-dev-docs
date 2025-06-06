# settings

**Framework**: App Intents  
**Kind**: property

The app entity describes settings for an audiobook or ebook.

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
var settings: some AssistantSchemas.Entity { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For more information about the `.books` app intent domain, see [`Making ebook actions available to Siri and Apple Intelligence`](making-ebook-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app entity that conforms to the `.books.settings` schema:

```swift
@AssistantEntity(schema: .books.settings)
struct BookSettingsEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [BookSettingsEntity.ID]) async throws -> [BookSettingsEntity] { [] }
        func entities(matching string: String) async throws -> [BookSettingsEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Book Settings" }

    let id = UUID()

    @Property
    var font: BookFont

    @Property
    var fontSize: BookFontSize

    @Property
    var theme: BookTheme

    @Property
    var pageNavigationSetting: BookPageNavigationSetting

    @Property
    var isTextJustified: Bool

    @Property
    var isAllowMultipleColumns: Bool}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschema/entityschema/settings)*