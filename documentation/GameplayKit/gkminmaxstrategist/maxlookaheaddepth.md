# maxLookAheadDepth

**Framework**: GameplayKit  
**Kind**: property

The number of future turns for the strategist to consider when planning moves.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var maxLookAheadDepth: Int { get set }
```

#### Discussion

The strategist works by recursively forming and examining a decision tree of possible future game model states and the moves leading to each. This property determines the number of future turns to consider and the depth of the resulting decision tree. Greater lookahead depth results in stronger play by a strategist-controlled player, but at a cost of increased computation time and memory usage.

For example, at the beginning of a Tic-Tac-Toe game, there are nine possible moves (one for each spot on the board), leading to nine possible states. After a move is made, the number of possible moves reduces by one. If this property’s value is 1, the strategist examines only those nine model states. If the [`maxLookAheadDepth`](gkminmaxstrategist/maxlookaheaddepth.md) value is 2, the strategist also examines the eight possible model states resulting from the next turn, following each of nine possible states for the current turn, for a total of 72 states. Continuing to add depth exponentially increases the search complexity. Tic-Tac-Toe requires three aligned moves to win, so a strategist that can plan its next three moves (and the two intervening moves of its opponent, for a total lookahead depth of five) is potentially capable of perfect play.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkminmaxstrategist/maxlookaheaddepth)*