# item

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `whiteboard` domain and its content matches the `item` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .whiteboard.item)` Swift macro.

The following example shows an app entity that conforms to the `item` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `whiteboard_item` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .whiteboard.item)
struct CanvasItemEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more item entities, unless you provide another.
    static let defaultQuery = CanvasItemEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the item entity.
    let id: <#Identifiable.ID#>

    var type: <#CanvasItemType#>

    var label: String?

    var x: Double

    var y: Double

    var width: Double?

    var height: Double?

    /// The details the system shows to identify the item entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more item entities by their identifiers.
    struct CanvasItemEntityQuery: EntityQuery {
        func entities(for identifiers: [CanvasItemEntity.ID]) async throws -> [CanvasItemEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the item entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `type` | `@AppEnum(schema: .whiteboard.itemType)` | Your app | Item Type `CanvasItemType` is a placeholder name for a type that conforms to the [`itemType`](../whiteboardenum/itemtype.md) enum schema, which your app defines and implements. |
| `label` | `String?` | Swift | Label |
| `x` | `Double` | Swift | X Position |
| `y` | `Double` | Swift | Y Position |
| `width` | `Double?` | Swift | Width |
| `height` | `Double?` | Swift | Height |

## See Also

### Content and parameter types
- [var board: some AppSchemaEntity](./board.md)
  An entity schema for a board.
- [AppSchema.WhiteboardEntity](../whiteboardentity.md)
  Identifies entity schemas in the whiteboard domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardentity/item)*