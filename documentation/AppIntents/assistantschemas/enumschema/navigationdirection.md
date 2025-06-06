# navigationDirection

**Framework**: App Intents  
**Kind**: property

The navigation direction of a book.

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
var navigationDirection: some AssistantSchemas.Enum { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app enum implementation.

For more information about the `.books` app intent domain, see [`Making ebook actions available to Siri and Apple Intelligence`](making-ebook-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app enum that conforms to the `.books.navigationDirection` schema:

```swift
@AssistantEnum(schema: .books.navigationDirection)
enum BookNavigationDirection: AppEnum {
    case next
    case previous

    static var caseDisplayRepresentations: [BookNavigationDirection: AppIntents.DisplayRepresentation] = [
        .next: "Next",
        .previous: "Previous",
    ]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/enumschema/navigationdirection)*