# AssistantSchemas.WordProcessorIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer word processing functionality.

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
protocol WordProcessorIntent : AssistantSchemas.Model
```

## Mentions

- [Making word processor actions available to Siri and Apple Intelligence](making-word-processor-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var addAudioToPage: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/addaudiotopage.md)
  The app intent conforms to the schema for adding audio to a page in a text document.
- [var addImageToPage: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/addimagetopage.md)
  The app intent conforms to the schema for adding an image to a page in a text document.
- [var addTextBoxToPage: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/addtextboxtopage.md)
  The app intent conforms to the schema for adding a text box to a page in a text document.
- [var addVideoToPage: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/addvideotopage.md)
  The app intent conforms to the schema for adding a video to a page in a text document.
- [var addWebVideoToPage: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/addwebvideotopage.md)
  The app intent conforms to the schema for adding a web video to a page in a text document.
- [var create: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/create.md)
  The app intent conforms to the schema for creating a text document.
- [var createPage: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/createpage.md)
  The app intent conforms to the schema for creating a page in a text document.
- [var open: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/open.md)
  The app intent conforms to the schema for opening a text document.
- [var openPage: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/openpage.md)
  The app intent conforms to the schema for opening a page in a text document.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making word processor actions available to Siri and Apple Intelligence](making-word-processor-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities that make your app’s word processor functionality available to Siri and Apple Intelligence.
- [AssistantSchemas.WordProcessorEntity](assistantschemas/wordprocessorentity.md)
  Assistant schema conformance for app entities that describe text documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/wordprocessorintent)*