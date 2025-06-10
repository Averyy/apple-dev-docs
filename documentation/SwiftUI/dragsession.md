# DragSession

**Framework**: SwiftUI  
**Kind**: struct

Describes the ongoing dragging session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DragSession
```

## Topics

### Structures
- [DragSession.ID](dragsession/id-swift.struct.md)
  The identifier of a drag session.
### Instance Properties
- [var draggedItemIndex: Int](dragsession/draggeditemindex.md)
  The index of the dragged item under the cursor.
- [var id: DragSession.ID](dragsession/id-swift.property.md)
  The identifier of the drag session.
- [var phase: DragSession.Phase](dragsession/phase-swift.property.md)
  The current phase of the drag session.
### Instance Methods
- [func draggedItemIDs<ItemID>(for: ItemID.Type) -> [ItemID]](dragsession/draggeditemids(for:).md)
  Provides an array of identifiers of the currently dragged items in a case when the items conform to the `Identifiable` protocol, or identifiers were provided to SwiftUI separately.
### Enumerations
- [DragSession.Phase](dragsession/phase-swift.enum.md)
  The phase of the current drag session

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct DropSession](dropsession.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragsession)*