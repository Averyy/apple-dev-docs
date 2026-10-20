# AssistantSchemas.WordProcessorIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Assistant schema conformance for app intents that offer word processing functionality.

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
protocol WordProcessorIntent : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var addAudioToPage: some AssistantSchemas.Intent](./wordprocessorintent/addaudiotopage.md)
  The app intent conforms to the schema for adding audio to a page in a text document.
- [var addImageToPage: some AssistantSchemas.Intent](./wordprocessorintent/addimagetopage.md)
  The app intent conforms to the schema for adding an image to a page in a text document.
- [var addTextBoxToPage: some AssistantSchemas.Intent](./wordprocessorintent/addtextboxtopage.md)
  The app intent conforms to the schema for adding a text box to a page in a text document.
- [var addVideoToPage: some AssistantSchemas.Intent](./wordprocessorintent/addvideotopage.md)
  The app intent conforms to the schema for adding a video to a page in a text document.
- [var addWebVideoToPage: some AssistantSchemas.Intent](./wordprocessorintent/addwebvideotopage.md)
  The app intent conforms to the schema for adding a web video to a page in a text document.
- [var create: some AssistantSchemas.Intent](./wordprocessorintent/create.md)
  The app intent conforms to the schema for creating a text document.
- [var createPage: some AssistantSchemas.Intent](./wordprocessorintent/createpage.md)
  The app intent conforms to the schema for creating a page in a text document.
- [var open: some AssistantSchemas.Intent](./wordprocessorintent/open.md)
  The app intent conforms to the schema for opening a text document.
- [var openPage: some AssistantSchemas.Intent](./wordprocessorintent/openpage.md)
  The app intent conforms to the schema for opening a page in a text document.

## Relationships

### Inherits From
- [AssistantSchemas.Model](./model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](../assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](./intentschema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/wordprocessorintent)*