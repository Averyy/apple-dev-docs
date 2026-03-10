# updateSheet

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for updating a sheet in a spreadsheet.

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
var updateSheet: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.spreadsheet.updateSheet` schema:

```swift
@AppIntent(schema: .spreadsheet.updateSheet)
struct UpdateSheetIntent: AppIntent {
    @Parameter
    var target: SheetEntity

    @Parameter
    var name: String?

    @Parameter
    var position: Int?

    func perform() async throws -> some IntentResult {
        .result()
    }
```

For more information about the `.spreadsheet` app intent domain, see [`Making spreadsheet actions available to Siri and Apple Intelligence`](making-spreadsheet-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var addAudioToSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/addaudiotosheet.md)
  The app intent conforms to the schema for adding audio to a slide.
- [var addCommentToSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/addcommenttosheet.md)
  The app intent conforms to the schema for adding a comment to a sheet in a spreadsheet.
- [var addImageToSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/addimagetosheet.md)
  The app intent conforms to the schema for adding an image to a sheet in a spreadsheet.
- [var addTextBoxToSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/addtextboxtosheet.md)
  The app intent conforms to the schema for adding a textbox to a sheet in a spreadsheet.
- [var addVideoToSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/addvideotosheet.md)
  The app intent conforms to the schema for adding a video to a sheet in a spreadsheet.
- [var addWebVideoToSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/addwebvideotosheet.md)
  The app intent conforms to the schema for adding a web video to a sheet in a spreadsheet.
- [var create: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/create.md)
  The app intent conforms to the schema for creating a spreadsheet.
- [var createSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/createsheet.md)
  The app intent conforms to the schema for creating a sheet in a spreadsheet.
- [var delete: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/delete.md)
  The app intent conforms to the schema for deleting a spreadsheet.
- [var deleteSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/deletesheet.md)
  The app intent conforms to the schema for deleting a sheet in a spreadsheet.
- [var open: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/open.md)
  The app intent conforms to the schema for opening a spreadsheet.
- [var openSheet: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/opensheet.md)
  The app intent conforms to the schema for opening a sheet in a spreadsheet.
- [var update: some AssistantSchemas.Intent](assistantschemas/spreadsheetintent/update.md)
  The app intent conforms to the schema for updating a spreadsheet.
- [AssistantSchemas.SpreadsheetIntent](assistantschemas/spreadsheetintent.md)
  Assistant schema conformance for app intents that offer spreadsheet functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/spreadsheetintent/updatesheet)*