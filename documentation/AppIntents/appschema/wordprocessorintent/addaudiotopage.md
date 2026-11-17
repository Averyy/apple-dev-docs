# addAudioToPage

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that adds an audio clip to a page.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var addAudioToPage: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `wordProcessor` domain and one of your app’s actions matches the `addAudioToPage` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .wordProcessor.addAudioToPage)` Swift macro.

The following example shows an intent that conforms to the `addAudioToPage` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `wordProcessor_addAudioToPage` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .wordProcessor.addAudioToPage)
struct AddAudioToWordProcessorPageIntent {
    /// Audio to add.
    var audio: IntentFile

    /// Page to add the audio to.
    var target: <#WordProcessorPageEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the add-audio-to-page intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `audio` | `IntentFile` | App Intents | Audio to add. |
| `target` | `@AppEntity(schema: .wordProcessor.page)` | Your app | Page to add the audio to. `WordProcessorPageEntity` is a placeholder name for a type that conforms to the [`page`](../wordprocessorentity/page.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var addImageToPage: some AppSchemaIntent](./addimagetopage.md)
  An intent schema that adds an image to a page.
- [var addTextBoxToPage: some AppSchemaIntent](./addtextboxtopage.md)
  An intent schema that adds a textbox to a page.
- [var addVideoToPage: some AppSchemaIntent](./addvideotopage.md)
  An intent schema that adds a video to a page.
- [var addWebVideoToPage: some AppSchemaIntent](./addwebvideotopage.md)
  An intent schema that adds a web video to a page.
- [var create: some AppSchemaIntent](./create.md)
  An intent schema that opens the app for composing a new text document.
- [var createPage: some AppSchemaIntent](./createpage.md)
  An intent schema that creates a new page in an editor document.
- [var open: some AppSchemaIntent](./open.md)
  An intent schema that opens the app to an editor.
- [var openPage: some AppSchemaIntent](./openpage.md)
  An intent schema that opens an editor document page.
- [AppSchema.WordProcessorIntent](../wordprocessorintent.md)
  Identifies intent schemas in the word processor domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/wordprocessorintent/addaudiotopage)*