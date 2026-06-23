# board

**Framework**: App Intents  
**Kind**: property

An entity schema for a board.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var board: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `whiteboard` domain and its content matches the `board` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .whiteboard.board)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `board` schema:

```swift
@AppEntity(schema: .whiteboard.board)
struct CanvasEntity {
    // MARK: Static

    static let defaultQuery = CanvasEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String
    var creationDate: Date
    var lastModificationDate: Date

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct CanvasEntityQuery: EntityQuery {
        func entities(for identifiers: [CanvasEntity.ID]) async throws -> [CanvasEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var item: some AppSchemaEntity](appschema/whiteboardentity/item.md)
  An entity schema for an item.
- [AppSchema.WhiteboardEntity](appschema/whiteboardentity.md)
  Identifies entity schemas in the whiteboard domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardentity/board)*