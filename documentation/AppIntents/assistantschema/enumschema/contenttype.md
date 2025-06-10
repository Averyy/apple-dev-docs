# contentType

**Framework**: App Intents  
**Kind**: property

The content type.

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
var contentType: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.books.contentType` schema:

```swift
@AssistantEnum(schema: .books.contentType)
enum BookContentType: AppEnum {
    case book
    case pdf

    static var caseDisplayRepresentations: [BookContentType: AppIntents.DisplayRepresentation] = [
        .book: "Book",
        .pdf: "PDF",
    ]
}
 For more information about the `.books` app intent domain,
 see <doc:Making-ebook-actions-available-to-siri-and-apple-intelligence>.
 For general information about app intent domains, see <doc:Integrating-actions-with-siri-and-apple-intelligence>.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschema/enumschema/contenttype)*