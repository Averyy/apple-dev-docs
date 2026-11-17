# addImageToSheet

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that adds an image to a sheet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var addImageToSheet: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `spreadsheet` domain and one of your app’s actions matches the `addImageToSheet` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .spreadsheet.addImageToSheet)` Swift macro.

The following example shows an intent that conforms to the `addImageToSheet` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `spreadsheet_addImageToSheet` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .spreadsheet.addImageToSheet)
struct AddImageToSheetIntent {
    /// Image to add.
    var image: IntentFile

    /// Sheet to add the image to.
    var target: <#SheetEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the add-image-to-sheet intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `image` | `IntentFile` | App Intents | Image to add. |
| `target` | `@AppEntity(schema: .spreadsheet.sheet)` | Your app | Sheet to add the image to. `SheetEntity` is a placeholder name for a type that conforms to the [`sheet`](../spreadsheetentity/sheet.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var addAudioToSheet: some AppSchemaIntent](./addaudiotosheet.md)
  An intent schema that adds an audio clip to a sheet.
- [var addCommentToSheet: some AppSchemaIntent](./addcommenttosheet.md)
  An intent schema that adds a comment to a sheet.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/spreadsheetintent/addimagetosheet)*