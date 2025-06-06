# lastValueTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The time of the most recent value change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var lastValueTimestamp: TimeInterval { get }
```

#### Discussion

This property isn’t a specific date and time. To determine the time between value changes, subtract a previous time from the current time.

## See Also

- [var value: Float](gclinearinput/value.md)
  The value in unit coordinates.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCLinearInput, Float) -> Void)?](gclinearinput/valuedidchangehandler.md)
  The block that the profile calls when an element’s value changes.
- [var lastValueLatency: TimeInterval](gclinearinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gclinearinput/lastvaluetimestamp)*