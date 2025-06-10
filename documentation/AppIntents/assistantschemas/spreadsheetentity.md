# AssistantSchemas.SpreadsheetEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe spreadsheet data.

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
protocol SpreadsheetEntity : AssistantSchemas.Model
```

## Mentions

- [Making spreadsheet actions available to Siri and Apple Intelligence](making-spreadsheet-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var document: some AssistantSchemas.Entity](assistantschemas/spreadsheetentity/document.md)
  The app entity describes a spreadsheet.
- [var sheet: some AssistantSchemas.Entity](assistantschemas/spreadsheetentity/sheet.md)
  The app entity describes a sheet in a spreadsheet.
- [var template: some AssistantSchemas.Entity](assistantschemas/spreadsheetentity/template.md)
  The app entity describes a template for a spreadsheet.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)

## See Also

- [Making spreadsheet actions available to Siri and Apple Intelligence](making-spreadsheet-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s spreadsheet functionality with Siri and Apple Intelligence.
- [AssistantSchemas.SpreadsheetIntent](assistantschemas/spreadsheetintent.md)
  Assistant schema conformance for app intents that offer spreadsheet functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/spreadsheetentity)*