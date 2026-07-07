# item

**Framework**: App Intents  
**Kind**: property

An entity schema for an item.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var item: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `whiteboard` domain and its content matches the `item` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .whiteboard.item)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `item` schema:

```swift
@AppEntity(schema: .whiteboard.item)
struct CanvasItemEntity {
    // MARK: Static

    static let defaultQuery = CanvasItemEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var type: <#CanvasItemType#>
    var label: String?
    var x: Double
    var y: Double
    var width: Double?
    var height: Double?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct CanvasItemEntityQuery: EntityQuery {
        func entities(for identifiers: [CanvasItemEntity.ID]) async throws -> [CanvasItemEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var board: some AppSchemaEntity](appschema/whiteboardentity/board.md)
  An entity schema for a board.
- [AppSchema.WhiteboardEntity](appschema/whiteboardentity.md)
  Identifies entity schemas in the whiteboard domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardentity/item)*