# stopPlayback

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for stopping a presentation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var stopPlayback: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.presentation.stopPlayback` schema:

```swift
@AppIntent(schema: .presentation.stopPlayback)
struct StopPlaybackPresentationIntent: AppIntent {
    @Parameter
    var target: PresentationSlideEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.presentation` app intent domain, see [`Making presentation actions available to Siri and Apple Intelligence`](making-presentation-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var addAudioToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addaudiotoslide.md)
  The app intent conforms to the schema for adding audio to a slide.
- [var addCommentToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addcommenttoslide.md)
  The app intent conforms to the schema for adding a comment to a slide.
- [var addImageToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addimagetoslide.md)
  The app intent conforms to the schema for adding an image to a slide.
- [var addTextBoxToSlide: some AssistantSchemas.Intent](assistantschemas/presentationintent/addtextboxtoslide.md)
  The app intent conforms to the schema for adding a text box to a slide.
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
- [var update: some AssistantSchemas.Intent](assistantschemas/presentationintent/update.md)
  The app intent conforms to the schema for updating the name of a presentation.
- [AssistantSchemas.PresentationIntent](assistantschemas/presentationintent.md)
  Assistant schema conformance for app intents that offer presentation functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/presentationintent/stopplayback)*