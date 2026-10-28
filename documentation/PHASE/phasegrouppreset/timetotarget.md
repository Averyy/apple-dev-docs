# timeToTarget

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A duration in which the engine fades the settings from their original value to their new value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var timeToTarget: Double { get }
```

```objc
@property (nonatomic, readonly) double timeToTarget;
```

## Discussion

This property determines the speed of activation when the app calls [`activate()`](./activate%28%29.md). The framework scales the value by [`unitsPerSecond`](../phaseengine/unitspersecond.md).

## See Also

### Fading Between Settings
- [var timeToReset: Double](./timetoreset.md)
  A duration in which the framework restores the group’s original state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/timetotarget)*