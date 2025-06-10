# relativeFontChange

**Framework**: App Intents  
**Kind**: property

The relative change of the font for rendering a book.

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
var relativeFontChange: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.books.relativeFontChange` schema:

```swift
@AssistantEnum(schema: .books.relativeFontChange)
enum BookRelativeFontChange: AppEnum {
    case increase
    case decrease

    static var caseDisplayRepresentations: [BookRelativeFontChange: AppIntents.DisplayRepresentation] = [
        .increase: "Increase",
        .decrease: "Decrease",
    ]
}
```

For more information about the `.books` app intent domain, see [`Making ebook actions available to Siri and Apple Intelligence`](making-ebook-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschema/enumschema/relativefontchange)*