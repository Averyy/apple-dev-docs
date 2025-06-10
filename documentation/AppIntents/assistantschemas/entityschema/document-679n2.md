# document

**Framework**: App Intents  
**Kind**: property

The app entity describes a spreadsheet.

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
var document: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.spreadsheet.document` schema:

```swift
@AssistantEntity(schema: .spreadsheet.document)
struct SpreadsheetEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [SpreadsheetEntity.ID]) async throws -> [SpreadsheetEntity] { [] }
        func entities(matching string: String) async throws -> [SpreadsheetEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Spreadsheet" }

    let id = UUID()

    @Property
    var name: String

```

For more information about the `.spreadsheet` app intent domain, see [`Making spreadsheet actions available to Siri and Apple Intelligence`](making-spreadsheet-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/entityschema/document-679n2)*