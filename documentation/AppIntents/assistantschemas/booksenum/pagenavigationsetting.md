# pageNavigationSetting

**Framework**: App Intents  
**Kind**: property

Navigation settings for rendering a book.

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
var pageNavigationSetting: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.books.pageNavigationSetting` schema:

```swift
@AppEnum(schema: .books.pageNavigationSetting)
enum BookPageNavigationSetting: AppEnum {
    case continuousScroll
    case pageTurning

    static var caseDisplayRepresentations: [BookPageNavigationSetting: AppIntents.DisplayRepresentation] = [
        .continuousScroll: "Continuous Scroll",
        .pageTurning: "Page Turning",
    ]
}
```

For more information about the `.books` app intent domain, see [`Books`](app-schema-domain-books.md). For general information about app intent domains, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksenum/pagenavigationsetting)*