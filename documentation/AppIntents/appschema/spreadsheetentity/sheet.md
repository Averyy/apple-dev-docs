# sheet

**Framework**: App Intents  
**Kind**: property

An entity schema for a sheet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var sheet: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `spreadsheet` domain and its content matches the `sheet` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .spreadsheet.sheet)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `sheet` schema:

```swift
@AppEntity(schema: .spreadsheet.sheet)
struct SheetEntity {
    // MARK: Static

    static let defaultQuery = SheetEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String
    var sheetIndex: Int
    var spreadsheet: <#SpreadsheetEntity#>

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct SheetEntityQuery: EntityQuery {
        func entities(for identifiers: [SheetEntity.ID]) async throws -> [SheetEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var document: some AppSchemaEntity](appschema/spreadsheetentity/document.md)
  An entity schema for a document.
- [var template: some AppSchemaEntity](appschema/spreadsheetentity/template.md)
  An entity schema for a template.
- [AppSchema.SpreadsheetEntity](appschema/spreadsheetentity.md)
  Identifies entity schemas in the spreadsheet domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/spreadsheetentity/sheet)*