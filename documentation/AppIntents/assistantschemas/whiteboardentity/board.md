# board

**Framework**: App Intents  
**Kind**: property

The app entity describes a whiteboard canvas.

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
var board: some AssistantSchemas.Entity { get }
```

## Mentions

- [Making whiteboard actions available to Siri and Apple Intelligence](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For more information about the `.whiteboard` app intent domain, see [`Making whiteboard actions available to Siri and Apple Intelligence`](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app entity that conforms to the `.whiteboard.board` schema:

```swift
@AssistantEntity(schema: .whiteboard.board)
struct CanvasEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [CanvasEntity.ID]) async throws -> [CanvasEntity] { [] }
        func entities(matching string: String) async throws -> [CanvasEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Canvas" }

    let id = UUID()

    @Property
    var title: String

    @Property
    var creationDate: Date

    @Property
    var lastModificationDate: Date
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/whiteboardentity/board)*