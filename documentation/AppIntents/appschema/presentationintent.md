# AppSchema.PresentationIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the presentation domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol PresentationIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var addAudioToSlide: some AppSchemaIntent](./presentationintent/addaudiotoslide.md)
  An intent schema that adds an audio clip to a slide.
- [var addCommentToSlide: some AppSchemaIntent](./presentationintent/addcommenttoslide.md)
  An intent schema that adds a comment to a slide.
- [var addImageToSlide: some AppSchemaIntent](./presentationintent/addimagetoslide.md)
  An intent schema that adds an image to a slide.
- [var addTextBoxToSlide: some AppSchemaIntent](./presentationintent/addtextboxtoslide.md)
  An intent schema that adds a text box to a slide.
- [var addVideoToSlide: some AppSchemaIntent](./presentationintent/addvideotoslide.md)
  An intent schema that adds a video to a slide.
- [var addWebVideoToSlide: some AppSchemaIntent](./presentationintent/addwebvideotoslide.md)
  An intent schema that adds a web video to a slide.
- [var create: some AppSchemaIntent](./presentationintent/create.md)
  An intent schema that opens the app for composing a new presentation.
- [var createSlide: some AppSchemaIntent](./presentationintent/createslide.md)
  An intent schema that creates a new slide in a presentation document.
- [var deleteSlide: some AppSchemaIntent](./presentationintent/deleteslide.md)
  An intent schema that deletes slides in a presentation.
- [var open: some AppSchemaIntent](./presentationintent/open.md)
  An intent schema that opens the app into an existing presentation.
- [var openSlide: some AppSchemaIntent](./presentationintent/openslide.md)
  An intent schema that opens a slide.
- [var setSlideTitle: some AppSchemaIntent](./presentationintent/setslidetitle.md)
  An intent schema that sets the title of the slide.
- [var startPlayback: some AppSchemaIntent](./presentationintent/startplayback.md)
  An intent schema that plays the presentation from the start or selected slide.
- [var stopPlayback: some AppSchemaIntent](./presentationintent/stopplayback.md)
  An intent schema that stops the currently playing presentation.
- [var update: some AppSchemaIntent](./presentationintent/update.md)
  An intent schema that renames an existing presentation.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var addAudioToSlide: some AppSchemaIntent](./presentationintent/addaudiotoslide.md)
  An intent schema that adds an audio clip to a slide.
- [var addCommentToSlide: some AppSchemaIntent](./presentationintent/addcommenttoslide.md)
  An intent schema that adds a comment to a slide.
- [var addImageToSlide: some AppSchemaIntent](./presentationintent/addimagetoslide.md)
  An intent schema that adds an image to a slide.
- [var addTextBoxToSlide: some AppSchemaIntent](./presentationintent/addtextboxtoslide.md)
  An intent schema that adds a text box to a slide.
- [var addWebVideoToSlide: some AppSchemaIntent](./presentationintent/addwebvideotoslide.md)
  An intent schema that adds a web video to a slide.
- [var create: some AppSchemaIntent](./presentationintent/create.md)
  An intent schema that opens the app for composing a new presentation.
- [var createSlide: some AppSchemaIntent](./presentationintent/createslide.md)
  An intent schema that creates a new slide in a presentation document.
- [var deleteSlide: some AppSchemaIntent](./presentationintent/deleteslide.md)
  An intent schema that deletes slides in a presentation.
- [var open: some AppSchemaIntent](./presentationintent/open.md)
  An intent schema that opens the app into an existing presentation.
- [var openSlide: some AppSchemaIntent](./presentationintent/openslide.md)
  An intent schema that opens a slide.
- [var setSlideTitle: some AppSchemaIntent](./presentationintent/setslidetitle.md)
  An intent schema that sets the title of the slide.
- [var startPlayback: some AppSchemaIntent](./presentationintent/startplayback.md)
  An intent schema that plays the presentation from the start or selected slide.
- [var stopPlayback: some AppSchemaIntent](./presentationintent/stopplayback.md)
  An intent schema that stops the currently playing presentation.
- [var update: some AppSchemaIntent](./presentationintent/update.md)
  An intent schema that renames an existing presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/presentationintent)*