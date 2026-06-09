# DropSession.LocalSession

**Framework**: SwiftUI  
**Kind**: struct

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
- [func draggedItemIDs<ItemID>(for: ItemID.Type) -> [ItemID]](dropsession/localsession-swift.struct/draggeditemids(for:).md)
  Provides an array of identifiers of the currently dragged items if available.

## See Also

- [var id: DropSession.ID](dropsession/id-swift.property.md)
  The unique identifier of the drop session.
- [DropSession.ID](dropsession/id-swift.struct.md)
  The identifier of a drag session.
- [var localSession: DropSession.LocalSession?](dropsession/localsession-swift.property.md)
  Provides additional information about a session if it originated within the app.
- [var phase: DropSession.Phase](dropsession/phase-swift.property.md)
  The phase of the current drop session.
- [DropSession.Phase](dropsession/phase-swift.enum.md)
  The phase of the current drop session.
- [var suggestedOperations: DropOperation.Set](dropsession/suggestedoperations.md)
  Operations suggested by the drag source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/localsession-swift.struct)*