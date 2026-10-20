# AssistantSchemas.SpreadsheetEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app entities that describe spreadsheet data.

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
protocol SpreadsheetEntity : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var document: some AssistantSchemas.Entity](./spreadsheetentity/document.md)
  The app entity describes a spreadsheet.
- [var sheet: some AssistantSchemas.Entity](./spreadsheetentity/sheet.md)
  The app entity describes a sheet in a spreadsheet.
- [var template: some AssistantSchemas.Entity](./spreadsheetentity/template.md)
  The app entity describes a template for a spreadsheet.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](../assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](./entityschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/spreadsheetentity)*