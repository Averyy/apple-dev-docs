# update

**Framework**: App Intents  
**Kind**: property

An intent schema that renames an existing spreadsheet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var update: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `spreadsheet` domain and one of your app’s actions matches the `update` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .spreadsheet.update)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `update` schema:

```swift
@AppIntent(schema: .spreadsheet.update)
struct UpdateSpreadsheetIntent {
    var target: <#SpreadsheetEntity#>
    var name: String?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var addAudioToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addaudiotosheet.md)
  An intent schema that adds an audio clip to a sheet.
- [var addCommentToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addcommenttosheet.md)
  An intent schema that adds a comment to a sheet.
- [var addImageToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addimagetosheet.md)
  An intent schema that adds an image to a sheet.
- [var addTextBoxToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addtextboxtosheet.md)
  An intent schema that adds text to a sheet.
- [var addVideoToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addvideotosheet.md)
  An intent schema that adds a video to a sheet.
- [var addWebVideoToSheet: some AppSchemaIntent](appschema/spreadsheetintent/addwebvideotosheet.md)
  An intent schema that adds a web video to a sheet.
- [var create: some AppSchemaIntent](appschema/spreadsheetintent/create.md)
  An intent schema that opens the app for composing a new spreadsheet.
- [var createSheet: some AppSchemaIntent](appschema/spreadsheetintent/createsheet.md)
  An intent schema that creates a new sheet in a spreadsheet.
- [var delete: some AppSchemaIntent](appschema/spreadsheetintent/delete.md)
  An intent schema that deletes existing spreadsheets.
- [var deleteSheet: some AppSchemaIntent](appschema/spreadsheetintent/deletesheet.md)
  An intent schema that deletes sheets in a spreadsheet.
- [var open: some AppSchemaIntent](appschema/spreadsheetintent/open.md)
  An intent schema that opens the app into an existing spreadsheet.
- [var openSheet: some AppSchemaIntent](appschema/spreadsheetintent/opensheet.md)
  An intent schema that opens a sheet.
- [var updateSheet: some AppSchemaIntent](appschema/spreadsheetintent/updatesheet.md)
  An intent schema that updates an existing sheet.
- [AppSchema.SpreadsheetIntent](appschema/spreadsheetintent.md)
  Identifies intent schemas in the spreadsheet domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/spreadsheetintent/update)*