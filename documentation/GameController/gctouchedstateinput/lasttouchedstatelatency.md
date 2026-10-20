# lastTouchedStateLatency

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) NSTimeInterval lastTouchedStateLatency;
```

#### Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event.

## See Also

### Getting change information
- [var isTouched: Bool](./istouched.md)
  A Boolean value that indicates whether the user touches the button.
- [var lastTouchedStateTimestamp: TimeInterval](./lasttouchedstatetimestamp.md)
  The time of the most recent touch state change.
- [var touchedDidChangeHandler: ((any GCPhysicalInputElement, any GCTouchedStateInput, Bool) -> Void)?](./toucheddidchangehandler.md)
  A block that the element calls when its touch value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gctouchedstateinput/lasttouchedstatelatency)*