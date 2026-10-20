# addCommentToSheet

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that adds a comment to a sheet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var addCommentToSheet: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `spreadsheet` domain and one of your app’s actions matches the `addCommentToSheet` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .spreadsheet.addCommentToSheet)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `addCommentToSheet` schema:

```swift
@AppIntent(schema: .spreadsheet.addCommentToSheet)
struct AddCommentToSheetIntent {
    var comment: String?
    var target: <#SheetEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Actions
- [var addAudioToSheet: some AppSchemaIntent](./addaudiotosheet.md)
  An intent schema that adds an audio clip to a sheet.
- [var addImageToSheet: some AppSchemaIntent](./addimagetosheet.md)
  An intent schema that adds an image to a sheet.
- [var addTextBoxToSheet: some AppSchemaIntent](./addtextboxtosheet.md)
  An intent schema that adds text to a sheet.
- [var addVideoToSheet: some AppSchemaIntent](./addvideotosheet.md)
  An intent schema that adds a video to a sheet.
- [var addWebVideoToSheet: some AppSchemaIntent](./addwebvideotosheet.md)
  An intent schema that adds a web video to a sheet.
- [var create: some AppSchemaIntent](./create.md)
  An intent schema that opens the app for composing a new spreadsheet.
- [var createSheet: some AppSchemaIntent](./createsheet.md)
  An intent schema that creates a new sheet in a spreadsheet.
- [var delete: some AppSchemaIntent](./delete.md)
  An intent schema that deletes existing spreadsheets.
- [var deleteSheet: some AppSchemaIntent](./deletesheet.md)
  An intent schema that deletes sheets in a spreadsheet.
- [var open: some AppSchemaIntent](./open.md)
  An intent schema that opens the app into an existing spreadsheet.
- [var openSheet: some AppSchemaIntent](./opensheet.md)
  An intent schema that opens a sheet.
- [var update: some AppSchemaIntent](./update.md)
  An intent schema that renames an existing spreadsheet.
- [var updateSheet: some AppSchemaIntent](./updatesheet.md)
  An intent schema that updates an existing sheet.
- [AppSchema.SpreadsheetIntent](../spreadsheetintent.md)
  Identifies intent schemas in the spreadsheet domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/spreadsheetintent/addcommenttosheet)*