# tabletopGame(_:parent:automaticUpdate:interaction:)

**Framework**: SwiftUI  
**Kind**: method

Supplies a closure which returns a new interaction whenever needed.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func tabletopGame(_ game: TabletopGame, parent: Entity, automaticUpdate: Bool = true, interaction make: @escaping (TabletopInteraction.Value) -> any TabletopInteraction.Delegate) -> some View
```

## See Also

- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool) -> some View](view/tabletopgame(_:parent:automaticupdate:).md)
  Adds a tabletop game to a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabletopgame(_:parent:automaticupdate:interaction:))*