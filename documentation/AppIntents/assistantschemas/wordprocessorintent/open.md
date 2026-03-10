# open

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for opening a text document.

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
var open: some AssistantSchemas.Intent { get }
```

## Mentions

- [Making word processor actions available to Siri and Apple Intelligence](making-word-processor-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.wordProcessor.open` schema:

```swift
@AppIntent(schema: .wordProcessor.open)
struct OpenWordProcessorDocumentIntent: OpenIntent {
    @Parameter
    var target: WordProcessorDocumentEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

## See Also

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
- [var openPage: some AssistantSchemas.Intent](assistantschemas/wordprocessorintent/openpage.md)
  The app intent conforms to the schema for opening a page in a text document.
- [AssistantSchemas.WordProcessorIntent](assistantschemas/wordprocessorintent.md)
  Assistant schema conformance for app intents that offer word processing functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/wordprocessorintent/open)*