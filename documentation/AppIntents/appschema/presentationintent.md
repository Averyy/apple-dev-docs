# AppSchema.PresentationIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the presentation domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol PresentationIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var addAudioToSlide: some AppSchemaIntent](appschema/presentationintent/addaudiotoslide.md)
  An intent schema that adds an audio clip to a slide.
- [var addCommentToSlide: some AppSchemaIntent](appschema/presentationintent/addcommenttoslide.md)
  An intent schema that adds a comment to a slide.
- [var addImageToSlide: some AppSchemaIntent](appschema/presentationintent/addimagetoslide.md)
  An intent schema that adds an image to a slide.
- [var addTextBoxToSlide: some AppSchemaIntent](appschema/presentationintent/addtextboxtoslide.md)
  An intent schema that adds a text box to a slide.
- [var addVideoToSlide: some AppSchemaIntent](appschema/presentationintent/addvideotoslide.md)
  An intent schema that adds a video to a slide.
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

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationintent)*