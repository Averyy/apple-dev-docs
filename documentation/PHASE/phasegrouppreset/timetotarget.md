# timeToTarget

**Framework**: PHASE  
**Kind**: property

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

#### Discussion

This property determines the speed of activation when the app calls [`activate()`](phasegrouppreset/activate().md). The framework scales the value by [`unitsPerSecond`](phaseengine/unitspersecond.md).

## See Also

- [var timeToReset: Double](phasegrouppreset/timetoreset.md)
  A duration in which the framework restores the group’s original state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/timetotarget)*