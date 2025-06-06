# Game Model Score Limits

**Framework**: GameplayKit

Limits to values returned by the [`score(for:)`](gkgamemodel/score(for:).md) method.

#### Overview

When you evaluate the state of a game model in the [`score(for:)`](gkgamemodel/score(for:).md) method, the [`GKMinmaxStrategist`](gkminmaxstrategist.md) class weights the resulting value by search depth and performs other calculations in its process of selecting an optimal move. To prevent overflow errors in such calculations, keep scores within the range of [`GKGameModelMinScore`](gkgamemodelminscore.md) to [`GKGameModelMaxScore`](gkgamemodelmaxscore.md), inclusive.

## Topics

### Constants
- [let GKGameModelMaxScore: Int](gkgamemodelmaxscore.md)
  The maximum return value allowed for the [`score(for:)`](gkgamemodel/score(for:).md) method.
- [let GKGameModelMinScore: Int](gkgamemodelminscore.md)
  The minimum return value allowed for the [`score(for:)`](gkgamemodel/score(for:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/game-model-score-limits)*