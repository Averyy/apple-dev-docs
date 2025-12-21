# DropSession

**Framework**: SwiftUI  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DropSession
```

## Topics

### Structures
- [DropSession.ID](dropsession/id-swift.struct.md)
  The identifier of a drag session.
- [DropSession.LocalSession](dropsession/localsession-swift.struct.md)
  Describes the session originated within the app.
### Instance Properties
- [var id: DropSession.ID](dropsession/id-swift.property.md)
  The unique identifier of the drop session.
- [var itemsCount: Int](dropsession/itemscount.md)
  Number of items for the drop.
- [var localSession: DropSession.LocalSession?](dropsession/localsession-swift.property.md)
  Provides additional information about a session if it originated within the app.
- [var location: CGPoint](dropsession/location.md)
  Location of drop in the local coordinate space
- [var phase: DropSession.Phase](dropsession/phase-swift.property.md)
  The phase of the current drop session.
- [var size: CGSize](dropsession/size.md)
  Size of the drop destination view.
- [var suggestedOperations: DropOperation.Set](dropsession/suggestedoperations.md)
  Operations suggested by the drag source.
### Enumerations
- [DropSession.Phase](dropsession/phase-swift.enum.md)
  The phase of the current drop session.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct DragSession](dragsession.md)
  Describes the ongoing dragging session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession)*