# NSSymbolEffectOptionsRepeatBehavior

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

The behavior of repetition to use when a symbol effect is animating.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
@interface NSSymbolEffectOptionsRepeatBehavior : NSObject
```

## Topics

### Type Methods
- [+ behaviorContinuous](./nssymboleffectoptionsrepeatbehavior/behaviorcontinuous.md)
  Creates and returns a repeat behavior that prefers to repeat indefinitely, using continuous animations if available. Continuous animations have an intro, a body that runs as long as the effect is enabled, and an outro. If available these animations provide a smoother animation when an effect repeats indefinitely.
- [+ behaviorPeriodic](./nssymboleffectoptionsrepeatbehavior/behaviorperiodic.md)
  Creates and returns a repeat behavior that prefers to repeat indefinitely using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.
- [+ behaviorPeriodicWithCount:](./nssymboleffectoptionsrepeatbehavior/behaviorperiodicwithcount_.md)
  Creates and returns a repeat behavior with a preferred play count using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.
- [+ behaviorPeriodicWithCount:delay:](./nssymboleffectoptionsrepeatbehavior/behaviorperiodicwithcount_delay_.md)
  Creates and returns a repeat behavior with a preferred play count and delay using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.
- [+ behaviorPeriodicWithDelay:](./nssymboleffectoptionsrepeatbehavior/behaviorperiodicwithdelay_.md)
  Creates and returns a repeat behavior with a preferred repeat delay using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Symbol effect options
- [NSSymbolEffectOptions](./nssymboleffectoptions.md)
  Options that configure how effects apply to symbol-based images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboleffectoptionsrepeatbehavior)*