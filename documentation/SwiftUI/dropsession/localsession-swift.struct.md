# DropSession.LocalSession

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Describes the session originated within the app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct LocalSession
```

## Topics

### Instance Methods
- [func draggedItemIDs<ItemID>(for: ItemID.Type) -> [ItemID]](./localsession-swift.struct/draggeditemids%28for%29.md)
  Provides an array of identifiers of the currently dragged items if available.

## See Also

### Getting drop session details
- [var id: DropSession.ID](./id-swift.property.md)
  The unique identifier of the drop session.
- [DropSession.ID](./id-swift.struct.md)
  The identifier of a drag session.
- [var localSession: DropSession.LocalSession?](./localsession-swift.property.md)
  Provides additional information about a session if it originated within the app.
- [var phase: DropSession.Phase](./phase-swift.property.md)
  The phase of the current drop session.
- [DropSession.Phase](./phase-swift.enum.md)
  The phase of the current drop session.
- [var suggestedOperations: DropOperation.Set](./suggestedoperations.md)
  Operations suggested by the drag source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/localsession-swift.struct)*