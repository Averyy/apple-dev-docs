# Making spreadsheet actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities to integrate your app’s spreadsheet functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s spreadsheet capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent and app entity implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows someone to open a spreadsheet, use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.spreadsheet` domain and the [`open`](assistantschemas/spreadsheetintent/open.md) schema:

```swift
@AssistantIntent(schema: .spreadsheet.open)
struct OpenSpreadsheetIntent: OpenIntent {
    var target: SpreadsheetDocumentEntity

    @MainActor
    func perform() async throws -> some IntentResult {
        return .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.spreadsheet` domain, see [`AssistantSchemas.SpreadsheetIntent`](assistantschemas/spreadsheetintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `SpreadsheetEntity`. The following code snippet shows how the `SpreadsheetEntity` implementation uses the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro:

```swift
@AssistantEntity(schema: .spreadsheet.document)
struct SpreadsheetDocumentEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [SpreadsheetDocumentEntity.ID]) async throws -> [SpreadsheetDocumentEntity] { [] }
        func entities(matching string: String) async throws -> [SpreadsheetDocumentEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Provide a display representation." }

    let id = UUID()

    var name: String
}
```

The assistant schema for the `PresentationEntity` consists of the `.spreadsheet` domain and the [`document`](assistantschemas/spreadsheetentity/document.md) schema.

For a list of available app entity schemas in the `.spreadsheet` domain, see [`AssistantSchemas.SpreadsheetEntity`](assistantschemas/spreadsheetentity.md).

## See Also

- [AssistantSchemas.SpreadsheetIntent](assistantschemas/spreadsheetintent.md)
  Assistant schema conformance for app intents that offer spreadsheet functionality.
- [AssistantSchemas.SpreadsheetEntity](assistantschemas/spreadsheetentity.md)
  Assistant schema conformance for app entities that describe spreadsheet data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-spreadsheet-actions-available-to-siri-and-apple-intelligence)*