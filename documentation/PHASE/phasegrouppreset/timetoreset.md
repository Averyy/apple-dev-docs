# timeToReset

**Framework**: PHASE  
**Kind**: property

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

#### Discussion

This property determines the speed of deactivation when the app calls [`deactivate()`](phasegrouppreset/deactivate().md). The framework scales the value by [`unitsPerSecond`](phaseengine/unitspersecond.md).

## See Also

- [var timeToTarget: Double](phasegrouppreset/timetotarget.md)
  A duration in which the engine fades the settings from their original value to their new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/timetoreset)*