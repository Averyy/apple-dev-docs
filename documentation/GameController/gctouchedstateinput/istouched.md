# isTouched

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the user touches the button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var isTouched: Bool { get }
```

#### Discussion

For controllers that support capacitive touch, the user can start touching the button without pressure when the value property is `0`. For controllers that don’t support capacitive touch, the user starts touching the button when the value property is greater than `0`.

## See Also

- [var lastTouchedStateTimestamp: TimeInterval](gctouchedstateinput/lasttouchedstatetimestamp.md)
  The time of the most recent touch state change.
- [var lastTouchedStateLatency: TimeInterval](gctouchedstateinput/lasttouchedstatelatency.md)
  The time in seconds between the last touch state change and the current time.
- [var touchedDidChangeHandler: ((any GCPhysicalInputElement, any GCTouchedStateInput, Bool) -> Void)?](gctouchedstateinput/toucheddidchangehandler.md)
  A block that the element calls when its touch value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gctouchedstateinput/istouched)*