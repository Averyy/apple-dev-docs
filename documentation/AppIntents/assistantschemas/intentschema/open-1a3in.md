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

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.wordProcessor.open` schema:

```swift
@AssistantIntent(schema: .wordProcessor.open)
struct OpenWordProcessorDocumentIntent: OpenIntent {
    @Parameter
    var target: WordProcessorDocumentEntity

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/intentschema/open-1a3in)*