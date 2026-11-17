# create

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that opens the app for composing a new presentation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var create: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `presentation` domain and one of your app’s actions matches the `create` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .presentation.create)` Swift macro.

The following example shows an intent that conforms to the `create` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `presentation_create` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .presentation.create)
struct CreatePresentationIntent {
    /// Template with which to create the presentation.
    var template: <#PresentationTemplateEntity#>?

    func perform() async throws -> some ReturnsValue<<#PresentationEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the create intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `template` | `@AppEntity(schema: .presentation.template)?` | Your app | Template with which to create the presentation. `PresentationTemplateEntity` is a placeholder name for a type that conforms to the [`template`](../presentationentity/template.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var addAudioToSlide: some AppSchemaIntent](./addaudiotoslide.md)
  An intent schema that adds an audio clip to a slide.
- [var addCommentToSlide: some AppSchemaIntent](./addcommenttoslide.md)
  An intent schema that adds a comment to a slide.
- [var addImageToSlide: some AppSchemaIntent](./addimagetoslide.md)
  An intent schema that adds an image to a slide.
- [var addTextBoxToSlide: some AppSchemaIntent](./addtextboxtoslide.md)
  An intent schema that adds a text box to a slide.
- [var addWebVideoToSlide: some AppSchemaIntent](./addwebvideotoslide.md)
  An intent schema that adds a web video to a slide.
- [var createSlide: some AppSchemaIntent](./createslide.md)
  An intent schema that creates a new slide in a presentation document.
- [var deleteSlide: some AppSchemaIntent](./deleteslide.md)
  An intent schema that deletes slides in a presentation.
- [var open: some AppSchemaIntent](./open.md)
  An intent schema that opens the app into an existing presentation.
- [var openSlide: some AppSchemaIntent](./openslide.md)
  An intent schema that opens a slide.
- [var setSlideTitle: some AppSchemaIntent](./setslidetitle.md)
  An intent schema that sets the title of the slide.
- [var startPlayback: some AppSchemaIntent](./startplayback.md)
  An intent schema that plays the presentation from the start or selected slide.
- [var stopPlayback: some AppSchemaIntent](./stopplayback.md)
  An intent schema that stops the currently playing presentation.
- [var update: some AppSchemaIntent](./update.md)
  An intent schema that renames an existing presentation.
- [AppSchema.PresentationIntent](../presentationintent.md)
  Identifies intent schemas in the presentation domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationintent/create)*