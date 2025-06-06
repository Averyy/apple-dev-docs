# gameModel

**Framework**: GameplayKit  
**Kind**: property  
**Required**: Yes

The model representing the current state of the game.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var gameModel: (any GKGameModel)? { get set }
```

#### Discussion

A game model—an instance of one of your custom classes implementing the [`GKGameModel`](gkgamemodel.md) protocol—contains all the information necessary to describe a distinct state of your game. For example, the game model class for a Tic-Tac-Toe game would encode the locations of X and O marks currently on the board and which player’s turn is next. The strategist works from the current game model when planning moves.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstrategist/gamemodel)*