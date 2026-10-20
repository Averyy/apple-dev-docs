# lastValueTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) NSTimeInterval lastValueTimestamp;
```

#### Discussion

This property isn’t a specific date and time. To determine the time between value changes, subtract a previous time from the current time.

## See Also

### Getting the value
- [var value: Float](./value.md)
  The value along the axis, in unit coordinates.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxisInput, Float) -> Void)?](./valuedidchangehandler.md)
  The block that the input object calls when the value changes.
- [var lastValueLatency: TimeInterval](./lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxisinput/lastvaluetimestamp)*