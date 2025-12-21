# item

**Framework**: App Intents  
**Kind**: property

The app entity describes an item on a whiteboard canvas.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var item: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.whiteboard.item` schema:

```swift
@AppEntity(schema: .whiteboard.item)
struct CanvasItemEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [CanvasItemEntity.ID]) async throws -> [CanvasItemEntity] { [] }
        func entities(matching string: String) async throws -> [CanvasItemEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Canvas Item" }

    let id = UUID()

    @Property
    var type: CanvasItemType

    @Property
    var label: String?

    @Property
    var x: Double

    @Property
    var y: Double

    @Property
    var width: Double?

    @Property
    var height: Double?
}
```

For more information about the `.whiteboard` app intent domain, see [`Making whiteboard actions available to Siri and Apple Intelligence`](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/whiteboardentity/item)*