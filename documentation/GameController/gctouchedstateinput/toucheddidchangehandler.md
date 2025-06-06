# touchedDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

A block that the element calls when its touch value changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var touchedDidChangeHandler: ((any GCPhysicalInputElement, any GCTouchedStateInput, Bool) -> Void)? { get set }
```

#### Discussion

Use this property to get the latest state of the touch input. The block’s parameters are:

## See Also

- [var isTouched: Bool](gctouchedstateinput/istouched.md)
  A Boolean value that indicates whether the user touches the button.
- [var lastTouchedStateTimestamp: TimeInterval](gctouchedstateinput/lasttouchedstatetimestamp.md)
  The time of the most recent touch state change.
- [var lastTouchedStateLatency: TimeInterval](gctouchedstateinput/lasttouchedstatelatency.md)
  The time in seconds between the last touch state change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gctouchedstateinput/toucheddidchangehandler)*