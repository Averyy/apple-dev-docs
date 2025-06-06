# valueDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The block that the profile calls when an element’s value changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCLinearInput, Float) -> Void)? { get set }
```

#### Discussion

The block’s parameters are:

## See Also

- [var value: Float](gclinearinput/value.md)
  The value in unit coordinates.
- [var lastValueTimestamp: TimeInterval](gclinearinput/lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](gclinearinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gclinearinput/valuedidchangehandler)*