# makeAdvancedPlayer(with:)

**Framework**: Core Haptics  
**Kind**: method

Creates an advanced haptic pattern player from a haptic pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeAdvancedPlayer(with pattern: CHHapticPattern) throws -> any CHHapticAdvancedPatternPlayer
```

#### Return Value

A new advanced pattern player instance.

## Parameters

- `pattern`: The haptic pattern you’d like the player to play.

## See Also

- [func makePlayer(with: CHHapticPattern) throws -> any CHHapticPatternPlayer](chhapticengine/makeplayer(with:).md)
  Creates a standard haptic pattern player from a haptic pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/makeadvancedplayer(with:))*