# makePlayer(with:)

**Framework**: Core Haptics  
**Kind**: method  
**Role**: Instance Method

Creates a standard haptic pattern player from a haptic pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makePlayer(with pattern: CHHapticPattern) throws -> any CHHapticPatternPlayer
```

```objc
- (id<CHHapticPatternPlayer>) createPlayerWithPattern:(CHHapticPattern *) pattern error:(NSError **) outError;
```

## Mentions

- [Playing a single-tap haptic pattern](../playing-a-single-tap-haptic-pattern.md)
- [Preparing your app to play haptics](../preparing-your-app-to-play-haptics.md)

#### Return Value

A new pattern player instance.

## Parameters

- `pattern`: The haptic pattern you’d like the player to play.

## See Also

### Creating Haptic Pattern Players
- [func makeAdvancedPlayer(with: CHHapticPattern) throws -> any CHHapticAdvancedPatternPlayer](./makeadvancedplayer%28with%29.md)
  Creates an advanced haptic pattern player from a haptic pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/makeplayer(with:))*