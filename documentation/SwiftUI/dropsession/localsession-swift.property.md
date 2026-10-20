# localSession

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

Provides additional information about a session if it originated within the app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var localSession: DropSession.LocalSession?
```

#### Discussion

This property is set to `nil` if drag originated outside the app.

## See Also

### Getting drop session details
- [var id: DropSession.ID](./id-swift.property.md)
  The unique identifier of the drop session.
- [DropSession.ID](./id-swift.struct.md)
  The identifier of a drag session.
- [DropSession.LocalSession](./localsession-swift.struct.md)
  Describes the session originated within the app.
- [var phase: DropSession.Phase](./phase-swift.property.md)
  The phase of the current drop session.
- [DropSession.Phase](./phase-swift.enum.md)
  The phase of the current drop session.
- [var suggestedOperations: DropOperation.Set](./suggestedoperations.md)
  Operations suggested by the drag source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/localsession-swift.property)*