# SymbolEffectOptions.RepeatBehavior

**Framework**: Symbols  
**Kind**: struct

The behavior to use when requesting any repetition on a `SymbolEffect`.

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
struct RepeatBehavior
```

## Topics

### Type Properties
- [static var continuous: SymbolEffectOptions.RepeatBehavior](symboleffectoptions/repeatbehavior/continuous.md)
  A repeat behavior that prefers to repeat indefinitely, using continuous animations if available. Continuous animations have an intro, a body that runs as long as the effect is enabled, and an outro. If available these animations provide a smoother animation when an effect repeats indefinitely.
- [static var periodic: SymbolEffectOptions.RepeatBehavior](symboleffectoptions/repeatbehavior/periodic.md)
  A repeat behavior that prefers to repeat indefinitely using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.
### Type Methods
- [static func periodic(Int?, delay: Double?) -> SymbolEffectOptions.RepeatBehavior](symboleffectoptions/repeatbehavior/periodic(_:delay:).md)
  A repeat behavior with a preferred play count and delay using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/symboleffectoptions/repeatbehavior)*