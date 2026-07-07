# openSheet

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for opening a sheet in a spreadsheet.

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
var openSheet: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.spreadsheet.openSheet` schema:

```swift
@AppIntent(schema: .spreadsheet.openSheet)
struct OpenSheetIntent: OpenIntent {
    @Parameter var target: SheetEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
```

For more information about the `.spreadsheet` app intent domain, see doc:Making-spreadsheet-actions-available-to-Siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/spreadsheetintent/opensheet)*