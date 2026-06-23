# create

**Framework**: App Intents  
**Kind**: property

An intent schema that opens the app for composing a new presentation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var create: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `presentation` domain and one of your app’s actions matches the `create` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .presentation.create)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `create` schema:

```swift
@AppIntent(schema: .presentation.create)
struct CreatePresentationIntent {
    var template: <#PresentationTemplateEntity#>?

    func perform() async throws -> some ReturnsValue<<#PresentationEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var addAudioToSlide: some AppSchemaIntent](appschema/presentationintent/addaudiotoslide.md)
  An intent schema that adds an audio clip to a slide.
- [var addCommentToSlide: some AppSchemaIntent](appschema/presentationintent/addcommenttoslide.md)
  An intent schema that adds a comment to a slide.
- [var addImageToSlide: some AppSchemaIntent](appschema/presentationintent/addimagetoslide.md)
  An intent schema that adds an image to a slide.
- [var addTextBoxToSlide: some AppSchemaIntent](appschema/presentationintent/addtextboxtoslide.md)
  An intent schema that adds a text box to a slide.
- [var addWebVideoToSlide: some AppSchemaIntent](appschema/presentationintent/addwebvideotoslide.md)
  An intent schema that adds a web video to a slide.
- [var createSlide: some AppSchemaIntent](appschema/presentationintent/createslide.md)
  An intent schema that creates a new slide in a presentation document.
- [var deleteSlide: some AppSchemaIntent](appschema/presentationintent/deleteslide.md)
  An intent schema that deletes slides in a presentation.
- [var open: some AppSchemaIntent](appschema/presentationintent/open.md)
  An intent schema that opens the app into an existing presentation.
- [var openSlide: some AppSchemaIntent](appschema/presentationintent/openslide.md)
  An intent schema that opens a slide.
- [var setSlideTitle: some AppSchemaIntent](appschema/presentationintent/setslidetitle.md)
  An intent schema that sets the title of the slide.
- [var startPlayback: some AppSchemaIntent](appschema/presentationintent/startplayback.md)
  An intent schema that plays the presentation from the start or selected slide.
- [var stopPlayback: some AppSchemaIntent](appschema/presentationintent/stopplayback.md)
  An intent schema that stops the currently playing presentation.
- [var update: some AppSchemaIntent](appschema/presentationintent/update.md)
  An intent schema that renames an existing presentation.
- [AppSchema.PresentationIntent](appschema/presentationintent.md)
  Identifies intent schemas in the presentation domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationintent/create)*