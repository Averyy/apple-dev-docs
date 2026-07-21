# delete

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for deleting a spreadsheet.

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
var delete: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.spreadsheet.delete` schema:

```swift
@AppIntent(schema: .spreadsheet.delete)
struct DeleteSpreadsheetIntent: DeleteIntent {
    @Parameter var entities: [SpreadsheetEntity]

    func perform() async throws -> some IntentResult {
        .result()
    }
```

For more information about the `.spreadsheet` app intent domain, see [`Spreadsheet`](app-schema-domain-spreadsheet.md). For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/spreadsheetintent/delete)*