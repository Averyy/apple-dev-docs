# board

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a board.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var board: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `whiteboard` domain and its content matches the `board` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .whiteboard.board)` Swift macro.

The following example shows an app entity that conforms to the `board` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `whiteboard_board` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .whiteboard.board)
struct CanvasEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more board entities, unless you provide another.
    static let defaultQuery = CanvasEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the board entity.
    let id: <#Identifiable.ID#>

    var title: String

    var creationDate: Date

    var lastModificationDate: Date

    /// The details the system shows to identify the board entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more board entities by their identifiers.
    struct CanvasEntityQuery: EntityQuery {
        func entities(for identifiers: [CanvasEntity.ID]) async throws -> [CanvasEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the board entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | Name |
| `creationDate` | `Date` | Foundation | Creation Date |
| `lastModificationDate` | `Date` | Foundation | Last Edited |

## See Also

### Content and parameter types
- [var item: some AppSchemaEntity](./item.md)
  An entity schema for an item.
- [AppSchema.WhiteboardEntity](../whiteboardentity.md)
  Identifies entity schemas in the whiteboard domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardentity/board)*