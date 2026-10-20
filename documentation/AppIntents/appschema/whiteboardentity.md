# AppSchema.WhiteboardEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the whiteboard domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol WhiteboardEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var board: some AppSchemaEntity](./whiteboardentity/board.md)
  An entity schema for a board.
- [var item: some AppSchemaEntity](./whiteboardentity/item.md)
  An entity schema for an item.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var board: some AppSchemaEntity](./whiteboardentity/board.md)
  An entity schema for a board.
- [var item: some AppSchemaEntity](./whiteboardentity/item.md)
  An entity schema for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardentity)*