# Making whiteboard actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities that make your app’s whiteboard functionality available to Siri and Apple Intelligence.

#### Overview

To integrate your app’s whiteboard capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent and app entity implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows someone to open a whiteboard, use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.whiteboard` domain and the [`createBoard`](assistantschemas/whiteboardintent/createboard.md) schema:

```swift
@AppIntent(schema: .whiteboard.createBoard)
struct CreateWhiteboardIntent: AppIntent {
    public var title: String?

    func perform() async throws -> some ReturnsValue<WhiteboardBoardEntity> {
        .result(value: WhiteboardBoardEntity())
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.whiteboard` domain, see [`AssistantSchemas.WhiteboardIntent`](assistantschemas/whiteboardintent.md).

##### Make Sure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `WhiteboardEntity`. The following code snippet shows how the `WhiteboardEntity` implementation uses the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro:

```swift
@AppEntity(schema: .whiteboard.board)
struct WhiteboardBoardEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [WhiteboardBoardEntity.ID]) async throws -> [WhiteboardBoardEntity] { [] }
        func entities(matching string: String) async throws -> [WhiteboardBoardEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Provide a display representation." }

    let id = UUID()

    var title: String
    var creationDate: Date
    var lastModificationDate: Date
}
```

The assistant schema for the `WhiteboardBoardEntity` consists of the `.whiteboard` domain and the [`board`](assistantschemas/whiteboardentity/board.md) schema.

For a list of available app entity schemas in the `.whiteboard` domain, see [`AssistantSchemas.WhiteboardEntity`](assistantschemas/whiteboardentity.md).

##### Make Sure Your Enumeration Meets Requirements

To make sure Siri and Apple Intelligence understand custom static types for your intent parameters, annotate app enumerations with the [`AssistantEnum(schema:)`](assistantenum(schema:).md) macro. Then, pass the `.whiteboard` domain and a schema to it. The following example uses the [`color`](assistantschemas/whiteboardenum/color.md) schema:

```swift
@AppEnum(schema: .whiteboard.color)
enum WhiteboardColor: String, AppEnum {
    case white
    case black
    case grey
    case green
    case red
    case blue
    case yourCustomAppColor

    static var caseDisplayRepresentations: [WhiteboardColor: AppIntents.DisplayRepresentation] = [:]

}
```

For a list of available app enums in the `.whiteboard` domain, refer to [`AssistantSchemas.WhiteboardEnum`](assistantschemas/whiteboardenum.md).

## See Also

- [AssistantSchemas.WhiteboardIntent](assistantschemas/whiteboardintent.md)
  Assistant schema conformance for app intents that offer whiteboard functionality.
- [AssistantSchemas.WhiteboardEntity](assistantschemas/whiteboardentity.md)
  Assistant schema conformance for app entities that describe data for whiteboard functionality.
- [AssistantSchemas.WhiteboardEnum](assistantschemas/whiteboardenum.md)
  Assistant schema conformance for whiteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-whiteboard-actions-available-to-siri-and-apple-intelligence)*