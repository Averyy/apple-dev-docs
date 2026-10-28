# behaviorPeriodicWithDelay:

**Framework**: Symbols  
**Kind**: method  
**Role**: Type Method

Creates and returns a repeat behavior with a preferred repeat delay using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.

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
+ (instancetype) behaviorPeriodicWithDelay:(double) delay;
```

## Return Value

A new behavior that prefers to repeat indefinitely with a specified delay using periodic animations.

## Parameters

- `delay`: The preferred delay between repetitions, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboleffectoptionsrepeatbehavior/behaviorperiodicwithdelay:)*