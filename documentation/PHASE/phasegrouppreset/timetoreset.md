# timeToReset

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A duration in which the framework restores the group’s original state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var timeToReset: Double { get }
```

```objc
@property (nonatomic, readonly) double timeToReset;
```

## Discussion

This property determines the speed of deactivation when the app calls [`deactivate()`](./deactivate%28%29.md). The framework scales the value by [`unitsPerSecond`](../phaseengine/unitspersecond.md).

## See Also

### Fading Between Settings
- [var timeToTarget: Double](./timetotarget.md)
  A duration in which the engine fades the settings from their original value to their new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/timetoreset)*