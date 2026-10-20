# GKGameActivity.State

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The state of a game activity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum State
```

```c
enum GKGameActivityState : NSUInteger;
```

## Topics

### Enumeration Cases
- [GKGameActivity.State.active](./state-swift.enum/active.md)
  The game activity is active.
- [GKGameActivity.State.ended](./state-swift.enum/ended.md)
  The game activity has ended. This is a terminal state.
- [GKGameActivity.State.initialized](./state-swift.enum/initialized.md)
  The game activity is initialized but has not started.
- [GKGameActivity.State.paused](./state-swift.enum/paused.md)
  The game activity is paused.
### Initializers
- [init?(rawValue: UInt)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the activity state
- [var state: GKGameActivity.State](./state-swift.property.md)
  The state of the game activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/state-swift.enum)*