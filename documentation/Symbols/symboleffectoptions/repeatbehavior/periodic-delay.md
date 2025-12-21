# periodic(_:delay:)

**Framework**: Symbols  
**Kind**: method

A repeat behavior with a preferred play count and delay using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func periodic(_ count: Int? = nil, delay: Double? = nil) -> SymbolEffectOptions.RepeatBehavior
```

#### Return Value

A new behavior with the preferred play count and delay using periodic animations.

## Parameters

- `count`: The preferred number of times to play the   effect, or nil to request it play indefinitely. Very   large or small values may be clamped.
- `delay`: The preferred delay between repetitions,   in seconds, or nil to request the default delay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/symboleffectoptions/repeatbehavior/periodic(_:delay:))*