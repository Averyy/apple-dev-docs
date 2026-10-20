# tabletopGame(_:parent:automaticUpdate:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a tabletop game to a view.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func tabletopGame(_ game: TabletopGame, parent: Entity, automaticUpdate: Bool = true) -> some View
```

## See Also

### Creating a tabletop game
- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool, interaction: (TabletopInteraction.Value) -> any TabletopInteraction.Delegate) -> some View](./tabletopgame%28_,parent,automaticupdate,interaction%29.md)
  Supplies a closure which returns a new interaction whenever needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabletopgame(_:parent:automaticupdate:))*