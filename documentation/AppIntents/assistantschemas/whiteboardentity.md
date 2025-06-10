# AssistantSchemas.WhiteboardEntity

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app entities that describe data for whiteboard functionality.

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
protocol WhiteboardEntity : AssistantSchemas.Model
```

## Mentions

- [Making whiteboard actions available to Siri and Apple Intelligence](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var board: some AssistantSchemas.Entity](assistantschemas/whiteboardentity/board.md)
  The app entity describes a whiteboard canvas.
- [var item: some AssistantSchemas.Entity](assistantschemas/whiteboardentity/item.md)
  The app entity describes an item on a whiteboard canvas.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.EntitySchema](assistantschema/entityschema.md)
- [AssistantSchemas.EntitySchema](assistantschemas/entityschema.md)

## See Also

- [Making whiteboard actions available to Siri and Apple Intelligence](making-whiteboard-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities that make your app’s whiteboard functionality available to Siri and Apple Intelligence.
- [AssistantSchemas.WhiteboardIntent](assistantschemas/whiteboardintent.md)
  Assistant schema conformance for app intents that offer whiteboard functionality.
- [AssistantSchemas.WhiteboardEnum](assistantschemas/whiteboardenum.md)
  Assistant schema conformance for whiteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/whiteboardentity)*