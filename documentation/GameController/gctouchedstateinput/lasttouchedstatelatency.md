# lastTouchedStateLatency

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time in seconds between the last touch state change and the current time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastTouchedStateLatency: TimeInterval { get }
```

#### Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event.

## See Also

- [var isTouched: Bool](gctouchedstateinput/istouched.md)
  A Boolean value that indicates whether the user touches the button.
- [var lastTouchedStateTimestamp: TimeInterval](gctouchedstateinput/lasttouchedstatetimestamp.md)
  The time of the most recent touch state change.
- [var touchedDidChangeHandler: ((any GCPhysicalInputElement, any GCTouchedStateInput, Bool) -> Void)?](gctouchedstateinput/toucheddidchangehandler.md)
  A block that the element calls when its touch value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gctouchedstateinput/lasttouchedstatelatency)*