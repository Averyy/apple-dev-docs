# tabletopGame(_:parent:automaticUpdate:interaction:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Supplies a closure which returns a new interaction whenever needed.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func tabletopGame(_ game: TabletopGame, parent: Entity, automaticUpdate: Bool = true, interaction make: @escaping (TabletopInteraction.Value) -> any TabletopInteraction.Delegate) -> some View
```

## See Also

### Creating a tabletop game
- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool) -> some View](./tabletopgame%28_,parent,automaticupdate%29.md)
  Adds a tabletop game to a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabletopgame(_:parent:automaticupdate:interaction:))*