# DropSession.ID

**Framework**: SwiftUI  
**Kind**: struct

The identifier of a drag session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ID
```

## Topics

### Instance Methods
- [func matches(_:)](dropsession/id-swift.struct/matches(_:).md)
  Checks if the session value describes the same drag session as the object provided by AppKit.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var id: DropSession.ID](dropsession/id-swift.property.md)
  The unique identifier of the drop session.
- [var localSession: DropSession.LocalSession?](dropsession/localsession-swift.property.md)
  Provides additional information about a session if it originated within the app.
- [DropSession.LocalSession](dropsession/localsession-swift.struct.md)
  Describes the session originated within the app.
- [var phase: DropSession.Phase](dropsession/phase-swift.property.md)
  The phase of the current drop session.
- [DropSession.Phase](dropsession/phase-swift.enum.md)
  The phase of the current drop session.
- [var suggestedOperations: DropOperation.Set](dropsession/suggestedoperations.md)
  Operations suggested by the drag source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/id-swift.struct)*