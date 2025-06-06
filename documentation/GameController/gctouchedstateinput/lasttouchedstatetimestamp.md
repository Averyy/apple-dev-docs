# lastTouchedStateTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time of the most recent touch state change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastTouchedStateTimestamp: TimeInterval { get }
```

#### Discussion

This property isn’t a specific date and time. To determine the time between changes, subtract a previous value from the current value.

## See Also

- [var isTouched: Bool](gctouchedstateinput/istouched.md)
  A Boolean value that indicates whether the user touches the button.
- [var lastTouchedStateLatency: TimeInterval](gctouchedstateinput/lasttouchedstatelatency.md)
  The time in seconds between the last touch state change and the current time.
- [var touchedDidChangeHandler: ((any GCPhysicalInputElement, any GCTouchedStateInput, Bool) -> Void)?](gctouchedstateinput/toucheddidchangehandler.md)
  A block that the element calls when its touch value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gctouchedstateinput/lasttouchedstatetimestamp)*