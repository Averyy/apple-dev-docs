# createPage

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for creating a page in a text document.

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
var createPage: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.wordProcessor.createPage` schema:

```swift
@AssistantIntent(schema: .wordProcessor.createPage)
struct CreateWordProcessorPageIntent: AppIntent {
    @Parameter
    var target: WordProcessorDocumentEntity

    @Parameter
    var template: String?

    func perform() async throws -> some ReturnsValue<WordProcessorPageEntity> {
        .result(value: WordProcessorPageEntity())
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/intentschema/createpage)*