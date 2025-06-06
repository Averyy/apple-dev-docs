# value

**Framework**: GameplayKit  
**Kind**: property  
**Required**: Yes

A value assigned and read by GameplayKit to rate the desirability of a move in your game.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var value: Int { get set }
```

#### Discussion

Your game does not assign to or read from this property directly. Instead, when you adopt the [`GKGameModelUpdate`](gkgamemodelupdate.md) protocol, you simply provide a read/write implementation of this property. When you use the [`GKMinmaxStrategist`](gkminmaxstrategist.md) class to select optimal moves during gameplay, GameplayKit assigns values to this property in order to rate the desirability of each move to a given player.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodelupdate/value)*