# page

**Framework**: App Intents  
**Kind**: property

An entity schema for a page.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var page: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reader` domain and its content matches the `page` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .reader.page)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `page` schema:

```swift
@AppEntity(schema: .reader.page)
struct ReaderPageEntity {
    // MARK: Static

    static let defaultQuery = ReaderPageEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var label: String

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct ReaderPageEntityQuery: EntityQuery {
        func entities(for identifiers: [ReaderPageEntity.ID]) async throws -> [ReaderPageEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var document: some AppSchemaEntity](appschema/readerentity/document.md)
  An entity schema for a document.
- [AppSchema.ReaderEntity](appschema/readerentity.md)
  Identifies entity schemas in the reader domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/readerentity/page)*