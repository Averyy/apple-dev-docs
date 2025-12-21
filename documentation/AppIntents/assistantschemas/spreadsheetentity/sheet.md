# sheet

**Framework**: App Intents  
**Kind**: property

The app entity describes a sheet in a spreadsheet.

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
var sheet: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.spreadsheet.sheet` schema:

```swift
@AppEntity(schema: .spreadsheet.sheet)
struct SheetEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [SheetEntity.ID]) async throws -> [SheetEntity] { [] }
        func entities(matching string: String) async throws -> [SheetEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Sheet" }

    let id = UUID()

    @Property
    public var spreadsheet: SpreadsheetEntity

    @Property
    public var name: String

    @Property
    public var sheetIndex: Int
```

For more information about the `.spreadsheet` app intent domain, see [`Making spreadsheet actions available to Siri and Apple Intelligence`](making-spreadsheet-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/spreadsheetentity/sheet)*