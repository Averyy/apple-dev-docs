# Presentation

**Framework**: App Intents

Make your presentation app’s actions available in the Shortcuts app by adopting schemas for common presentation actions.

#### Overview

The `.presentation` domain defines app schemas that provide a structured representation for common presentation actions and content. Apply schemas in the `.presentation` domain to make your app’s presentation functionality available as actions in the Shortcuts app. Schemas in this domain don’t make your conforming types discoverable by Apple Intelligence and Siri.

> 💡 **Tip**: Xcode generates a template implementation when you type `presentation_` and select a schema from the suggestions list.

For more information about app schemas, see [`App schema domains`](app-schema-domains.md).

## Topics

### Actions
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
- [var create: some AppSchemaIntent](appschema/presentationintent/create.md)
  An intent schema that opens the app for composing a new presentation.
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
### Content and parameter types
- [var document: some AppSchemaEntity](appschema/presentationentity/document.md)
  An entity schema for a document.
- [var slide: some AppSchemaEntity](appschema/presentationentity/slide.md)
  An entity schema for a slide.
- [var template: some AppSchemaEntity](appschema/presentationentity/template.md)
  An entity schema for a template.
- [AppSchema.PresentationEntity](appschema/presentationentity.md)
  Identifies entity schemas in the presentation domain.

## See Also

- [Books](app-schema-domain-books.md)
  Make your ebook reader’s actions available in the Shortcuts app by adopting schemas for common reading actions.
- [Browser](app-schema-domain-browser.md)
  Make your web browser’s actions available in the Shortcuts app by adopting schemas for common browsing actions.
- [Journaling](app-schema-domain-journaling.md)
  Make your journaling app’s actions available in the Shortcuts app by adopting schemas for journal-entry management.
- [Reader](app-schema-domain-reader.md)
  Make your document reader’s actions available in the Shortcuts app by adopting schemas for document viewing and manipulation.
- [Spreadsheet](app-schema-domain-spreadsheet.md)
  Make your spreadsheet app’s actions available in the Shortcuts app by adopting schemas for spreadsheet management.
- [Whiteboard](app-schema-domain-whiteboard.md)
  Make your whiteboard app’s actions available in the Shortcuts app by adopting schemas for common whiteboard actions.
- [Word processor](app-schema-domain-word-processor.md)
  Make your word processor’s actions available in the Shortcuts app by adopting schemas for document editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-presentation)*