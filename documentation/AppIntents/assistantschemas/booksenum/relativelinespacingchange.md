# relativeLineSpacingChange

**Framework**: App Intents  
**Kind**: property

The relative change in line spacing for rendering a book.

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
var relativeLineSpacingChange: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.books.relativeLineSpacingChange` schema:

```swift
@AppEnum(schema: .books.relativeLineSpacingChange)
enum BookRelativeLineSpacingChange: AppEnum {
    case `default`

    static var caseDisplayRepresentations: [BookRelativeLineSpacingChange: AppIntents.DisplayRepresentation] = [
        .`default`: "Default"
    ]
}
```

For more information about the `.books` app intent domain, see [`Books`](app-schema-domain-books.md). For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksenum/relativelinespacingchange)*