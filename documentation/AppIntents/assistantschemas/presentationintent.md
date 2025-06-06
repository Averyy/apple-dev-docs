# AssistantSchemas.PresentationIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer presentation functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol PresentationIntent : AssistantSchemas.Model
```

## Mentions

- [Making presentation actions available to Siri and Apple Intelligence](making-presentation-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var addAudioToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addaudiotoslide.md)
  The app intent conforms to the schema for adding audio to a slide.
- [var addCommentToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addcommenttoslide.md)
  The app intent conforms to the schema for adding a comment to a slide.
- [var addImageToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addimagetoslide.md)
  The app intent conforms to the schema for adding an image to a slide.
- [var addTextBoxToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addtextboxtoslide.md)
  The app intent conforms to the schema for adding a text box to a slide.
- [var addVideoToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addvideotoslide.md)
  The app intent conforms to the schema for adding a video to a slide.
- [var addWebVideoToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addwebvideotoslide.md)
  The app intent conforms to the schema for adding a video from the internet to a slide.
- [var create: some AssistantSchemas.Intent](assistantschemas/presentationintent/create.md)
  The app intent conforms to the schema for creating a presentation.
- [var createSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/createslide.md)
  The app intent conforms to the schema for creating a new slide for a presentation.
- [var deleteSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/deleteslide.md)
  The app intent conforms to the schema for deleting a slide.
- [var open: some AssistantSchemas.Intent](assistantschemas/presentationintent/open.md)
  The app intent conforms to the schema for opening a presentation.
- [var openSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/openslide.md)
  The app intent conforms to the schema for opening a slide of a presentation.
- [var setSlideTitle: some AssistantSchemas.Intent](assistantschemas/presentationintent/setslidetitle.md)
  The app intent conforms to the schema for setting the title of a slide.
- [var startPlayback: some AssistantSchemas.Intent](assistantschemas/presentationintent/startplayback.md)
  The app intent conforms to the schema for starting a presentation.
- [var stopPlayback: some AssistantSchemas.Intent](assistantschemas/presentationintent/stopplayback.md)
  The app intent conforms to the schema for stopping a presentation.
- [var update: some AssistantSchemas.Intent](assistantschemas/presentationintent/update.md)
  The app intent conforms to the schema for updating the name of a presentation.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making presentation actions available to Siri and Apple Intelligence](making-presentation-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s presentation functionality with Siri and Apple Intelligence.
- [AssistantSchemas.PresentationEntity](assistantschemas/presentationentity.md)
  Assistant schema conformance for app entities that describe presentation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/presentationintent)*