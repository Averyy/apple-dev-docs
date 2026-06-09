# readingListItem

**Framework**: App Intents  
**Kind**: property

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst ?+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
var readingListItem: some AssistantSchemas.Entity { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.

The following example shows an app entity that conforms to the `browser.readingListItem` schema:

```swift
@AppEntity(schema: .browser.readingListItem)
struct ReadingListItemEntity {
    struct ReadingListItemEntityQuery: EntityQuery {
        func entities(for identifiers: [ReadingListItemEntity.ID]) async throws -> [ReadingListItemEntity] {
            <#code#>
        }
    }
    static let defaultQuery = ReadingListItemEntityQuery()

    let displayRepresentation: DisplayRepresentation = {
        <#DisplayRepresentation#>
    }

    let id: <#Identifiable.ID#>
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/browserentity/readinglistitem)*