# behaviorPeriodicWithCount:

**Framework**: Symbols  
**Kind**: method  
**Role**: Type Method

Creates and returns a repeat behavior with a preferred play count using periodic animations. Periodic animations play the effect at regular intervals starting and stopping each time.

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
+ (instancetype) behaviorPeriodicWithCount:(NSInteger) count;
```

## Return Value

A new behavior with the preferred play count using periodic animations.

## Parameters

- `count`: The preferred number of times to play the effect. Very large or small values may be clamped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboleffectoptionsrepeatbehavior/behaviorperiodicwithcount:)*